## EXCEL ##  =countif(B:B,A1)=0

# 2022-6-16: aggregate addresses (daily released need to re-run)
f = open('addr-close2-list1.csv', 'r')
csv = f.readlines()
f.close()
uniqAddr = {}
for l in csv:
    if not l:
        continue
    ll = l.strip().split(',')
    if len(ll) < 2:
        continue
    for lll in ll[1:]:
        if uniqAddr.get(lll):
            raise ValueError(ll[0], lll)
        uniqAddr[lll] = ll[0]
# 707 print( len(uniqAddr) )

AsBs = ('0306','0307','0308','0309','0310',
      '0311','0312','0313','0314','0315','0316','0317','0318','0319','0320',
      '0321','0322','0323','0324','0325','0326','0327','0328','0329','0330','0331',
      '0401','0402','0403','0404','0405','0406','0407','0408','0409','0410',
      '0411','0412','0413','0414','0415','0416','0417','0418','0419','0420',
      '0421','0422','0423','0424','0425','0426','0427','0428','0429','0430',
      '0501','0502','0503','0504','0505','0506','0507','0508','0509','0510',
      '0511','0512','0513','0514','0515','0516','0517','0518','0519','0520',
      '0521','0522','0523','0524','0525','0526','0527','0528','0529','0530','0531',
      '0601','0602','0603','0604','0605','0606','0607','0608','0609','0610',
      '0611','0612','0613','0614','0615','0616','0617','0618','0619','0620',
      '0621','0622','0623',              '0626', # 正好100个
             '0702','0703','0704','0705','0706','0707','0708','0709','0710',
      '0711','0712','0713','0714','0715','0716','0717','0718','0719','0720',
      '0721','0722','0723','0724','0725','0726','0727','0728','0729','0730'  ,
                    '0803',
      '0811','0812','0813','0814','0815','0816','0817','0818','0819','0820',
      '0821','0822',       '0824','0825','0826','0827',              '0830'  ,
      '0901','0902',                            '0907',       '0909','0910',
      '0911',                            '0916',       '0918',
                                                              '0929','0930',
      '1001',              '1004','1005','1006','1007','1008','1009','1010',
      '1011','1012','1013','1014','1015','1016','1017','1018','1019','1020',
      '1021','1022','1023','1024','1025','1026','1027','1028','1029','1030'  ,
             '1102','1103',       '1105',       '1107','1108','1109','1110',
                    '1113','1114'
      )
#### 以上不能有末尾逗号 没有空字符检查
As = AsBs[:-9]
Bs = AsBs[-9:]
#### 以上14会因为没有阳性感染者而变小
if len(Bs) > 14:
    raise ValueError('not in B 最多14天')

districts = ('浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区',
             '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区',
             '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区' )
by_district = {'浦东新区':[], '黄浦区':[], '静安区':[], '徐汇区':[], '长宁区':[],
               '普陀区':[], '虹口区':[], '杨浦区':[], '宝山区':[], '闵行区':[],
               '嘉定区':[], '金山区':[], '松江区':[], '青浦区':[], '奉贤区':[], '崇明区':[] }
districts_released = {}
districts_today = {}
districts_inB = {}
by_address = {'shanghaifabu':['0313'] }
if len(As) < 2:
    raise ValueError('in A 数据量少，0306需为字符', As)
    #As = '0306' # if ,'0320')
    #As = []     # < 0320
transition_int = int(Bs[0])
if (As):
    transition_int = int(As[0]) # 306


import re
def clean_dates(arr):
    ds = re.sub(r'\d', '', ','.join(arr) )
    dsi = 16
    for dd in ds.split(','):
        if not dd:
            continue
        ind = districts.index(dd)
        if ind < dsi:
            dsi = ind
    if not dsi in range(0, 16): # 16 not in range
        raise ValueError(dsi, ds, arr)
    arr_new = []
    for aa in arr:
        arr_new.append(aa.replace(districts[dsi], ''))
    return arr_new


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


def uniq_a(lll):
    if uniqAddr.get(lll):
        return uniqAddr[lll]
    return lll

