# Day8 - bjdctf_2020_babystack2（64 位 backdoor）

## 1. 环境
- 平台：BUUCTF
- 文件：`bjdctf_2020_babystack2`
- 保护：NX（无 PIE）

## 2. 漏洞
`read(0, buf, (unsigned int)nbytes)` → 64 位栈溢出

## 3. 绕过
- if ( (int)nbytes > 10 )
  {
    puts("Oops,u name is too long!");
    exit(-1);
  }
    对我们定义读入的数据长度这部分进行过滤
    利用unsigned关键字的只能表示0~4,294,967,295范围内的数的特性，输入负数会直接取能表示的最大值，进行绕过。
- **64 位控制**：用 `p64()` 和 `0x10 + 8`
- **64位控制**: 用'p64()' 和 后门地址'0x040072A'跳转后门，获取flag
## 4. 命令
```bash
python3 exp.py
