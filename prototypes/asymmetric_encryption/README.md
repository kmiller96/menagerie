# Asymmetric Encryption

Playing around with encrypting plain files using asymmetric encryption.

## Generating Keys

```bash
cargo run generate public.pem private.pem
```

## Encrypting

```bash
cargo run encrypt public.pem message.txt  # Prints base64 to stdout.
```

## Decrypting

```bash
cargo run decrypt private.pem message.secret
```
