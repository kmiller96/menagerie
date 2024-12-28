# "Hello World!" Yew App

```bash
# Installing dependencies
rustup target add wasm32-unknown-unknown
cargo install --locked trunk

# Running the application
trunk serve

# Builds the application into /dist
trunk build --release
```