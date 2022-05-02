## EXCEL ##  =countif(B:B,A1)=0

As = ('0318','0319','0320',
      '0321','0322','0323','0324','0325','0326','0327','0328','0329','0330',
      '0331',
      '0401','0402','0403','0404','0405','0406','0407','0408','0409','0410',
      '0411','0412','0413','0414','0415','0416','0417'
      )
Bs = ('0418','0419','0420',
      '0421','0422','0423','0424','0425','0426','0427','0428','0429','0430',
      '0501'
      )

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


def read_a_list(s, tag=''):
    f = open('%s.txt' % s, 'r')
    pre = f.readlines()
    f.close()
    post = []
    running_district = ''
    for l in pre:
        line = l.strip().replace('（住宅）', ''
                       ).replace('（公寓）', '')
        if line == 'shanghaifabu':
            #print('>>>>', s, line)
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
             ) > -1 or line.find('落实终末消毒'
             ) > -1 or line.find('滑动查看' ) > -1:
            continue
        elif running_district and tag == 'list':
            post.append( '%s%s' % (running_district, line) )
            continue
        elif running_district and '%s%s' % (running_district, line) not in post:
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
                if s not in by_address[line]:
                    by_address[line] += [s]
                else:
                    # 不同区 地址同名, 团结村 国权北路555
                    by_address[line] += ['%s%s' % (s, running_district) ]
            else:
                by_address[line] = [s]
        else:
            print('>>', s, line, len(post) )
    return post


print('====================')

A = []
for s in As:
    A += read_a_list(s)
    #print('>>>>', s)
print('in A, estimated', len(list(set(A))) )
#print('A', list(set(by_district['杨浦区'])))

B = []
for s in Bs[:-1]:
    B += read_a_list(s, tag='inB')
B += read_a_list(Bs[-1], tag='today')
BB = list(set(B))
print('in B, estimated', len(BB) )
# print('B', list(set(by_district['杨浦区'])))
ddc = 0
for dd in districts:
    #print('>>>>', dd, len(by_district[dd]) )
    ddc += len(by_district[dd])
print('by district total, w/dupl', ddc )


Z = []
count = 0
#print('sorted by listed dates')
for longline in A:
    #if line.find('国权北路1566') > -1 or line.find('淞沪路2005') > -1 or line.find('邯郸路220') > -1 :
    #    print('in A', line)
    if longline not in Z and longline not in BB: # and line not in notThese:
        count += 1
        Z.append(longline)
        if longline.startswith('浦东新区'):
            line = longline[4:]
        else:
            line = longline[3:]
        #print('>>>>', line)
        for dd in districts:
            if line in by_district[dd]:
                if (districts_released.get(dd)):
                    districts_released[dd] += [line]
                else:
                    districts_released[dd] = [line]
                break
            pass
print('in A, not in B, estimated', count, '\n')


to_check = ('海波路850弄', '龙吴路2588弄',
            '国权北路1566弄', '国权北路1450弄', '东安路130号', '邯郸路220号' )
for ch in to_check:
    if by_address.get(ch):
        print(ch, by_address[ch] )
    else:
        print(ch, 'zero' )


latest_released = {}
count = 0
for line, dates in by_address.items():
    if dates[-1] == As[-1]:
        count += 1
        #print('>>>>', line)
        for dd in districts:
            if line in by_district[dd]:
                if (latest_released.get(dd)):
                    latest_released[dd] += [line]
                else:
                    latest_released[dd] = [line]
                break # 地址同名, 团结村 国权北路555
            pass

print('\nreleased %s, estimated' % Bs[-1], count)
for dd in districts:
    if latest_released.get(dd):
        print('%s\t%s' % (dd, len(latest_released[dd]) ))
    else:
        print(dd, 0)


latest_added = {}
Bs2 = read_a_list(Bs[-2], tag='list')
for dd in districts:
    if not districts_today.get(dd):
        continue
    #print('>>>>', dd, len(districts_today[dd]) )
    for line in districts_today[dd]:
        if ('%s%s' % (dd, line)) not in Bs2:
            #print('>>>>', dd, line)
            if (latest_added.get(dd)):
                latest_added[dd] += [line]
            else:
                latest_added[dd] = [line]


from datetime import datetime
datestr = '%s' % datetime.now()
fz = open('negative.txt', 'w')
fz.write('# %s' %  datestr)
fz.write('\n# 被列入 %s 上海发布的感染者居住地' % ','.join(As) )
fz.write('\n# 但没有出现在之后的上海发布')
fz.write('\n# 因微信页面可被编辑，本列表基于分析时的页面')
fz.write('\n# 疾控，满足7+7和第13天全员核酸阴性，小区解封')
fz.write('\n# 供参考\n')
fz.write('\n'.join(Z) )
fz.write('\n####\n')
fz.close()

f = open('map-location.csv', 'r')
csv = f.readlines()
f.close()
C = []
CC = {}
for l in csv:
    if not l:
        continue
    ls = l.split(',')
    if len(ls) > 3 and ls[0] not in C:
        C.append( ls[0].strip() )
        CC[ ls[0].strip() ] = [ ls[1], ls[2], ls[3] ]
        # 1经度 2纬度
        # 3 是否精确
        # 4 可信度
fz = open('inB-not-map.txt', 'w')
fz.write('# %s' %  datestr)
for longline in BB:
    if longline not in C:
        fz.write('\n%s' % longline)
fz.close

import json
j = {'date':datestr,
     'locations':CC }
fz = open('map-location.json', 'w')
fz.write("csv='%s'" % json.dumps(j, ensure_ascii=False) )
fz.close()

# j = {'date':datestr,
#      'address':by_address,
#      'today':districts_today,
#      'inB':districts_inB,
#      'districts':by_district,
#      'released':districts_released,
#      'released_today':latest_released,
#      'latest_added':latest_added }
# fz = open('full.json', 'w')
# fz.write("data='%s'" % json.dumps(j, ensure_ascii=False) ) #, sort_keys=True, indent=2
# fz.close()
# print('\n\nupdate drag-me.html and sh2.html with full.json?v=%s\n\n' % Bs[-1] )