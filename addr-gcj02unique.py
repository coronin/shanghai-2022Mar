# 2022-5-15 not need after uniqueLL into addr-amap.py
#
#
#

import time

# https://github.com/wandergis/coordTransform_py
import math
pi = 3.1415926535897932384626 # π
a = 6378245.0 # 长半轴
ee = 0.00669342162296594323 # 偏心率平方

def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret

def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

def gcj02_to_wgs84(lng, lat):
    # if out_of_china(lng, lat):
    # return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [str(lng * 2 - mglng),
            str(lat * 2 - mglat) ]

def allMinus(full, to_remove):
    out = []
    for line in full:
        remove = False
        for to_ in to_remove:
            if line.find(to_) >= 0:
                remove = True
                break
        if not remove:
            out.append(line)
    return out


# 2022-7-25
aaa = [
            [
              121.50671354,
              31.32067543
            ],
            [
              121.50884162,
              31.32051378
            ],
            [
              121.51056916,
              31.32000223
            ],
            [
              121.51127377,
              31.31970425
            ],
            [
              121.51122653,
              31.31928705
            ],
            [
              121.51139718,
              31.31836529
            ],
            [
              121.51110096,
              31.31735824
            ],
            [
              121.51047416,
              31.31660933
            ],
            [
              121.5101061,
              31.31580242
            ],
            [
              121.50867996,
              31.31606005
            ],
            [
              121.50670328,
              31.31623107
            ],
            [
              121.50658254,
              31.31848215
            ],
            [
              121.50671354,
              31.32067543
            ]
          ]
print('[')
for aa in aaa:
    print('[', ','.join( gcj02_to_wgs84(aa[0], aa[1]) ), '],')
print(']   # remove the last comma')
raise
# 2022-6-12


files = ['ttt1652545705.txt','ttt1652546352.txt','ttt1652548410.txt',
         'ttt1652549660.txt','ttt1652545897.txt','ttt1652546593.txt',
         'ttt1652549146.txt','ttt1652550069.txt','ttt1652546124.txt',
         'ttt1652547662.txt','ttt1652549409.txt']

csv = []
for ff in files:
    f = open('/Users/liang/Downloads/%s' % ff, 'r')
    txt = f.readlines()
    f.close()
    for l in txt:
        if not l or l.startswith('#'):
            continue
        csv.append( l.strip() )
print('get:', len(csv))

uniqueLL = []
line_to_remove = []
for l in csv:
    ll = ','.join(l.split(',')[1:3])
    uniqueLL.append(ll)
    if uniqueLL.count(ll) == 2:
        print(l)
        line_to_remove.append(ll)
        continue

fz = open('/Users/liang/Downloads/done%s.txt' % int(time.time()), 'w')
fz.write('\n'.join(allMinus(csv, line_to_remove)))
fz.close