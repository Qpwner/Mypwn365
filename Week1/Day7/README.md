# Day7 - CTFShow babystack（64 位无 canary + backdoor）

## 1. 环境
- 平台：CTFShow
- 文件：`babystack`
- 保护：NX（无 canary、无 PIE）

## 2. 漏洞
`read(0, buf, (unsigned int)nbytes)` → 64 位栈溢出

## 3. 绕过
- **无 canary**：直接跳 backdoor()
- **64 位**：用 `p64()` 和 `0x10+8`

## 4. 命令
```bash
python3 exp.py
