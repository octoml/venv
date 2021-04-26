# Virtual CK environment

[![compatibility](https://github.com/ctuning/ck-guide-images/blob/master/ck-compatible.svg)](https://github.com/ctuning/ck)
[![automation](https://github.com/ctuning/ck-guide-images/blob/master/ck-artifact-automated-and-reusable.svg)](https://youtu.be/7zpeIVwICa4)

## Prerequisites

You need to have git, python, pip and virtualenv installed on your system.

### CK framework

Install [CK](https://github.com/ctuning/ck) :
```
pip3 install ck
```
or
```
python3 -m pip install ck
```

In case of problems, please follow [this guide](https://ck.readthedocs.io/en/latest/src/installation.html).

### CK venv automation repository

Pull CK repository with virtual environment automation:
```
ck pull repo --url=https://github.com/octoml/ck-venv
```

### Windows
If your host OS is Windows, please pull the following repository 
with extra CK components for Windows:
```
ck pull repo:ck-win
```

### Update all repositories

You can update all CK repositories from time to time using the following command:
```
ck pull all
```

## Installation and usage

* [Native installation](README.native.md)
* [CK adaptive containers](README.docker.md)

## Problems

Don't hesitate to report issues or submit feature requests.

## Motivation

* [White paper](https://arxiv.org/pdf/2006.07161.pdf) and [extended journal article](https://arxiv.org/pdf/2011.01149.pdf)
* [ACM TechTalk on YouTube](https://www.youtube.com/watch?=7zpeIVwICa4)
