#!/usr/bin/env python3
import string
from pwn import *

flag = open('flag.txt','rb').read()
lc = string.ascii_lowercase
uc = string.ascii_uppercase

def rot_n(s,n):
	return str.translate(s, str.maketrans(lc + uc,lc[n:] + lc[:n] + uc[n:] + uc[:n]))

conn = remote('172.17.0.2',9999,level='error')
round=1
conn.recvuntil("\n")
try:
	while True:
		chall = conn.recv(4096).strip().decode().split("\n")[0]
		print(repr(chall))
		for i in range(27):
			ans = rot_n(chall,i)
			if "msg is" in ans:
				conn.sendline(ans)
				print(ans)
		round+=1
		conn.recvuntil("ROUND "+str(round)+"\n")
		input("pause..")
except:
	print("###########################\n"*2)
	print(conn.recv())