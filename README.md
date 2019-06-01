#### [调用官方API–快速执行脚本 DOC](doc/fourth-homework.md)

#### [接入一个自己研发的的API  DOC](doc/fifth-homework.md)

蓝鲸智云应用开发模板--助力你的自动化
这里有各种层次的应用样例，根据你的需要，选择合适的样例开始快速开发。

- 运行要求说明：

```
安装requirements.txt文件中的python包
安装mysql，并调整 config\dev.py里的DB用户名和密码
数据库初始化： 本模版工程的具体使用过程如下：
                      1. manage.py migate    (初始化数据库表)
                      2. 针对有表的application创建表：
                      例如：manage.py migrate home_application

在项目文件夹同级的目录里建立logs文件夹（如不清楚可以直接runserver后看错误提示信息）
```
 
目录说明：


- 公共包
	- blueapps：蓝鲸开发框架公共模块
	- blueking：蓝鲸应用网关模块
	- static：态文件(css, js, img)
	- templates：模版（django模版和mako模版，如果说ajax的子页面，模版文件可以使用其他后缀，如**.part）

- 配置包
    - config：用户配置包
    	- dev.py：开发环境配置，如 数据库
    	- stag.py： 测试环境配置
    	- prod.py：正式环境配置

- 应用包
	- home_application: 你的根应用包，用于开发你的应用的主要功能，子功能可以单独建立其他的应用包


#### 开发说明：

- 修改配置文件
	- conf/\_\_init__.py 文件：APP_ID \ APP_TOKEN （蓝鲸智云开发者中心 -> 点击应用ID -> 基本信息 中可以查看到这个两个值的信息）
	- conf/\_\_init__.py.py 文件：BK_PAAS_HOST（蓝鲸智云开发者中心的域名，形如：http://paas.bking.com）
	- conf/dev.py 文件：DATABASES（本地开发数据库信息）
	- conf/stag.py 文件：DATABASES（测试环境数据库信息）
	- conf/prod.py 文件：DATABASES（正式环境数据库信息）
