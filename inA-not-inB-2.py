## EXCEL ##  =countif(B:B,A1)=0

f1 = open('A.txt', 'r')
As = ','.join( f1.readlines() ).replace('，',',').replace('。',',').replace('、',',').replace(' ',',').replace('\r',',')
A = [ s.strip() for s in list(filter(None, As.split(',') )) ]
print('in A ~', len(A), ' w/ duplicates')
f1.close()
f2 = open('B.txt', 'r')
Bs = ','.join( f2.readlines() ).replace('，',',').replace('。',',').replace('、',',').replace(' ',',')
B = list(set([ s.strip()
           for s in list(filter(None, Bs.split(',') )) ]))
print('not in B ~', len(B) )
f2.close()
print('total ~', len( list(set(A+B)) ))
#f3 = open('negativeSince0328.txt', 'r')
#notThese = f3.readlines()
#f3.close()

Z = []
count = 0
print('sorted by name')
for line in A:
    if not line or line.find('分别居住于'
         ) > -1 or line.find('居住于：'
         ) > -1 or line.find('通报：'
         ) > -1 or line.find('资料：'
         ) > -1 or line.find('编辑：'
         ) > -1 or line.find('修改'
         ) > -1 or line.find('区新增'
         ) > -1 or line.find('无新增'
         ) > -1 or line.find('2022年'
         ) > -1 or line.find('3月'
         ) > -1 or line.find('4月'
         ) > -1 or line.find('感染者'
         ) > -1 or line.find('落实终末消毒'
         ) > -1 or line.find('滑动查看' ) > -1:
        continue
    if line in ['浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区',
                '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区',
                '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区']:
        #print('## maybe %s' % line)
        continue
    if line.find('崂山四村') > -1 or line.find('国权北路') > -1 :
        print('in A', line)
    if line not in Z and line not in B: # and line not in notThese:
        count += 1
        #print(line)
        Z.append(line)

print(count)

# 2022-04-11 10:31:30.139664
# 被列入 0320-0328 上海发布的感染者居住地
# 但没有出现在 0329 之后的上海发布
# 因微信页面可被编辑，本列表基于分析时的页面
# 之前风控，满足7+7和第13天全员核酸阴性，小区解封
# 供参考
from datetime import datetime
fz = open('negativeSince0329.txt', 'w')
fz.write( '%s\n' % datetime.now() )
fz.write( u'\n'.join(Z) )
fz.write( u'\n####\n')
fz.close()