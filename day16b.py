# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import binascii
import bitstring

with open('day16.dat') as f:
    data = binascii.unhexlify(f.readline().strip())
    bs = bitstring.ConstBitStream(data)
    print(bs)


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

def read_packet(data: bitstring.ConstBitStream, depth=0) -> (Packet, int):
    start = data.bitpos
    version = data.read('uint:3')
    type_id = data.read('uint:3')
    if type_id == 4:
        value = 0
        while True:
            is_last = data.read('uint:1')
            chunk = data.read('uint:4')
            value = (value << 4) | chunk
            if not is_last:
                break
        return Value(version, value), data.bitpos - start
    length_type = data.read('uint:1')
    if length_type == 0:
        bits_to_read = data.read('uint:15')
        packet = type_mapping[type_id](version)
        inner_start = data.bitpos
        while (data.bitpos - inner_start) < bits_to_read:
            p, r = read_packet(data, depth+1)
            packet.subpackets.append(p)
    else:
        packets_to_read = data.read('uint:11')
        packet = type_mapping[type_id](version)
        for i in range(packets_to_read):
            p, r = read_packet(data, depth+1)
            packet.subpackets.append(p)
    return packet, data.bitpos - start


packet, read = read_packet(bs)

print(packet.value())