def read_a_list(s, tag=''):
    if not s:
        return []
    global transition_int;
    if tag != 'list' and int(s) != transition_int:
        raise ValueError('%s.txt' % s, transition_int)
    transition_int += 1
    if tag != 'list' and transition_int == 332:
        transition_int = 401
    elif tag != 'list' and transition_int == 431:
        transition_int = 501
    elif tag != 'list' and transition_int == 532:
        transition_int = 601
    elif tag != 'list' and transition_int in (624, 625):
        transition_int = 626
    elif tag != 'list' and transition_int in (627, 628, 629, 630, 701): # 631
        transition_int = 702
    elif tag != 'list' and transition_int in (731, 801, 802): # 732
        transition_int = 803
    elif tag != 'list' and transition_int in (804, 805, 806, 807, 808, 809, 810):
        transition_int = 811
    elif tag != 'list' and transition_int == 823:
        transition_int = 824
    elif tag != 'list' and transition_int in (828, 829):
        transition_int = 830
    elif tag != 'list' and transition_int == 831: # 832
        transition_int = 901
    elif tag != 'list' and transition_int in (903, 904, 905, 906):
        transition_int = 907
    elif tag != 'list' and transition_int == 908:
        transition_int = 909
    elif tag != 'list' and transition_int in (912, 913, 914, 915):
        transition_int = 916
    elif tag != 'list' and transition_int == 917:
        transition_int = 918
    elif tag != 'list' and transition_int in (919, 920, 921, 922, 923, 924, 925, 926, 927, 928):
        transition_int = 929
    elif tag != 'list' and transition_int == 931:
        transition_int = 1001
    elif tag != 'list' and transition_int in (1002, 1003):
        transition_int = 1004
    elif tag != 'list' and transition_int in (1031, 1101):
        transition_int = 1102
    elif tag != 'list' and transition_int == 1104:
        transition_int = 1105
    elif tag != 'list' and transition_int == 1106:
        transition_int = 1107
    elif tag != 'list' and transition_int in (1111, 1112):
        transition_int = 1113
    #### @@
    if len(s) != 4:
        f = open('%s.txt' % s, 'r')
    else:
        f = open('shanghaifabu/%s.txt' % s, 'r')
    pre = f.readlines()
    f.close()
    post = []
    running_district = ''
    s_dt = '（%s月%s日' % (int(s[:2]), int(s[2:]))
    for l in pre:
        line = l.strip().replace('（住宅）', ''
                       ).replace('（公寓）', '') ## 店铺）宿舍）
        if line.find(s_dt) > 0:
            line = line.split(s_dt)[0]
        if line == 'shanghaifabu' and tag != 'list':
            by_address[line] += [s]
            continue
        for dd in districts:
            if line.find(dd) > -1:
                running_district = dd
                #print('>>>>', s, line)
                break
            pass
        if line in districts:
            continue
        if line.find(running_district) > -1:
            continue
        if running_district and (line.find('资料') > -1 or
                                 line.find('卫健委') > -1 or
                                 line.find('新闻办编辑') > -1):
            running_district = ''
            continue
        if len( line.strip() ) > 26:
            print('>> %s.txt' % s, 26, line)
        if line.find('已通报') > 0:
            raise ValueError('%s.txt' % s, line, line )
        if not line or line == '新增' or line.find('区新增'
             ) > -1 or line.find('无新增'
             ) > -1 or line.find('微信号'
             ) > -1 or line.find('微信平台'
             ) > -1 or line.find('功能介绍'
             ) > -1 or line.find('梦幻的城市'
             ) > -1 or line.find('共同成长'
             ) > -1 or line.find('上海的资讯'
             ) > -1 or line.find('上海的理由'
             ) > -1 or line.find('收录于'
             ) > -1 or line.find('按照统一'
             ) > -1 or line.find('修改'
             ) > -1 or line.find('上海发布'
             ) > -1 or line.find('各区信息'
             ) > -1 or line.find('居住于'
             ) > -1 or line.find('居住地址'
             ) > -1 or line.find('2022年'
             ) > -1 or line.find('3月'
             ) > -1 or line.find('4月'
             ) > -1 or line.find('5月'
             ) > -1 or line.find('6月'
             ) > -1 or line.find('7月'
             ) > -1 or line.find('8月'
             ) > -1 or line.find('9月'
             ) > -1 or line.find('10月'
             ) > -1 or line.find('上述人员'
             ) > -1 or line.find('外省市返沪'
             ) > -1 or line.find('外省来沪'
             ) > -1 or line.find('外省返'
             ) > -1 or line.find('系外省'
             ) > -1 or line.find('抵沪'
             ) > -1 or line.find('落地检'
             ) > -1 or line.find('暂住于'
             ) > -1 or line.find('自我健康监测'
             ) > -1 or line.find('1例'
             ) > -1 or line.find('病例'
             ) > -1 or line.find('感染者'
             ) > -1 or line.find('中发现' # 隔离管控 风险人群筛查
             ) > -1 or line.find('落实管控'
             ) > -1 or line.find('采取封控'
             ) > -1 or line.find('落实消毒'
             ) > -1 or line.find('落实终末消毒'
             ) > -1 or line.find('滑动查看'
             ) > -1 or line.find('当前高中风险'
             ) > -1 or line.find('当前中高风险'
             ) > -1 or line.find('当前中风险'
             ) > -1 or line.find('当前高风险'
             ) > -1 or line.find('关注我们'
             ) > -1 or line.find('转载请注明'
             ) > -1 or line.find('互动你我'
             ) > -1 or line.find('官方资讯'
             ) > -1 or line.find('一起成长'
             ) > -1 or line.find('守护安全'
             ) > -1 or line.find('公众号'
             ) > -1 or line.find('陪伴我们'
             ) > -1 or line.find('关注和参与'
             ) > -1 or line.find('政府微信'
             ) > -1 or line.find('官方微信'
             ) > -1 or line.find('第一时间'
             ) > -1 or line.find('及时发布'
             ) > -1 or line.find('欢迎关注'
             ) > -1 or line.find('信息发布'
             ) > -1 or line.find('大小事' ) > -1:
            continue
        if not running_district:
            raise ValueError('%s.txt' % s, line, len(post) )
        # 2022-6-16
        line1 = uniq_a( '%s%s' % (running_district, line) )[len(running_district):]
        if tag == 'list':
            post.append( '%s%s' % (running_district, line1) )
            continue
        elif '%s%s' % (running_district, line1) not in post:
            if re.match(r'\d+\D\D?$', line1) and line1 not in ('195街坊'):
                raise ValueError('%s.txt' % s, line1, len(post) )
            post.append( '%s%s' % (running_district, line1) )
            if line1 not in by_district[running_district]:
                by_district[running_district].append(line1)
            if tag == 'today':
                print(Bs[-1], running_district, line1)
                # 2022-6-1
                if districts_today.get(running_district):
                    districts_today[running_district] += [line1]
                else:
                    districts_today[running_district] = [line1]
            if tag in ('inB', 'today'):
                if districts_inB.get(running_district):
                    if line not in districts_inB[running_district]:
                        districts_inB[running_district] += [line1]
                else:
                    districts_inB[running_district] = [line1]
            if by_address.get(line1):
                by_address[line1] += ['%s%s' % (s, running_district) ]
            else:
                by_address[line1] = [ '%s%s' % (s, running_district)]
        else:
            raise ValueError('%s.txt' % s, line, line1, len(post) )
    return post


