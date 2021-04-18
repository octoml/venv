# OS prerequisites

Minimal for Ubuntu:
```
sudo apt-get install libffi-dev
sudo apt-get install libssl-dev openssl
```

Max for Ubuntu:

```
sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev
```

# Installation

```
ck install package --tags=compiler,python
```

CK will ask you to select a version (variation).

# Environment flags

```
ck install package --tags=compiler,python --env.KEY=VALUE
```

* --env.ENABLE_OPTS=yes | --env.ENABLE_OPTS

  Enable optimizations (very slow compilation: ~30..60 min)

* --env.ENABLE_SHARED=""

  Turn off shared libraries

* --env.WITH_ENSUREPIP=yes | --env.WITH_ENSUREPIP

  Ensure that pip is installed too
