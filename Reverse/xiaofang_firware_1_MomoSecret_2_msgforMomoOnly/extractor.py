#!/usr/bin/env python3

import sys

class FirmwarePart:
    def __init__(self, name, offset, size):
        self.name = name
        self.offset = offset
        self.size = size

firmware_parts = [
    FirmwarePart("header_1", 0x0, 0x240000),
    FirmwarePart("squashfs_1", 0x240000, 0x590000),
    FirmwarePart("squashfs_2", 0x590000, 0x63000C),
    FirmwarePart("header_2", 0x63000C, 0xCD0000),
    FirmwarePart("squashfs_3", 0xCD0000, 0xD7000C),
    FirmwarePart("header_3", 0xD7000C, 16777216-0xD7000C)
]

if sys.argv[1] == "unpack":
    f = open(sys.argv[2], "rb")
    for part in firmware_parts:
        outfile = open(part.name, "wb")
        f.seek(part.offset, 0)
        data = f.read(part.size)
        outfile.write(data)
        outfile.close()
        print(f"Wrote {part.name} - {hex(len(data))} bytes")
elif sys.argv[1] == "pack":
    f = open(sys.argv[2], "wb")
    for part in firmware_parts[1:]:
        i = open(part.name, "rb")
        data = i.read()
        f.write(data)
        padding = (part.size - len(data))
        print(f"Wrote {part.name} - {hex(len(data))} bytes")
        print(f"Padding: {hex(padding)}")
        f.write(b'\x00' * padding)