# transition_int = 5090509
# print('\n'.join(read_a_list('05090509') ))
# raise RuntimeError

A = []
if As == '0306':
    A = read_a_list(As)
elif As:
    for s in As:
        A += read_a_list(s)
        #print('>>>>', s, len(A) )
#print('A', list(set(by_district['杨浦区'])))
B = []
for s in Bs[:-1]:
    B += read_a_list(s, tag='inB')
B += read_a_list(Bs[-1], tag='today')
BB = list(set(B))
print('====================')
print('in A, estimated', len(list(set(A))) )
print('in B, estimated', len(BB) )
# print('B', list(set(by_district['杨浦区'])))
ddc = 0
for dd in districts:
    #print('>>>>', dd, len(by_district[dd]) )
    ddc += len(by_district[dd])
print('by district total, w/dupl', ddc )
# for zz in list(set(A + BB)):
#     # if len(zz) > 13: # 浦东新区世纪大道1239号
#     #     print(zz)
#     if re.search(r'\d+\D\D+\d+', zz):
#         print(zz)
#     # if re.match(r'\d+\D\D+村', zz):
#     #     print(zz)
# raise RuntimeError

from datetime import datetime
datestr = '%s' % datetime.now()
import json
####
# 以下注释，以更新 map-location.json

Z = []
count = 0
#print('sorted by listed dates')
for longline in A:
    #if line.find('国权北路1566') > -1 or line.find('淞沪路2005') > -1 or line.find('邯郸路220') > -1 :
    #    print('in A', line)
    if longline not in Z and longline not in BB: # and line not in notThese:
        count += 1
        Z.append(longline)
        # if longline.startswith('浦东新区'):
        #     line = longline[4:]
        # else:
        #     line = longline[3:]
        # for dd in districts:
        #     if line in by_district[dd]:
        #         if (districts_released.get(dd)):
        #             districts_released[dd] += [line]
        #         else:
        #             districts_released[dd] = [line]
        #         break
        #     pass
