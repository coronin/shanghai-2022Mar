## EXCEL ##  =countif(B:B,A1)=0

As = ('0318','0319',
      '0320','0321','0322','0323','0324','0325','0326','0327','0328','0329'
      )
Bs = ('0330','0331',
      '0401','0402','0403','0404','0405','0406','0407','0408','0409','0410',
      '0411','0412'
      )

by_district = {'浦东新区':[], '黄浦区':[], '静安区':[], '徐汇区':[], '长宁区':[],
               '普陀区':[], '虹口区':[], '杨浦区':[], '宝山区':[], '闵行区':[],
               '嘉定区':[], '金山区':[], '松江区':[], '青浦区':[], '奉贤区':[], '崇明区':[] }
districts = ('浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区',
             '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区',
             '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区' )
by_address = {'上海发布':['0313'] }

def read_a_list(s):
    f = open('%s.txt' % s, 'r')
    pre = f.readlines()
    f.close()
    post = []
    running_district = ''
    for l in pre:
        line = l.strip().replace('（住宅）', '')
        for dd in districts:
            if line.find(dd) > -1:
                running_district = dd
                #print(s, line)
                break
            pass
        if line in districts:
            continue
        if line.find(running_district) > -1:
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
             ) > -1 or line.find('资料：'
             ) > -1 or line.find('编辑：'
             ) > -1 or line.find('修改'
             ) > -1 or line.find('shanghaifabu'
             ) > -1 or line.find('上海发布'
             ) > -1 or line.find('各区信息'
             ) > -1 or line.find('区新增'
             ) > -1 or line.find('无新增'
             ) > -1 or line.find('2022年'
             ) > -1 or line.find('3月'
             ) > -1 or line.find('4月'
             ) > -1 or line.find('1例为'
             ) > -1 or line.find('感染者'
             ) > -1 or line.find('中发现'
             ) > -1 or line.find('落实终末消毒'
             ) > -1 or line.find('滑动查看' ) > -1:
            continue
        elif line not in post: ## raw address, one day = one list
            post.append(line) # clean address
            if running_district and (line not in by_district[running_district]):
                by_district[running_district].append(line)
            if by_address.get(line):
                by_address[line] += [s]
            else:
                by_address[line] = [s]
    #print(len(post))
    return post

A = []
B = []

for s in As:
    A += read_a_list(s)
    #print(s)
print('in A, estimated', len(list(set(A))) )
#print(list(set(by_district['杨浦区'])))

for s in Bs:
    B += read_a_list(s)
ddc = 0
for dd in districts:
    print(dd, len(by_district[dd]) )
    ddc += len(by_district[dd])
print('by district, estimated total', ddc )
BB = list(set(B))
print('in B, estimated', len(BB) )
# print(list(set(by_district['杨浦区'])))

Z = []
count = 0
#print('sorted by listed dates')
for line in A:
    #if line.find('国权北路1566') > -1 or line.find('淞沪路2005') > -1 or line.find('邯郸路220') > -1 :
    #    print('in A', line)
    if line not in Z and line not in BB: # and line not in notThese:
        count += 1
        #print(line)
        Z.append(line)
print('in A, not in B, estimated', count)
to_check = ['龙吴路2588弄', '国权北路1566弄', '国权北路1450弄', '东安路130号', '邯郸路220号' ]
for ch in to_check:
    if by_address.get(ch):
        print(ch, by_address[ch] )
    else:
        print(ch, 'zero' )

from datetime import datetime
datestr = '%s' % datetime.now()
fz = open('negative.txt', 'w')
fz.write('# %s' %  datestr)
fz.write('\n# 被列入 %s 上海发布的感染者居住地' % ','.join(As) )
fz.write('\n# 但没有出现在之后的上海发布')
fz.write('\n# 因微信页面可被编辑，本列表基于分析时的页面')
fz.write('\n# 疾控，满足7+7和第13天全员核酸阴性，小区解封')
fz.write('\n# 供参考\n')
fz.write( u'\n'.join(Z) )
fz.write( u'\n####\n')
fz.close()

import json
j = {'date':datestr,
     'districts':by_district,
     'address':by_address }
fz = open('full.json', 'w')
fz.write(json.dumps(j, ensure_ascii=False) ) #, sort_keys=True, indent=2
fz.close()