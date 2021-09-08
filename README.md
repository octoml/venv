***OctoML and the cTuning foundation donated this repository to MLCommons: https://github.com/mlcommons/ck-venv***


# Virtual CK environment

[![compatibility](https://github.com/ctuning/ck-guide-images/blob/master/ck-compatible.svg)](https://github.com/ctuning/ck)
[![automation](https://github.com/ctuning/ck-guide-images/blob/master/ck-artifact-automated-and-reusable.svg)](https://youtu.be/7zpeIVwICa4)

This [CK](https://github.com/ctuning/ck) repository provides automation 
for virtual environments on Linux and Windows.

## License

Apache 2.0

## Installation

### Install CK framework
Install CK framework and prerequisites as descrbied in [this guide](https://ck.readthedocs.io/en/latest/src/installation.html).

In most cases, you can install ck using pip as follows:

```
pip install ck
```
or
```
python3 -m pip install ck
```
or
```
pip3 install ck --user
```

### Install virtualenv

```
pip3 install virtualenv
```

### Pull this repository via CK

```
ck pull repo:ck-venv
```

If you use Windows, you need to pull an extra repository:
```
ck pull repo:ck-win
```

### Update all CK repositories

You can update all CK repositories from time to time using the following command:
```
ck pull all
```

## Usage

* [From the native environment](README.native.md)
* [From containers](README.docker.md)

## Problems

Don't hesitate to report issues or submit feature requests [here](https://github.com/ctuning/ck-venv/issues).

## Motivation

* [OctoML.ai](https://OctoML.ai)
* [White paper](https://arxiv.org/pdf/2006.07161.pdf) and [extended journal article](https://arxiv.org/pdf/2011.01149.pdf)
* [ACM TechTalk on YouTube](https://www.youtube.com/watch?=7zpeIVwICa4)
