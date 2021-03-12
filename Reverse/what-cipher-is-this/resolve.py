#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def XOR(inpString): 
    xorKey = 'A'
    length = len(inpString)
    for i in range(length):
        inpString = (inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i + 1:]) 
           
    return inpString

print(repr(XOR("MOCSCTF{RE_Pyth0n_byt3_c0d3}")))
#~\x82j\x8aj\x8cp\xda\x88n\xa2\x84\xd6\xcc\xb4D\xc0\xa2\xa8\xd6\xccJ\xa2\xaaD\xacJ\xde
print(repr(XOR("\x0c\x0e\x02\x12\x02\x15\x07:\x13\x04\x1e\x1185)q/\x1e#85r\x1e\"q%r<")))