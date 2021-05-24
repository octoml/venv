# Adaptive CK containers

## Prerequisites

You need to have docker installed on your system.

## List available docker images

```
ck ls docker
```

We plan to add CK adaptive container templates 
for other popular Linux distributions 
including amazonlinux, centos and debian.

## Build some container

```
ck build docker:{name from the above list}
```

For example:
```
ck build docker:ck-template-ml --tag=ubuntu-20.04
```

## Run container in the interactive mode

```
ck run docker:ck-template-ml --tag=ubuntu-20.04
```

You can now issue CK commands to pull CK-compatible repositories
build packages and run workflows in a unified way.
