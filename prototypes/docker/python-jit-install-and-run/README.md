# Python Just-in-Time Install & Run

Installs a python package and runs the supplied args just in time.

## Demo

```bash
docker build -t tap-clockify .
docker run tap-clockify \
    git+https://github.com/quantile-taps/tap-clockify.git \
    tap-clockify --help
```