print('in A, not in B, estimated', count)


latest_released = {}
# listed30days = []
count = 0
for line, dates in by_address.items():
    # if len(dates) >= 30: # 地址同名 日期连着区
    #     listed30days.append(line)
    ddd = -1
    while As and len(dates) >= (0 - ddd) and dates[ddd][:4] == As[-1]:
        count += 1
        dd = dates[ddd][4:]
        if line in by_district[dd]:
            if (latest_released.get(dd)):
                latest_released[dd] += [line]
            else:
                latest_released[dd] = [line]
        else:
            raise ValueError('>>', line, dates)
        ddd -= 1
    if line != 'shanghaifabu':
        by_address[line] = clean_dates(dates)
if count:
    print('')
print('released %s, estimated' % Bs[-1], count)
if A:
    for dd in districts:
        if latest_released.get(dd):
            print('%s\t%s' % (dd, len(latest_released[dd]) ))
        else:
            print('%s\t0' % dd)

# listed_30days = list(set(listed30days))
# print('\nlisted 30 days', len(listed_30days) )
# if len(AsBs) < 39: # 0412
#     print('should be zero, before 0412')

# latest_added = {}
# Bs2 = read_a_list(Bs[-2], tag='list')
# for dd in districts:
#     if not districts_today.get(dd):
#         continue
#     #print('>>>>', dd, len(districts_today[dd]) )
#     for line in districts_today[dd]:
#         if ('%s%s' % (dd, line)) not in Bs2:
#             #print('>>>>', dd, line)
#             if (latest_added.get(dd)):
#                 latest_added[dd] += [line]
#             else:
#                 latest_added[dd] = [line]

# latest_added2 = {}
# latest_added7 = {}
# Bs4 = [[], [], [], [], [], [] ] # >= 0501
# try:
#     Bs4[0] = read_a_list(Bs[-3], tag='list')
#     Bs4[1] = read_a_list(Bs[-4], tag='list')
#     for dd in districts:
#         if not districts_today.get(dd):
#             continue
#         #print('>>>>', dd, len(districts_today[dd]) )
#         for line in districts_today[dd]:
#             if ('%s%s' % (dd, line)) not in Bs2 and (
#                 '%s%s' % (dd, line)) not in Bs4[0] and (
#                 '%s%s' % (dd, line)) not in Bs4[1]:
#                 #print('>>>>', dd, line)
#                 if (latest_added2.get(dd)):
#                     latest_added2[dd] += [line]
#                 else:
#                     latest_added2[dd] = [line]
#     try:
#         Bs4[2] = read_a_list(Bs[-5], tag='list')
#         Bs4[3] = read_a_list(Bs[-6], tag='list')
#         Bs4[4] = read_a_list(Bs[-7], tag='list')
#         Bs4[5] = read_a_list(Bs[-8], tag='list')
#         for dd in districts:
#             if not districts_today.get(dd):
#                 continue
#             #print('>>>>', dd, len(districts_today[dd]) )
#             for line in districts_today[dd]:
#                 last38 = False
#                 for Bs4_ in Bs4:
#                     if ('%s%s' % (dd, line)) in Bs4_:
#                         last38 = True;
#                         break;
#                 if last38:
#                     continue
#                 if ('%s%s' % (dd, line)) not in Bs2:
#                     #print('>>>>', dd, line)
#                     if (latest_added7.get(dd)):
#                         latest_added7[dd] += [line]
#                     else:
#                         latest_added7[dd] = [line]
#     except:
#         print('>> empty .latest_added7')
# except:
#     print('>> empty .latest_added2')


