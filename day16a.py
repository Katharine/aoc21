# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import binascii
import bitstring

with open('day16.dat') as f:
    data = binascii.unhexlify(f.readline().strip())
    bs = bitstring.ConstBitStream(data)


class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id
        self.subpackets = []


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
        return Packet(version, type_id), data.bitpos - start
    length_type = data.read('uint:1')
    if length_type == 0:
        bits_to_read = data.read('uint:15')
        packet = Packet(version, type_id)
        inner_start = data.bitpos
        while (data.bitpos - inner_start) < bits_to_read:
            p, r = read_packet(data, depth+1)
            packet.subpackets.append(p)
    else:
        packets_to_read = data.read('uint:11')
        packet = Packet(version, type_id)
        for i in range(packets_to_read):
            p, r = read_packet(data, depth+1)
            packet.subpackets.append(p)
    return packet, data.bitpos - start


packet, read = read_packet(bs)

def sum_versions(packet: Packet) -> int:
    return packet.version + sum(map(sum_versions, packet.subpackets))

print(sum_versions(packet))
