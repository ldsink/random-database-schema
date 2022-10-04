# random-database-schema

> 随机出一个非常大的数据库 Schema

## 特点

* 使用 poetry 管理依赖
* 模块化，可以方便的换成其他数据库，目前支持 ClickHouse
* 单入口，使用简单

## 使用

```
# 克隆项目
git clone https://github.com/ldsink/random-database-schema
cd random-database-schema

# 安装依赖
poetry install

# 设置参数开始生成数据库
poetry run python main.py
```

## TODO

* 支持其他数据库
* 生成速度更快
