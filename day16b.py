# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import binascii


class Bitstream:
    def __init__(self, hex: str):
        self.data = ''.join(bin(x)[2:].zfill(8) for x in binascii.unhexlify(hex))
        self.bitpos = 0

    def read(self, bits: int) -> int:
        v = int(self.data[self.bitpos:self.bitpos+bits], 2)
        self.bitpos += bits
        return v


with open('day16.dat') as f:
    bs = Bitstream(f.readline().strip())


class Packet:
    def __init__(self, version):
        self.version = version
        self.subpackets = []

    def value(self):
        raise NotImplemented


class Value(Packet):
    def __init__(self, version, value):
        super(Value, self).__init__(version)
        self.v = value

    def value(self):
        return self.v


class Sum(Packet):
    def value(self):
        return sum(x.value() for x in self.subpackets)


class Product(Packet):
    def value(self):
        prod = 1
        for x in self.subpackets:
            prod *= x.value()
        return prod


class Minimum(Packet):
    def value(self):
        return min(x.value() for x in self.subpackets)


class Maximum(Packet):
    def value(self):
        return max(x.value() for x in self.subpackets)


class GreaterThan(Packet):
    def value(self):
        a = self.subpackets[0].value()
        b = self.subpackets[1].value()
        return int(a > b)


class LessThan(Packet):
    def value(self):
        a = self.subpackets[0].value()
        b = self.subpackets[1].value()
        return int(a < b)


class Equal(Packet):
    def value(self):
        a = self.subpackets[0].value()
        b = self.subpackets[1].value()
        return int(a == b)


type_mapping = {
    0: Sum,
    1: Product,
    2: Minimum,
    3: Maximum,
    5: GreaterThan,
    6: LessThan,
    7: Equal,
}

def read_packet(data: Bitstream) -> Packet:
    version = data.read(3)
    type_id = data.read(3)
    if type_id == 4:
        value = 0
        while True:
            is_last = data.read(1)
            chunk = data.read(4)
            value = (value << 4) | chunk
            if not is_last:
                break
        return Value(version, value)
    length_type = data.read(1)
    if length_type == 0:
        bits_to_read = data.read(15)
        packet = type_mapping[type_id](version)
        inner_start = data.bitpos
        while (data.bitpos - inner_start) < bits_to_read:
            p = read_packet(data)
            packet.subpackets.append(p)
    else:
        packets_to_read = data.read(11)
        packet = type_mapping[type_id](version)
        for i in range(packets_to_read):
            p = read_packet(data)
            packet.subpackets.append(p)
    return packet


packet = read_packet(bs)

print(packet.value())
