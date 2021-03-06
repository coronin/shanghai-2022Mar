## EXCEL ##  =countif(B:B,A1)=0

transition_int = 0
AsBs_ = ['0306','0307','0308','0309','0310',
      '0311','0312','0313','0314','0315','0316','0317','0318','0319','0320',
      '0321','0322','0323','0324','0325','0326','0327','0328','0329','0330',
      '0331',
      '0401','0402','0403','0404','0405','0406','0407','0408','0409','0410',
      '0411','0412','0413','0414','0415','0416','0417','0418','0419','0420',
      '0421','0422','0423','0424','0425','0426','0427','0428','0429','0430',
      '0501','0502','0503','0504','0505','0506','0507','0508','0509','0510',
      '0511','0512','0513','0514','0515','0516','0517','0518','0519','0520']
# raise
#### used on 2022-5-22 fix missing address
# 0315
# +松江区
# +车峰路199弄
# +浦东新区
# +张杨路1515弄
# 0309
# +奉贤区
# +百团路198弄
# +闵行区
# +梅富路366号

def big_boss():
    #### 以上不能有末尾逗号 没有空字符检查
    As = AsBs[:-14]
    Bs = AsBs[-14:]
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
    global transition_int
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


    def read_a_list(s, tag=''):
        if not s:
            return []
        global transition_int;
        if tag != 'list' and int(s) != transition_int:
            raise ValueError(s, transition_int)
        transition_int += 1
        if tag != 'list' and transition_int == 332:
            transition_int = 401
        elif tag != 'list' and transition_int == 431:
            transition_int = 501
        elif tag != 'list' and transition_int == 532:
            transition_int = 601
        if len(s) != 4:
            f = open('%s.txt' % s, 'r')
        else:
            f = open('shanghaifabu/%s.txt' % s, 'r')
        pre = f.readlines()
        f.close()
        post = []
        running_district = ''
        for l in pre:
            line = l.strip().replace('（住宅）', ''
                           ).replace('（公寓）', '') ## 店铺）宿舍）
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
            if len( line.strip() ) > 20:
                print('>> %s.txt' % s, line, 20)
            if not line or line.find('居住于'
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
                 ) > -1 or line.find('区新增'
                 ) > -1 or line.find('无新增'
                 ) > -1 or line.find('2022年'
                 ) > -1 or line.find('3月'
                 ) > -1 or line.find('4月'
                 ) > -1 or line.find('5月'
                 ) > -1 or line.find('1例为'
                 ) > -1 or line.find('病例'
                 ) > -1 or line.find('感染者'
                 ) > -1 or line.find('中发现'
                 ) > -1 or line.find('落实管控'
                 ) > -1 or line.find('采取封控'
                 ) > -1 or line.find('落实消毒'
                 ) > -1 or line.find('落实终末消毒'
                 ) > -1 or line.find('滑动查看'
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
            elif running_district and tag == 'list':
                post.append( '%s%s' % (running_district, line) )
                continue
            elif running_district and '%s%s' % (running_district, line) not in post:
                if re.match(r'\d+\D\D?$', line):
                    raise ValueError(s, line, len(post))
                post.append( '%s%s' % (running_district, line) )
                if line not in by_district[running_district]:
                    by_district[running_district].append(line)
                if tag == 'today':
                    if districts_today.get(running_district):
                        districts_today[running_district] += [line]
                    else:
                        districts_today[running_district] = [line]
                if tag in ('inB', 'today'):
                    if districts_inB.get(running_district):
                        if line not in districts_inB[running_district]:
                            districts_inB[running_district] += [line]
                    else:
                        districts_inB[running_district] = [line]
                if by_address.get(line):
                    by_address[line] += ['%s%s' % (s, running_district) ]
                else:
                    by_address[line] = [ '%s%s' % (s, running_district)]
            else:
                print('>> %s.txt' % s, line, len(post) )
        return post


    # transition_int = 5090509
    # print('\n'.join(read_a_list('05090509') ))
    # raise RuntimeError
    print('====================')

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
    print('in A, estimated', len(list(set(A))) )
    print('in B, estimated', len(BB) )
    # print('B', list(set(by_district['杨浦区'])))
    ddc = 0
    for dd in districts:
        #print('>>>>', dd, len(by_district[dd]) )
        ddc += len(by_district[dd])
    print('by district total, w/dupl', ddc )
    # import re
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
    print('in A, not in B, estimated', count, '\n')


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
    # to_check = ('东川路800号', '海波路850弄', '龙吴路2588弄', '凤城三村',
    #             '国权北路1566弄', '国权北路1450弄', '东安路130号', '邯郸路220号' )
    # for ch in to_check:
    #     if by_address.get(ch):
    #         print(ch, by_address[ch] )
    #         if by_address[ch][-1][:4] == Bs[-1]:
    #             print('    ^^\n')
    #     else:
    #         print(ch, 'zero' )


    # fz = open('negative.txt', 'w')
    # fz.write('# %s %s' % (Bs[-1], datestr))
    # fz.write('\n# 被列入 %s 上海发布的感染者居住地' % ','.join(As) )
    # fz.write('\n# 但没有出现在之后的上海发布')
    # fz.write('\n# 因微信页面可被编辑，本列表基于分析时的页面')
    # fz.write('\n# 疾控，满足7+7和第13天全员核酸阴性，小区解封')
    # fz.write('\n# 供参考\n')
    # fz.write('\n'.join(Z) )
    # fz.write('\n####')
    # fz.close()

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
    # print('\nupdate drag-me.html and sh2.html with full.json?v=%s' % Bs[-1] )
    if not A:
        print('no A, today', len(districts_today) )
        print('no A, inB', len(districts_inB) )
        # print('no A, released', len(districts_released) )
        print('no A, latest released', len(latest_released) )
        # print('no A, latest added', len(latest_added) )

    # 以上注释，以更新 map-location.json
    ####


AsBs = AsBs_
while len(AsBs) > 16:
    big_boss()
    print('%s done!\n' % AsBs.pop() )
print(AsBs)