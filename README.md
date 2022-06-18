# shanghai-2022Mar

根据上海发布的数据，手动整理每日感染者的地址
1. edit then python3 daily-AB.py
2. following screen suggestion, manual fix month-day.txt file
3. edit then python3 inA-not-inB-3.py
4. edit, drag and test drag-me.html
5. python3 -m http.server and test sh2.html
5. local: git push
6. remote web server, cd root folder: git pull

腾讯CDN已经启用，更新COS文件后需要URL刷新，比如
* https://cdn.teach.bio/map-location.json
* https://cdn.teach.bio/inAB-close.json
* https://cdn.teach.bio/full0616.json
* https://cdn.teach.bio/full0514.json
* https://cdn.teach.bio/full0505.json
如大量更改COS文件，可刷新CDN目录

### 本地运行
* git clone https://github.com/coronin/shanghai-2022Mar
* 把文件 drag-me.html 拖入支持ES6的浏览器，比如 firefox chrome edge
* 或者在代码所在目录运行 python3 -m http.server 然后网址访问 http://127.0.0.1:8000/sh2.html

### py文件
* daily-AB      用于更新每日地址，手动修正后移入 shanghaifabu/
* early-AB      提取早期 同地址的性别与年龄
* inA-not-inB-3 生成每日 full.json 更新地址文件 map-location.json
* addr-close    读入地址csv 更新临近地址文件 inAB-close.json（目前有1万多地址有待check）
* addr-close2   产生list用于合并地址
* addr-amap     读入待check文件 获取高德数据（存为 gcj02 精度51）

作者 @the_paper_link