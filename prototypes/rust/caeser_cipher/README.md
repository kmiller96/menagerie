# Caeser Cipher

Takes a file (or stdin) and performs a caeser cipher.

Usage:

```bash
<program> encrypt --secret 14 file.txt 
```

## Quickstart

```bash
echo "My secret message" | cargo run -- encrypt --secret=10 - > message.txt
cargo run -- decrypt --secret=10 message.txt
```