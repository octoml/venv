# CK virtual environment

## Prerequisites

You need to have git, python, pip and virtualenv installed on your system.

## CK framework

Install [CK framework](https://github.com/ctuning/ck):
```
pip install ck
```
or
```
python3 -m pip install ck
```

In case of problems, please follow [this guilde](https://ck.readthedocs.io/en/latest/src/installation.html)

## CK venv automation repository 

Pull CK repository with virtual environment automation:
```
ck pull repo --url=https://github.com/octoml/ck-venv
```

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

## Find where the virtual environment is located

```
ck find venv:test1
```

## Install and use another python

Some projects require a specific python version that may not be installed on your system.
In such case you can use a CK python package to automatically download 
and install a required python version as follows (for example, MLPerf inference v0.7+ 
requires Python 3.7+ which may not be available on your system):
```
ck install package --tags=compiler,python
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
