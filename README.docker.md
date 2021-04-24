# Adaptive CK containers

## Prerequisites

You need to have docker installed on your system.

## List available docker images

```
ck ls docker
```

Available docker images:
* ck-template-ml-nvidia-cuda-10.2-tensorrt-6-ubuntu-18.04
* ck-template-ml-nvidia-cuda-10.2-tensorrt-7-ubuntu-18.04
* ck-template-ml-x8664-tf-2.1.0-mkl-ubuntu-18.04
* ck-template-ml-x8664-tf-2.3.0-avx512-mkl-ubuntu-18.04
* ck-template-ml-x8664-ubuntu-20.04

We plan to add CK adaptive container templates 
for other popular Linux distributions 
including amazonlinux, centos and debian.

## Build some container

```
ck build docker:{name from above}
```

For example:
```
ck build docker:ck-template-ml-x8664-ubuntu-20.04
```

## Run container in the interactive mode

```
ck run docker:ck-template-ml-x8664-ubuntu-20.04
```

You can now issue CK commands to pull CK-compatible repositories
build packages and run workflows in a unified way.
