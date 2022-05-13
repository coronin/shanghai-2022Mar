# shanghai-2022Mar

根据上海发布的数据，手动整理每日感染者的地址
1. python3 daily-AB.py
2. following screen suggestion, manual fix month-day.txt file
3. edit then python3 inA-not-inB-2.py
4. edit, drag and test drag-me.html and sh2.html
5. local: git push
6. web server, cd root folder: git pull

腾讯CDN已经启用，更新COS文件后需要URL刷新，比如
* https://cdn.teach.bio/map-location.json
* https://cdn.teach.bio/full0511.json
* https://cdn.teach.bio/full0505.json
如大量更改COS文件，可刷新CDN目录

### 本地运行
* git clone https://github.com/coronin/shanghai-2022Mar
* 把文件 drag-me.html 拖入支持ES6的浏览器，比如 firefox chrome edge
* 或者在代码所在目录运行 python3 -m http.server 然后网址访问 http://127.0.0.1:8000/sh2.html

作者 @the_paper_link