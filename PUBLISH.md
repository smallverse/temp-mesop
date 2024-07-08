
# create a Dockerfile for it

https://docs.docker.com/language/rust/build-images/

init in code directory
```shell
docker init
```
---

### build by docker-compose

```shell
#docker compose up --build
docker compose build
```
---


### run in local by shell

```shell
# https://docs.anaconda.com/miniconda/#quick-command-line-install
#conda create -n python310 python=3.10
#conda activate
#conda deactivate
conda activate python310

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

```

```shell


python -m main


```

## run in docker by docker-compose

### build and run by docker-compose
#### rebuild
```shell
docker compose up --build --force-recreate
```

```shell
docker compose up --build -d --force-recreate
```
---
#### not rebuild
```shell
docker compose up --force-recreate

```
```shell
docker compose up -d --force-recreate

```
