# 使用方法

本项目依赖`scrapy`库。

安装依赖后，执行

```bash
scrapy crawl movie -O movie.json
```

爬取电影信息，并保存到`movie.json`文件中。

执行

```bash
scrapy crawl comment -O comment.json
```

爬取所有短评信息，并保存到`comment.json`文件中。
