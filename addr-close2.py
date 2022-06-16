within = 2
# 2022-6-16 上榜地址统一 区+最短独特地址

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

# delta latitude: 1 deg = 110.574 km
# delta longitude: 1 deg = 111.320*cos(latitude) km
def ll_to_meter(dlat, dlon):
    d0 = int(abs(dlat) * 110574)
    d1 = int(abs(dlon) * 111320 * math.cos(abs(dlat) / pi / 180) )
    return int(math.sqrt(math.pow(d0,2) + math.pow(d1,2) ))


f = open('map-location.csv', 'r')
csv = f.readlines()
f.close()
C = []
CC = {}
cccc = 0
cccd = 0
nnnn = 0
a_ = 0
aa = 1
print('will process:', len(csv)-aa)
XX = []
for l in csv[aa:2000]: # [1:]
    a_ += 1
    if not l:
        continue
    # if len(l) > 60:
    #     print('\n\n\n\n%s' % (aa+a_), l, )
    #     raise
    ls = l.split(',')
    if len(ls) > 4 and ls[1] and ls[2] and ls[4]:
        if int(ls[4]) <= 30: # 可信度 大于30
            nnnn += 1
            XX.append( ls[0].strip() )
            continue
        if ls[0] not in C:
            C.append( ls[0].strip() ) # C内无重复
        # 1经度 2纬度
        # 3 是否精确
        # 4 可信度
        # 6 bd09_to_wgs84 gcj02_to_wgs84
        if len(ls) > 7 and ls[6] == 'bd09':
            CC[ ls[0].strip() ] = bd09_to_wgs84(float(ls[1]), float(ls[2])
                                               ) + [ ls[3] ]
            cccc += 1
        elif len(ls) > 7 and ls[6] == 'gcj02':
            #gcj02unique
            CC[ ls[0].strip() ] = gcj02_to_wgs84(float(ls[1]), float(ls[2])
                                                ) + [ ls[3] ]
            cccd += 1
        else:
            CC[ ls[0].strip() ] = [ ls[1], ls[2], ls[3] ]

from datetime import datetime
datestr = '%s' % datetime.now()

if cccc:
    print('bd09_to_wgs84() str format:', cccc)
if cccd:
    print('gcj02_to_wgs84() str format:', cccd)
if nnnn:
    print('list: not precise location', nnnn)
    fz = open( 'addr-close2-30.txt', 'w')
    fz.write('# addr-close2.py %s\n' % datestr)
    fz.write('\n'.join( sorted(list(set(XX))) ))
    fz.write('\n####')
    fz.close
print('total unique address:', len(C) )

# print('国权北路1450到1560距离',
#       ll_to_meter(float(CC['杨浦区国权北路1566弄'][0]) - float(CC['杨浦区国权北路1450弄'][0]),
#                   float(CC['杨浦区国权北路1566弄'][1]) - float(CC['杨浦区国权北路1450弄'][1]) ))

U = C[0]
V = C[1:]
W = []
ww = {}
www = 0
while V:
    for v in V:
        Uv = ll_to_meter(float(CC[U][0]) - float(CC[v][0]),
                         float(CC[U][1]) - float(CC[v][1]) )
        if Uv < within: ####
            if U not in W:
                W.append(U)
            if v not in W:
                W.append(v)
            # W是索引 ww是距离很近的列表
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

Wls = sorted(list(set(W))) # for key,val in ww.items():

def abcdef(L):
    return L

fz = open( 'addr-close2-list.txt', 'w')
fz.write('# addr-close2.py %s\n' % datestr)
import collections
W0 = [Wls[0]] + sorted(ww[ Wls[0] ])
for Wi in Wls[1:]:
    if len( list(set(W0)) ) == 1:
        W0 = [Wi] + sorted(ww[Wi])
        continue
    if len( list(set([Wi] + ww[Wi])) ) == 1:
        continue
    if collections.Counter(W0) == collections.Counter( [Wi] + ww[Wi] ):
        continue
    else:
        W0d = W0[0][:3]
        W0jj = []
        W0jj.append(W0[0])
        for W0j in W0[1:]:
            if W0j[:3] == W0d:
                W0jj.append(W0j)
        if len(W0jj) > 1:
            fz.write('%s\n' % ','.join(abcdef(W0jj)) )
        W0 = [Wi] + sorted(ww[Wi])
fz.write('####')
fz.close
