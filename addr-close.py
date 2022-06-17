within = 125
nearby = 12 # 仅用于输出check.txt
# 2022-5-11 init
# 2022-5-14 amap gcj02

# https://github.com/wandergis/coordTransform_py
import math
x_pi = 3.14159265358979324 * 3000.0 / 180.0
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

def bd09_to_gcj02(bd_lon, bd_lat):
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]

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

def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)

# https://stackoverflow.com/questions/1253499/
# delta latitude: 1 deg = 110.574 km
# delta longitude: 1 deg = 111.320*cos(latitude) km
def ll_to_meter(dlat, mlat, dlon):
    d0 = int(abs(dlat) * 110574)
    d1 = int(abs(dlon) * 111320 * math.cos(pi * mlat/180) )
    return int(math.sqrt(math.pow(d0,2) + math.pow(d1,2) ))


import json
f = open('shanghaifabu/map-location.json', 'r')
fj = json.loads( f.read()[5:-1] )
f.close()
CC = fj['locations']
C = list( CC.keys() )

print('total unique address:', len(C) )

print('lon E', CC['杨浦区国权北路1566弄'][0], 'lat N', CC['杨浦区国权北路1566弄'][1])
print('lon E', CC['杨浦区国权北路1450弄'][0], 'lat N', CC['杨浦区国权北路1450弄'][1])
print('Haversine formula 2943m vs', ll_to_meter(
    float(CC['杨浦区国权北路1566弄'][1]) - float(CC['杨浦区国权北路1450弄'][1]),
    (float(CC['杨浦区国权北路1566弄'][1]) + float(CC['杨浦区国权北路1450弄'][1]))/2,
    float(CC['杨浦区国权北路1566弄'][0]) - float(CC['杨浦区国权北路1450弄'][0]) ))

U = C[0]
V = C[1:]
W = []
ww = {}
www = 0
while V:
    for v in V:
        Uv = ll_to_meter(float(CC[U][1]) - float(CC[v][1]),
                         (float(CC[U][1]) + float(CC[v][1]))/2,
                         float(CC[U][0]) - float(CC[v][0]) )
        if Uv < within: ####
            if U not in W:
                W.append(U)
            W.append(v)
            if ww.get(U):
                ww[U] += [v]
            else:
                ww[U] = [v]
            if ww.get(v):
                ww[v] += [U]
            else:
                ww[v] = [U]
            #V.remove(v)
    U = V[0]
    V.pop(0)
    www += 1
    if www % 10000 == 0:
        print('>> V remain:', '%s, www ' % len(V), www)

print('addresses into ww:', len(W) )
print('ww object size:', len(ww) )
#print(ww)

to_check = []
for key,val in ww.items():
    if len(val) > nearby:
        # 2022-5-24 print('>>', key, len(val) )
        if not key in to_check:
            to_check.append(key)
        for vv in val:
            if not vv in to_check:
                to_check.append(vv)

from datetime import datetime
datestr = '%s' % datetime.now()
fz = open('addr-close-check.txt', 'w')
fz.write('# AB %s 可信度30' % datestr)
fz.write('\n# https://console.amap.com/dev/')
fz.write('\n%s' % '\n'.join(to_check) )
fz.write('\n####')
fz.close

j = {'date':datestr,
     'within':within,
     'ww size':len(ww),
     'tag':'AB',
     'pairs':ww }
fz = open('shanghaifabu/inAB-close.json', 'w')
fz.write( json.dumps(j, ensure_ascii=False) )
fz.close()