print('\n')
to_check = ('东川路800号', '海波路850弄', '龙吴路2588弄', '凤城三村',
            '国权北路1566弄', '国权北路1450弄', '东安路130号', '邯郸路220号', '武东路57号' )
for ch in to_check:
    if by_address.get(ch) and int(by_address[ch][-1]) > 600:
        print(ch, '\tlast', by_address[ch][-1], '\ttotal', len(by_address[ch]) )
        if by_address[ch][-1][:4] == Bs[-1]:
            print('    ^^\n')
    #else:
    #    print(ch, 'zero' )


fz = open('negative.txt', 'w')
fz.write('# %s %s' % (Bs[-1], datestr))
fz.write('\n# 被列入 %s 上海发布的感染者居住地' % ','.join(As) )
fz.write('\n# 但没有出现在之后的上海发布')
fz.write('\n# 因微信页面可被编辑，本列表基于分析时的页面')
fz.write('\n# 疾控，满足7+7和第13天全员核酸阴性，小区解封')
fz.write('\n# 供参考\n')
fz.write('\n'.join(Z) )
fz.write('\n##')
fz.close()

j = {'date':datestr,
     'tag':Bs[-1],
     'address':by_address,
     # 'today':districts_today,          # map of by_district
     # 'inB':districts_inB,              # map of by_district
     'districts':by_district }
     # 'released':districts_released,    # map of by_district
     # 'released_today':latest_released, # map of by_district
     # 'latest_added2':latest_added2,    # map of by_district
     # 'latest_added7':latest_added7,    # map of by_district
     # 'latest_added':latest_added       # map of by_district
# if listed_30days:
#     j['listed_30days'] = listed_30days # map of by_district
fz = open('shanghaifabu/full%s.json' % Bs[-1], 'w')
fz.write("data='%s'" % json.dumps(j, ensure_ascii=False) ) #, sort_keys=True, indent=2
#  jsonp  '%s(%s)' % (callback, out)
fz.close()
print('\nupdate drag-me.html and sh2.html with full.json?v=%s' % Bs[-1] )
if not A:
    print('no A, today', len(districts_today) )
    print('no A, inB', len(districts_inB) )
    # print('no A, released', len(districts_released) )
    print('no A, latest released', len(latest_released) )
    # print('no A, latest added', len(latest_added) )

