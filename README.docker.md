# Adaptive CK containers

## Prerequisites

You need to have docker installed on your system.

## List available docker images

```
ck ls docker
```

## Build selected docker

```
ck build docker:{name from above}
```

For example:
```
ck build docker:ck-template-ml-x8664-ubuntu-20.04
```

## Run docker image (interactive mode)

```
ck run docker:ck-template-ml-x8664-ubuntu-20.04
```

You can now issue CK commands to pull CK-compatible repositories
build packages and run workflows in a unified way.
