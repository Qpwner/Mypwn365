## Day9 - 任意64位无canary（64 位无 canary + backdoor）

1. **保护**：NX（无 canary、无 PIE）
2. **漏洞**：`read(0, buf, 0x200ull)` → 64 位栈溢出
3. **绕过**：输送0x100+8个垃圾数据后直接跳 backdoor()
4. **结果**：`NSSCTF{f3632346-8397-46cf-a97d-01d27ea47b43}`
