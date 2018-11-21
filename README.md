# Today in History

通过爬取维基百科，获得“历史上的今天”数据库，并提供API。

## Requirements
python3, mysql and php is required. You can use `apt-get`, `yum` or `brew` to install them.

## Install
```bash
git clone https://github.com/stevenjoezhang/TodayInHistory-Crawler.git
cd TodayInHistory-Crawler
```

## Run
修改`mysql.py`和`index.php`中的参数`username`、`password`和`dbname`，分别是你的登录用户名、密码和数据库名。数据表名默认是event，也可以自行修改。先创建数据表，执行：
```sql
create database dbname;
#建立数据库images
use dbname;
CREATE TABLE `event` (
  `type` int(1) DEFAULT NULL,
  `year` varchar(6) DEFAULT NULL,
  `date` varchar(6) DEFAULT NULL,
  `info` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
然后，运行`today.py`（如果中文维基百科无法正常访问，请使用该文件中提供的代理）：
```bash
python3 today.py
```
在爬取了1月1日到12月31日的数据后，就可以通过访问`index.php`进行查询了。  
爬取失败的项目会被记录在`error.txt`中，这里有一份样例，大多是由于字符集造成的问题。

## Credits
* [libowei1213](http://libowei.net) Developer of this project.
* Revised by [Mimi](https://zhangshuqiao.org).

## License
Released under the GNU General Public License v3  
http://www.gnu.org/licenses/gpl-3.0.html
