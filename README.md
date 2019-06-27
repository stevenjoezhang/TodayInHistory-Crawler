# Today in History

通过爬取维基百科，获得“历史上的今天”数据库，并提供API。

## Requirements
Python3 and MySQL is required. You can use `apt-get`, `yum` or `brew` to install them.

## Install
```bash
# Clone this repository
git clone https://github.com/stevenjoezhang/TodayInHistory-Crawler.git
# Go into the repository
cd TodayInHistory-Crawler
# Install dependencies
pip3 install -r requirements.txt
```

## Run
在`spider.py`和`server.py`中有自定义的参数`username`、`password`和`dbname`，分别将它们修改为你的登录用户名、密码和数据库名。数据表名默认是`event`，也可以自行修改。先创建数据表，执行：
```sql
CREATE DATABASE dbname;
#建立数据库，dbname保持一致即可
USE dbname;
CREATE TABLE event (
  id int(10) UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  type int(1) DEFAULT NULL,
  year varchar(6) DEFAULT NULL,
  date varchar(6) DEFAULT NULL,
  info varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
QUIT;
```
然后，运行`spider.py`（如果中文维基百科无法正常访问，请使用代理）：
```bash
python3 spider.py
```  
程序会自动开始爬取数据。爬取失败的项目会被记录在`failed.txt`中，这个repo中有一份样例。失败的原因大多是由于字符集造成的问题。  
在爬取了1月1日到12月31日的数据后，就可以通过执行
```bash
python3 server.py
```
开启服务器，使用浏览器访问`localhost:8080`即可进行查询。

## Credits
* Inspired by [libowei1213](http://libowei.net).
* Revised by [Mimi](https://zhangshuqiao.org).

## License
Released under the GNU General Public License v3  
http://www.gnu.org/licenses/gpl-3.0.html