# 以上注释，以更新 map-location.json
####
f = open('map-location.csv', 'r')
csv = f.readlines()
f.close()
C = []
CC = {}
hot_addr = 0
for l in csv[1:]:
    if not l:
        continue
    ls = l.split(',')
    if len(ls) > 3 and ls[1] and ls[2]:
        ls0s = ls[0].strip()
        if ls0s.startswith('浦东新区'):
            line = ls0s[4:]
        else:
            line = ls0s[3:]
        if ls0s in [
#### @@ 复制进 drag-me.html 并获取定位，再缩短 进csv和sh2.html，然后查log导入此处
'杨浦区政衷路36弄',
'静安区西藏北路507号',
'松江区东方佘山索菲特大酒店',
'普陀区紫荆苑',
'宝山区锦秋花园',
'浦东新区海潮村',
'浦东新区金石村'
        ] and ls0s not in C:
            hot_addr += 1
            print('手动+中高风险', hot_addr, ls0s)
        elif len(by_address) > 1 and not by_address.get(line): # 只收录有上榜记录的地址
            continue
        #if len(by_address) > 1 and uniqAddr.get(ls0s):
        #    print('map-location could be unique', ls0s, uniqAddr[ls0s])
        # map-location could be unique 浦东新区光明村 浦东新区曹路镇光明村
        # map-location could be unique 浦东新区红星村 浦东新区祝桥镇红星村
        # map-location could be unique 浦东新区营房村 浦东新区康桥镇营房村
        # map-location could be unique 浦东新区中新村 浦东新区高桥镇中新村
        # map-location could be unique 浦东新区金星村 浦东新区祝桥镇金星村
        # map-location could be unique 嘉定区桃园新村 嘉定区嘉定镇街道桃园新村
        # map-location could be unique 浦东新区汇南村 浦东新区惠南镇汇南村
        # map-location could be unique 浦东新区秀龙村 浦东新区康桥镇秀龙村
        # map-location could be unique 嘉定区大陆村 嘉定区外冈镇大陆村
        # map-location could be unique 浦东新区梅园村 浦东新区航头镇梅园村
        # map-location could be unique 浦东新区灯塔村 浦东新区高东镇灯塔村
        # map-location could be unique 浦东新区勤丰村 浦东新区惠南镇勤丰村
        # map-location could be unique 嘉定区联西村 嘉定区安亭镇联西村
        # map-location could be unique 浦东新区新苗村 浦东新区康桥镇新苗村
        # map-location could be unique 浦东新区高桥镇中新村 浦东新区高桥镇北新村中新村
        # map-location could be unique 浦东新区富强村 浦东新区惠南镇富强村
        # map-location could be unique 嘉定区五四村 嘉定区江桥镇五四村
        # map-location could be unique 浦东新区城南村 浦东新区川沙新镇城南村
        # map-location could be unique 浦东新区前进村唐家新村 浦东新区唐镇前进村唐家新村
        # map-location could be unique 浦东新区立新村 浦东新区祝桥镇立新村
        # map-location could be unique 浦东新区幸福村 浦东新区惠南镇幸福村
        # map-location could be unique 浦东新区光辉村 浦东新区宣桥镇光辉村
        # map-location could be unique 嘉定区新丰村 嘉定区南翔镇新丰村
        # map-location could be unique 浦东新区牌楼村 浦东新区航头镇牌楼村
        # map-location could be unique 浦东新区罗家村 浦东新区曹路镇罗家村
        # map-location could be unique 松江区中心村 松江区石湖荡镇中心村
        # map-location could be unique 浦东新区先进村 浦东新区祝桥镇先进村
        # map-location could be unique 浦东新区跃进新村 浦东新区合庆镇跃进新村
        # map-location could be unique 浦东新区友谊村 浦东新区惠南镇友谊村
        # map-location could be unique 浦东新区星火村 浦东新区祝桥镇星火村
        # map-location could be unique 嘉定区星光村 嘉定区安亭镇星光村
        # map-location could be unique 浦东新区永乐村 浦东新区惠南镇永乐村
        # map-location could be unique 浦东新区高桥村 浦东新区泥城镇高桥村
        # map-location could be unique 嘉定区灯塔村 嘉定区嘉定工业区灯塔村
        # map-location could be unique 嘉定区黎明村 嘉定区嘉定工业区黎明村
        # map-location could be unique 嘉定区永丰村 嘉定区南翔镇永丰村
        # map-location could be unique 奉贤区横桥村 奉贤区四团镇横桥村
        # map-location could be unique 浦东新区高桥村 浦东新区泥城镇高桥村
        # map-location could be unique 浦东新区光明村 浦东新区曹路镇光明村
        elif len(by_address) == 1 and uniqAddr.get(ls0s): # 只去掉了可被简化的短地址
            continue
        if ls0s not in C:
            C.append( ls0s )
        # 1经度 2纬度
        # 3 是否精确
        # 4 可信度
        # 6 bd09_to_wgs84 gcj02_to_wgs84
        if len(ls) > 7 and ls[6] == 'bd09':
            CC[ ls0s ] = bd09_to_wgs84(float(ls[1]), float(ls[2])
                                               ) + [ ls[3] ]
        elif len(ls) > 7 and ls[6] == 'gcj02':
            CC[ ls0s ] = gcj02_to_wgs84(float(ls[1]), float(ls[2])
                                                ) + [ ls[3] ]
        else:
            CC[ ls0s ] = [ ls[1], ls[2], ls[3] ]

fz = open('inAB-not-map.txt', 'w')
fz.write('# AB %s' % datestr)
fz.write('\n# https://maplocation.sjfkai.com/')
AB = list(set(BB + A))
for longline in AB:
    if longline not in C:
        fz.write('\n%s' % longline)
fz.write('\n##')
fz.close

j = {'date':datestr,
     'tag':'AB',
     'locations':CC }
fz = open('shanghaifabu/map-location.json', 'w')
fz.write("csv='%s'" % json.dumps(j, ensure_ascii=False) )
#  jsonp  '%s(%s)' % (callback, out)
fz.close()
print('\ncheck inAB-not-map.txt, update map-location.csv and do ##')
print('refresh CDN, especially https://cdn.teach.bio/map-location.json ##\n')
