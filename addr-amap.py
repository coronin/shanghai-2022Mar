import urllib.request
import urllib.parse
import json
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


f = open('inAB-close-check.txt', 'r')
txt = f.readlines()
f.close()
C = []
for l in txt[2:]:
    if not l or l.startswith('#'):
        continue
    C.append( l.strip() )
print('will process:', len(C))
csv = []

# addr = ['徐汇区零陵路365号',
# '徐汇区东安路271弄',
# '徐汇区东安路364弄',
# '徐汇区东安路271号',
# '徐汇区零陵路357号']
cc = 0
uniqueLL = []
line_to_remove = []
while cc < len(C):
    addr = C[cc: cc+10]
    resp = urllib.request.urlopen(
           'https://restapi.amap.com/v3/geocode/geo?' +
           'key=   @@      &batch=true&output=json&address=%s&city=%s' % (
           urllib.parse.quote('|'.join(addr)),
           urllib.parse.quote('上海') ) )
    r = resp.read().decode('utf-8')
    cont = json.loads(r)
    if not int(cont['status']):
        print(cont['info']) # if status=0 will show
        raise
    ct = -1
    for c in cont['geocodes']:
        ct += 1
        uniqueLL.append(c['location'] )
        if uniqueLL.count(c['location']) > 1:
            if uniqueLL.count(c['location']) == 2:
                line_to_remove.append(c['location'] )
                # print('!!1', c['location'])
            continue
        d = c['formatted_address'].replace('上海市','').replace('|','')
        if not c['number'] or addr[ct].find(c['number']) == -1:
            if c['formatted_address'].find(addr[ct][:3]) == -1:
                print('!!2', addr[ct][:3], c['formatted_address'] )
                continue
            if addr[ct] != d and not addr[ct].startswith(d
                           ) and not addr[ct].endswith(d[4:]) :
                print(addr[ct], c['formatted_address'] )
        #c['adcode']
        #d = c['location'].split(',')
        #print(gcj02_to_wgs84( float(d[0]), float(d[1]) ))
        csv.append('%s,%s,0,51,%s,gcj02,' % (
                   addr[ct], c['location'], c['level'] ))
    if int(cont['count']) != (ct+1):
        print('!!3', ct, cont['count'])
    e = '\n'.join(allMinus( csv, line_to_remove ))
    # for aaddr in addr:
    #     if e.find(aaddr) == -1:
    #         print('!!4', aaddr)
    if cc and not cc % 200:
        fz = open('/Users/liang/Downloads/%s.txt' % int(time.time()), 'w')
        fz.write(e)
        fz.close
        print('remain:', (len(C) - cc))
        time.sleep(7)
    cc += 10

fz = open('/Users/liang/Downloads/end_%s.txt' % int(time.time()), 'w')
fz.write(e)
fz.close