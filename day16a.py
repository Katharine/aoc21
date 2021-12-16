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
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id
        self.subpackets = []


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
        return Packet(version, type_id)
    length_type = data.read(1)
    if length_type == 0:
        bits_to_read = data.read(15)
        packet = Packet(version, type_id)
        inner_start = data.bitpos
        while (data.bitpos - inner_start) < bits_to_read:
            p = read_packet(data)
            packet.subpackets.append(p)
    else:
        packets_to_read = data.read(11)
        packet = Packet(version, type_id)
        for i in range(packets_to_read):
            p = read_packet(data)
            packet.subpackets.append(p)
    return packet


packet = read_packet(bs)

def sum_versions(packet: Packet) -> int:
    return packet.version + sum(map(sum_versions, packet.subpackets))

print(sum_versions(packet))
