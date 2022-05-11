# 2022-5-11

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

# Latitude: 1 deg = 110.574 km
# Longitude: 1 deg = 111.320*cos(latitude) km
def ll_to_meter(lat, lon):
    return [int(lat * 110574),
            int(lon * 111320 * math.cos(lat / pi / 180) ) ]

f = open('map-location.csv', 'r')
csv = f.readlines()
f.close()
C = []
CC = {}
cccc = 0
for l in csv[1:]:
    if not l:
        continue
    ls = l.split(',')
    if len(ls) > 3 and ls[0] not in C:
        C.append( ls[0].strip() )
        # 1经度 2纬度
        # 3 是否精确
        # 4 可信度
        # 6 bd09_to_wgs84
        if len(ls) > 7 and ls[6] == 'bd09':
            CC[ ls[0].strip() ] = bd09_to_wgs84(float(ls[1]), float(ls[2])
                                               ) + [ ls[3] ]
            cccc += 1
        else:
            CC[ ls[0].strip() ] = [ ls[1], ls[2], ls[3] ]
#if cccc:
#    print('bd09_to_wgs84() str format', cccc)


import itertools
unique_combinations = []
permut = itertools.permutations(C, len(C) )
for comb in permut:
    zipped = zip(comb, C)
    unique_combinations.append(list(zipped))
print(C)
print( len(unique_combinations) )


# j = {'date':datestr,
#      'tag':'AB',
#      'locations':CC }
# fz = open('shanghaifabu/map-location.json', 'w')
# fz.write("csv='%s'" % json.dumps(j, ensure_ascii=False) )
# #  jsonp  '%s(%s)' % (callback, out)
# fz.close()
# print('\ncheck inAB-not-map.txt, update map-location.csv and do ####\n')
