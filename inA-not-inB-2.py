## EXCEL ##  =countif(B:B,A1)=0

As = ('0318','0319',
      '0320','0321','0322','0323','0324','0325','0326','0327','0328','0329'
      )
Bs = ('0330','0331',
      '0401','0402','0403','0404','0405','0406','0407','0408','0409','0410',
      '0411'#,'0412'
      )

by_district = {'浦东新区':[], '黄浦区':[], '静安区':[], '徐汇区':[], '长宁区':[],
               '普陀区':[], '虹口区':[], '杨浦区':[], '宝山区':[], '闵行区':[],
               '嘉定区':[], '金山区':[], '松江区':[], '青浦区':[], '奉贤区':[], '崇明区':[] }
def read_a_list(s):
    f = open('%s.txt' % s, 'r')
    pre = f.readlines()
    f.close()
    post = []
    running_district = ''
    for l in pre:
        line = l.strip().replace('（住宅）')
        if not line or line.find('分别居住于'
             ) > -1 or line.find('居住于：'
             ) > -1 or line.find('通报：'
             ) > -1 or line.find('资料：'
             ) > -1 or line.find('编辑：'
             ) > -1 or line.find('修改'
             ) > -1 or line.find('上海发布'
             ) > -1 or line.find('各区信息'
             ) > -1 or line.find('区新增'
             ) > -1 or line.find('无新增'
             ) > -1 or line.find('2022年'
             ) > -1 or line.find('3月'
             ) > -1 or line.find('4月'
             ) > -1 or line.find('感染者'
             ) > -1 or line.find('中发现'
             ) > -1 or line.find('落实终末消毒'
             ) > -1 or line.find('滑动查看' ) > -1:
            continue
        if line in list(by_district.keys()):
            running_district = line
            if line == '金山区':
                print(s, line)
            continue
        if l not in post:
            post.append(line)
            if running_district:
                by_district[running_district].append(line)
    #print(len(post))
    return post

A = []
B = []

for s in As:
    A += read_a_list(s)
    #print(s)
print('A~', len(list(set(A))) )
#print(list(set(by_district['杨浦区'])))

for s in Bs:
    B += read_a_list(s)
BB = list(set(B))
print('B~', len(BB) )
# print(list(set(by_district['杨浦区'])))

Z = []
count = 0
print('sorted by name')
for line in A:
    if line.find('国权北路1566') > -1 or line.find('淞沪路2005') > -1 or line.find('淞塘路98') > -1 or line.find('武川路') > -1 :
        print('in A', line)
    if line not in Z and line not in B: # and line not in notThese:
        count += 1
        #print(line)
        Z.append(line)
print(count)

# from datetime import datetime
# fz = open('negative.txt', 'w')
# fz.write('# %s' % datetime.now() )
# fz.write('\n# 被列入 %s 上海发布的感染者居住地' % ','.join(As) )
# fz.write('\n# 但没有出现在之后的上海发布')
# fz.write('\n# 因微信页面可被编辑，本列表基于分析时的页面')
# fz.write('\n# 疾控，满足7+7和第13天全员核酸阴性，小区解封')
# fz.write('\n# 供参考\n')
# fz.write( u'\n'.join(Z) )
# fz.write( u'\n####\n')
#fz.close()

