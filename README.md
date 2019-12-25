# Seeta QAServer

## 项目目录结构说明

```text
.
|____docs                 # 文档说明
|____qaserver             # 项目目录
| |____handlers           # 处理逻辑和路由映射、C控制层
| | |____base             # 处理基类，其他业务处理类可以继承这个基类
| | |____public           # 业务处理类
| | |____urls.py          # 路由配置文件
| |____libs               # 库文件，做一些中间层的封装，解耦合
| |____logs               # 日志文件
| |____models             # 模型类，处理数据库交互
| |____settings           # 项目配置文件
| |____static             # 静态文件，存放js、css、html、img等
| |____templates          # 模板，存放html页面
| |____utils              # 工具类，例如：验证码生成、IP地址转换
|____tests                # 单元测试
|____venv                 # python虚拟运行时环境
|____build.py             # 项目编译脚本+
|____setup.py             # 项目打包脚本
|____runserver.py         # 项目启动文件
|____requirements.txt     # 项目依赖包
|____README.md            # 项目说明文件
```