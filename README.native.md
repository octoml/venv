# CK virtual environment (native installation)

## Prerequisites

You need to have docker installed on your system.

## Create virtual environment with existing Python

Run the following command:
```
ck create venv:test1
```

CK will attempt to detect existing python versions and will ask you which one to use for your virtual environment.

## Activate created virtual environment

```
ck activate venv:test1
```

## Detect another installed python to be used for virtual environment

You can detect another python version installed on your system 
that can be used to create CK virtual environments as follows:

```
ck detect soft --tags=compiler,python
```

You can specify extra paths where to search for it as follows:
```
ck detect soft:compiler.python --search_dirs={directories separated by comma}
```

You can force CK to search for Python only in one specific directory:
```
ck detect soft:compiler.python --search_dir={path to python installation}
```

If your host OS is Windows, you can manually download and install a required Python version 
from [here](https://www.python.org/downloads/windows/) and then use above CK commands 
to detect the new installation.

## Install and use another python

Some projects require a specific python version that may not be installed on your system.
In such case you can use a CK python package to automatically download 
and install a required python version as follows (for example, MLPerf inference v0.7+ 
requires Python 3.7+ which may not be available on your system):
```
ck install package --tags=compiler,python,src
```

Note that you may need to have some system dependencies installed. Typical dependencies for Ubuntu:
```
sudo apt install libglib2.0-0 libsm6 \
                 git wget bzip2 zip libz-dev \
                 cmake \
                 libssl-dev libbz2-dev libffi-dev
```

It may take several minutes depending on your system.

You can turn on optimizations as follows:
```
ck install package --tags=compiler,python --env.ENABLE_OPTS=yes
```

But note that it may take 1 hour to build such python. 
You can find all customization options in [the readme](https://github.com/octoml/ck-venv/tree/main/package/python-from-src) 
of this CK package.

You can also install python without shared libraries as follows:
```
ck install package --tags=compiler,python --env.ENABLE_SHARED=""
```

You can then create a virtual environment with the new python using the same CK command as before:
```
ck create venv:test2
```

CK will detect that a new Python version is installed and will ask you to use it.

## List all available virtual environments
```
ck ls venv
```

## Find where a given virtual environment located:

```
ck find venv:test1
```

## Delete a given virtual environment
```
ck rm venv:test1
```
