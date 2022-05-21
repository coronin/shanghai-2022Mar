from bs4 import BeautifulSoup
from urllib import request
import json
import os
# os.system('scrapy fetch --nolog https://www.cell.com/cell/newarticles > cell.txt')
import re

districts = ('浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区',
             '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区',
             '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区' )
running_d = ''

_z = (
['0317','https://wsjkw.sh.gov.cn/xwfb/20220318/dc6e1aca667a45a682f32ac514c6062e.html'],
#0317最后一个 男,29 大木桥路450弄
['0316','https://wsjkw.sh.gov.cn/xwfb/20220317/46f73d4d70b54982b04c925eea6cb031.html'],
['0315','https://wsjkw.sh.gov.cn/xwfb/20220316/18a627b694eb471f9a415dfa20b6d0b4.html'], #区地址个数 200
['0314','https://wsjkw.sh.gov.cn/xwfb/20220315/e2b0122c52304fe0a41a8b726b3413d2.html'], #区地址个数 138
['0313','https://wsjkw.sh.gov.cn/xwfb/20220314/ea83d1b33a2e40fea7de115c16cbae8a.html'],
['0312','https://wsjkw.sh.gov.cn/xwfb/20220313/ac598c0104ad49f8913df20d794d68d1.html'], #区地址个数 64
['0311','https://wsjkw.sh.gov.cn/xwfb/20220312/559cc1eb3e9646b6a08b28ce340a3463.html'], #区地址个数 81
['0310','https://wsjkw.sh.gov.cn/xwfb/20220311/a7bb01fac3664085a882d46dc4e194ba.html'], #区地址个数 74
['0309','https://wsjkw.sh.gov.cn/xwfb/20220310/c7a3763da0cd46cbb563df4064ee1a15.html'], #区地址个数 77
['0308','https://wsjkw.sh.gov.cn/xwfb/20220309/077a50ff4cf4422d836e857126008ff6.html'],
['0307','https://wsjkw.sh.gov.cn/xwfb/20220308/a2f9fa49a4274509a1a42fa871bf77ee.html'], #区地址个数 55
['0306','https://wsjkw.sh.gov.cn/xwfb/20220307/6490dbd707674b278f40159595aa5cd9.html']
#0306最后一个 男,17 宝安公路3705弄
      )
## no place info before 3/6
## 从3月18日起三天内，我市对非重点区域内人员分时分批次开展一次免费核酸检测
## 从3月13日启动校园封闭管理

checked_tags = ('0306', '0317')
used_kd = []
_data = []
for z in _z:
    print('\n%s' % z[1])
    if z[1].endswith('.html'):
        if not os.path.isfile('shanghaifabu/%s%s.txt' % (z[0],z[0])):
            os.system('scrapy fetch --nolog %s > %s%s.txt' % (z[1], z[0],z[0]) )
        f = open('shanghaifabu/%s%s.txt' % (z[0],z[0]), 'r')
        page = f.read()
        f.close()
        pp = BeautifulSoup(page, features="lxml").find('div', {'id' : 'ivs_content'}).get_text("\n", strip=True)
        ppp = re.findall(r'，居住于(\S{2,3}区[^，。]+)', pp ) + re.findall(r'，居住地为(\S{2,3}区[^，。]+)', pp )
        #print('就读于', re.findall(r'，就读于(\S{2,3}区[^，。]+)', pp) )
        #print('外省市', re.findall(r'，外省市([^，。]+)', pp) )
        cc = re.findall('24时，新增本土[^0-9]+(\d{1,3})', pp)[1:]
        if cc and sum([int(ccc) for ccc in cc]) != len(ppp):
            print('搜到新增本土数', '+'.join(cc) )
            print('搜到区地址个数', len(ppp))
            #print('\n'.join(ppp) )
        wxx = re.sub(r'(\S{2,3})区', r'\1区,', '\n'.join(ppp) )
    else:
        raise ValueError('只能处理网页')

    res = wxx.replace('，', ',').replace('。', ',').replace('、', ',').replace('；', ',').replace(';', ','
            ).replace(' ', ',').replace('\t', ','
            ).replace('分别居住于', ',').replace('：', ','
            ).replace('我区', ',,,,').replace('已对相关', ',')

    #Z = [ s.strip() for s in list(filter(None, res.split(',') )) ]
    Z = [ s.strip() for s in filter(None, res.split(',') ) ]
    #print(len(Z))
    ZZ = re.sub(r'\s', ',', '\n'.join(Z))
    pps = re.sub(r'\s', '', pp).replace('闵行校区', '闵行区')
    #print(pps)
    running_k = ''
    _regex = r"(\S)，(\d+)岁"
    xx = re.findall(_regex, pps)
    #x = re.findall(rf"(\S，\d+)岁\S+{zz}", pps)
    xi = 0
    data = {}
    max_d = ''
    max_dc = 0
    _ZZ = ZZ.split(',')
    for zi,zzz in enumerate(_ZZ):
        # if len( zz.strip() ) > 20: # 5/18 金山区
        #     print('%s\n' % zz.strip() )
        # elif zz.find('成功') > -1 or zz.find('目前') > -1:
        #     print('## 成功 | 目前\n%s\n' % zz.strip() )
        ####
        zz = zzz.replace('闵行校区', '闵行区')
        if not zz or zz in districts:
            running_k = zz
            continue
        if (zi+1) < len(_ZZ) and _ZZ[zi+1] == '宿舍':
            zz += _ZZ[zi+1]
            _ZZ[zi+1] = ''
        elif (zi+1) < len(_ZZ) and re.match(r'\d+\D', _ZZ[zi+1]):
            zz += _ZZ[zi+1]
            _ZZ[zi+1] = ''
        elif (zi+2) < len(_ZZ) and re.match(r'\d+$', _ZZ[zi+1]):
            zz += _ZZ[zi+1] + _ZZ[zi+2]
            _ZZ[zi+1] = ''
            _ZZ[zi+2] = ''
        if not zz in used_kd:
            used_kd += [running_k + zz]
        #if xi and not xi%20:# or xi in range(30,40): #@@@@
        if xi and not z[0] in checked_tags:
            print('    ', xi, ','.join(xx[xi]), zz)
        try:
            if data.get(running_k + zz):
                data[running_k + zz] += [[z[0]] + list(xx[xi])]
                if len(data[running_k + zz]) > max_dc:
                    max_dc = len(data[running_k + zz])
                    max_d = running_k + zz
            else:
                data[running_k + zz] = [[z[0]] + list(xx[xi])]
        except:
            raise ValueError(z[0], running_k, zz, xi, len(xx) )
        xi += 1
    if not z[0] in checked_tags:
        print('#%s最后一个' % z[0], ','.join(xx[xi-1]), zz)
        print('    最大', max_d, max_dc ) #, data[max_d]
    if max_dc != len(re.findall(max_d, pps)):
        raise ValueError(z[0], max_d, max_dc, len(re.findall(max_d, pps)) )
    _data += [data]
####
fz = open('early%s.json' % z[0], 'w')
fz.write( json.dumps(_data, ensure_ascii=False) )
fz.close()
