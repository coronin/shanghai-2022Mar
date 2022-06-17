# from bs4 import BeautifulSoup
# from urllib import request
# import json
# import re
import os
# os.system('scrapy fetch --nolog https://www.cell.com/cell/newarticles > cell.txt')

# # 2022-6-16: aggregate addresses (daily released need to re-run)
# f = open('addr-close2-list1.csv', 'r')
# csv = f.readlines()
# f.close()
# uniqAddr = {}
# for l in csv:
#     if not l:
#         continue
#     ll = l.strip().split(',')
#     if len(ll) < 2:
#         continue
#     for lll in ll[1:]:
#         if uniqAddr.get(lll):
#             raise ValueError(ll[0], lll)
#         uniqAddr[lll] = ll[0]
# # 707 print( len(uniqAddr) )

# def uniq_a(lll):
#     if uniqAddr.get(lll):
#         return uniqAddr[lll]
#     return lll

districts = ('浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区',
             '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区',
             '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区' )
running_d = ''

_z = (
   ['0616','https://mp.weixin.qq.com/s/86Ly4-B8zpVAtay0syJuwg']
  ,['0615','https://mp.weixin.qq.com/s/SHpQtAgzJRTHsypyDtEU3w']
  ,['0614','https://mp.weixin.qq.com/s/jNlwZj7s19emjB58lE9rzg']
  ,['0613','https://mp.weixin.qq.com/s/Brq4G4gZOj2y_F4O8cPm2A']
  ,['0612','https://mp.weixin.qq.com/s/7tHJuJUtYEEIqGlywmWpBg']
  ,['0611','https://mp.weixin.qq.com/s/BUs1bbsc_YTmyFkJ-xdPtw']
  ,['0610','https://mp.weixin.qq.com/s/Cv94y7zJ1THMXBkwKloHkA']
  ,['0609','https://mp.weixin.qq.com/s/IpYd6G-lavQmufm1DQiFVg']
  ,['0608','https://mp.weixin.qq.com/s/OKxw0qxTtCy_utS5ilh6Lw']
  ,['0607','https://mp.weixin.qq.com/s/W9tBwbc2tSNe7-zDWw_ViA']
  ,['0606','https://mp.weixin.qq.com/s/ft2t7EVyT96YmwXfvd-zQg']
  ,['0605','https://mp.weixin.qq.com/s/zERWgFNJzWTydSmvjRPFLw']
  ,['0604','https://mp.weixin.qq.com/s/2zJLbgq0spJfXHY9BLMhWA']
  ,['0603','https://mp.weixin.qq.com/s/z-v2eFk7btPaXEBZro8sqQ']
  ,['0602','https://mp.weixin.qq.com/s/eYimdanb4krg7j_vAJd33g']
  ,['0601','https://mp.weixin.qq.com/s/UnPUsNGUyL1_NxBKMQyZpA']
  ,['0531','https://mp.weixin.qq.com/s/CaM334YdoAxbwA8PJ19wcg']
  ,['0530','https://mp.weixin.qq.com/s/1AsoUPz51QTmNUPItNUCFg']
  ,['0529','https://mp.weixin.qq.com/s/kuCaSb1fFdzaUhwsc6KPSA']
  ,['0528','https://mp.weixin.qq.com/s/PHW04o9E4HKgkGE6wt3suA']
  ,['0527','https://mp.weixin.qq.com/s/A5CZRqmuMTdmYcZhdIi9rQ']
  ,['0526','https://mp.weixin.qq.com/s/edhko1xae7do5FhPSER7Qw']
  ,['0525','https://mp.weixin.qq.com/s/ofoMUIJOQNAtwGXn7Xqr3g']
  ,['0524','https://mp.weixin.qq.com/s/Zpll7k6wZfJiPNeV8sz6Ig']
  ,['0523','https://mp.weixin.qq.com/s/-8XvTb6gxkgfNzMxQ_COZw']
  ,['0522','https://mp.weixin.qq.com/s/FE5FmXxk7180mjqoj9jOSA']
  ,['0521','https://mp.weixin.qq.com/s/XWA8Pzf0DQ5i92si5Epsgg']
  ,['0520','https://mp.weixin.qq.com/s/APzs3KMMjfzAZzhypMXAEg']
  ,['0519','https://mp.weixin.qq.com/s/HIjthO2QrWMs3awazdyI5Q']
  ,['0518','https://mp.weixin.qq.com/s/rQ385zJfnJQVH1A9TE98TA']
  ,['0517','https://mp.weixin.qq.com/s/q2BapLzFqFVctV-g9xJYcw']
  ,['0516','https://mp.weixin.qq.com/s/gnW4IoImldVq9jotw_C1nw']
  ,['0515','https://mp.weixin.qq.com/s/19BHG_8SUwK07nUeNjc9Dw']
  ,['0514','https://mp.weixin.qq.com/s/d1qIhfwsisM2jQpfURml3A']
  ,['0513','https://mp.weixin.qq.com/s/lIMFiBlzIXvju2VV_I4j0g']
  ,['0512','https://mp.weixin.qq.com/s/YyhqHoMgyetDu6kP9-Ybpw']
  ,['0511','https://mp.weixin.qq.com/s/i4BwsY-a9zXjkJe-FTea4Q']
  ,['0510','https://mp.weixin.qq.com/s/V9gNghk8vWinad_VT_YAtg']
  ,['0509','https://mp.weixin.qq.com/s/iUhgNb9-2Ofhsg9zxi2hiw']
  ,['0508','https://mp.weixin.qq.com/s/SU8bV1IqoaH2NeUs_HJBzg']
  ,['0507','https://mp.weixin.qq.com/s/Dt_Q7mwgzJIdn7NwqeGNeA']
  ,['0317','https://wsjkw.sh.gov.cn/xwfb/20220318/dc6e1aca667a45a682f32ac514c6062e.html']
  ,['0316','https://wsjkw.sh.gov.cn/xwfb/20220317/46f73d4d70b54982b04c925eea6cb031.html']
  ,['0315','https://wsjkw.sh.gov.cn/xwfb/20220316/18a627b694eb471f9a415dfa20b6d0b4.html'] #区地址个数 200
  ,['0314','https://wsjkw.sh.gov.cn/xwfb/20220315/e2b0122c52304fe0a41a8b726b3413d2.html'] #区地址个数 138
  ,['0313','https://wsjkw.sh.gov.cn/xwfb/20220314/ea83d1b33a2e40fea7de115c16cbae8a.html']
  ,['0312','https://wsjkw.sh.gov.cn/xwfb/20220313/ac598c0104ad49f8913df20d794d68d1.html'] #区地址个数 64
  ,['0311','https://wsjkw.sh.gov.cn/xwfb/20220312/559cc1eb3e9646b6a08b28ce340a3463.html'] #区地址个数 81
  ,['0310','https://wsjkw.sh.gov.cn/xwfb/20220311/a7bb01fac3664085a882d46dc4e194ba.html'] #区地址个数 74
  ,['0309','https://wsjkw.sh.gov.cn/xwfb/20220310/c7a3763da0cd46cbb563df4064ee1a15.html'] #区地址个数 77
  ,['0308','https://wsjkw.sh.gov.cn/xwfb/20220309/077a50ff4cf4422d836e857126008ff6.html']
  ,['0307','https://wsjkw.sh.gov.cn/xwfb/20220308/a2f9fa49a4274509a1a42fa871bf77ee.html'] #区地址个数 55
  ,['0306','https://wsjkw.sh.gov.cn/xwfb/20220307/6490dbd707674b278f40159595aa5cd9.html'] #首次出现区地址
  ,['0506','https://mp.weixin.qq.com/s/bqZp2AqqE-FPzJpx6FlhPA']
  ,['0505','https://mp.weixin.qq.com/s/IqIqMik_fGpPgfNgIZ8ieg']
  ,['0504','https://mp.weixin.qq.com/s/J68hA0ncRR_q91ccVINP0g']
  ,['0503','https://mp.weixin.qq.com/s/KyTRqsRBWbM5cEa2sk2wbg']
  ,['0502','https://mp.weixin.qq.com/s/s_spcc0OApRItbuq5DG2LA']
  ,['0501','https://mp.weixin.qq.com/s/agdZHOqVZh9atNHOQEFTog']
  ,['0430','https://mp.weixin.qq.com/s/qbB7VjEXMTK0zB6JIqBbAA']
  ,['0429','https://mp.weixin.qq.com/s/aQMZ8WmeYEaBPFv0yVs4BQ']
  ,['0428','https://mp.weixin.qq.com/s/aDU54MGe9XPWEMrdKMRFww']
  ,['0427','https://mp.weixin.qq.com/s/SKkU2W-Ic1H_qWnYC9NtXA']
  ,['0426','https://mp.weixin.qq.com/s/SIuDbITNdgWwYyM3eiyrgg']
  ,['0425','https://mp.weixin.qq.com/s/IrtFkZDWaB6io18QXwuQ9g']
  ,['0424','https://mp.weixin.qq.com/s/9-DRQF8pbz_2uivgscOmbw']
  ,['0423','https://mp.weixin.qq.com/s/YNeLEO7BZouZRfyD2TWOlA']
  ,['0422','https://mp.weixin.qq.com/s/LySBR0VJswl_ZI1KtWlXqw']
  ,['0421','https://mp.weixin.qq.com/s/qFvUyEB-R-GKP7vgKR-c3A']
  ,['0420','https://mp.weixin.qq.com/s/8qCvsE578Ehz6UcWYRBfXw']
  ,['0419','https://mp.weixin.qq.com/s/puNUP9bjYlZNELsse09Z0w']
  ,['0418','https://mp.weixin.qq.com/s/GWI6LxYLHOvv1dioN5olxg']
  ,['0417','https://mp.weixin.qq.com/s/LguiUZj-zxy4xy19WO0_UA']
  ,['0416','https://mp.weixin.qq.com/s/dRa-PExJr1qkRis88eGCnQ']
  ,['0415','https://mp.weixin.qq.com/s/ZkhimhWpa92I2EWn3hmd8w']
  ,['0414','https://mp.weixin.qq.com/s/5T76lht3s6g_KTiIx3XAYw']
  ,['0413','https://mp.weixin.qq.com/s/L9AffT-SoEBV4puBa_mRqg']
  ,['0412','https://mp.weixin.qq.com/s/OZGM-pNkefZqWr0IFRJj1g']
  ,['0411','https://mp.weixin.qq.com/s/vxFiV2HeSvByINUlTmFKZA']
  ,['0410','https://mp.weixin.qq.com/s/u0XfHF8dgfEp8vGjRtcwXA']
  ,['0409','https://mp.weixin.qq.com/s/_Je5_5_HqBcs5chvH5SFfA']
  ,['0408','https://mp.weixin.qq.com/s/79NsKhMHbg09Y0xaybTXjA']
  ,['0407','https://mp.weixin.qq.com/s/HTM47mUp0GF-tWXkPeZJlg']
  ,['0406','https://mp.weixin.qq.com/s/8bljTUplPh1q4MXb6wd_gg']
  ,['0405','https://mp.weixin.qq.com/s/djwW3S9FUYBE2L5Hj94a3A']
  ,['0404','https://mp.weixin.qq.com/s/MkKsQkgvUWbwj8z9jG_Zng']
  ,['0403','https://mp.weixin.qq.com/s/uj4TYASUn2YJZQMg2aUvdw']
  ,['0402','https://mp.weixin.qq.com/s/2VWTo6e9gmWJ0vxeZ4PhIw']
  ,['0401','https://mp.weixin.qq.com/s/gQDyFLtdILP2NuSBgcjUxg']
  ,['0331','https://mp.weixin.qq.com/s/hnrGo4KvUvxhpjFyiE8-sQ']
  ,['0330','https://mp.weixin.qq.com/s/SSFVzOSXPTj-aLzR1tdtxw']
  ,['0329','https://mp.weixin.qq.com/s/K6jT1wRMSScBhvxcB2yV4g']
  ,['0328','https://mp.weixin.qq.com/s/656rotFOMeDScnKSt6OmyQ']
  ,['0327','https://mp.weixin.qq.com/s/MfBzdO0bG4fbokKTRCWuIw']
  ,['0326','https://mp.weixin.qq.com/s/JwUn4sVxSvHQs5KoyFn-lw']
  ,['0325','https://mp.weixin.qq.com/s/xV7WBuu_7D9JA_D2mEOH_w']
  ,['0324','https://mp.weixin.qq.com/s/oBQXVicoi5tXuFt06ybsog']
  ,['0323','https://mp.weixin.qq.com/s/XL_hz8ESYGM8ZW7FQuHFRA']
  ,['0322','https://mp.weixin.qq.com/s/UUmzrx54vMdzZBKUm4uKfg']
  ,['0321','https://mp.weixin.qq.com/s/lqzf4il2Io1LXXf11PBN-A']
  ,['0320','https://mp.weixin.qq.com/s/s3FN7zk__wTz-jZM1c_lOg']
  ,['0319','https://mp.weixin.qq.com/s/njMjbpRELpe7SWA7AnB5NA']
  ,['0318','https://mp.weixin.qq.com/s/xLVPnOTErTe3dmAenUyDGQ']
      )

used_kd = []
_data = {}
datadata = {}
for z in _z:
    print( z[0] )
    if z[1].endswith('.html'):
        if not os.path.isfile('html-files/%s.html' % z[0]):
            print( z[1] )
            os.system('scrapy fetch --nolog %s > html-files/%s.html' % (z[1], z[0]) )
            #os.system('curl -o html-files/%s.html %s' % (z[0], z[1]) )
    elif z[1].find('mp.weixin.qq.com') > 0:
        if not os.path.isfile('html-files/%s.htm' % z[0]):
            print( z[1] )
            os.system('scrapy fetch --nolog %s > html-files/%s.htm' % (z[1], z[0]) )
            #os.system('curl -o html-files/%s.htm %s' % (z[0], z[1]) )
        # f = open('shanghaifabu/%s%s.txt' % (z[0],z[0]), 'r')
        # page = f.read()
        # f.close()
        # if z[0] in ('0308','0309'): #@@@@ 本地文件 复制粘贴的文本
        #     pp = page
        # else:
        #     pp = BeautifulSoup(page, features="lxml").find('div', {'id' : 'ivs_content'}).get_text("\n", strip=True)
        # if pp.find('外省来沪') > 0 and pp.find(' 外省来沪') == -1:
        #     raise ValueError(z[0], '外省来沪')
        # if pp.find('来沪求职') > 0 and pp.find(' 来沪求职') == -1:
        #     raise ValueError(z[0], '来沪求职')
        # ppp = re.findall(r'，\s*居住于(\S{2,3}区[^，。]+)', pp ) + re.findall(r'，\s*居住地为(\S{2,3}区[^，。]+)', pp )
        # #print('就读于', re.findall(r'，就读于(\S{2,3}区[^，。]+)', pp) )
        # #print('外省市', re.findall(r'，外省市([^，。]+)', pp) )
        # cc = re.findall('24时，新增本土[^0-9]+(\d{1,3})', pp)[1:]
        # if cc and sum([int(ccc) for ccc in cc]) != len(ppp):
        #     print('搜到新增本土数', '+'.join(cc) )
        #     print('搜到区地址个数', len(ppp))
        #     #print('\n'.join(ppp) )
        # wxx = re.sub(r'(\S{2,3})区', r'\1区,', '\n'.join(ppp) )
    else:
        raise ValueError(z[0], '只能处理.html或mp.weixin.qq.com')

    # res = wxx.replace('，', ',').replace('。', ',').replace('、', ',').replace('；', ',').replace(';', ','
    #         ).replace(' ', ',').replace('\t', ','
    #         ).replace('分别居住于', ',').replace('：', ','
    #         ).replace('我区', ',,,,').replace('已对相关', ',')

    # #Z = [ s.strip() for s in list(filter(None, res.split(',') )) ]
    # Z = [ s.strip() for s in filter(None, res.split(',') ) ]
    # #print(len(Z))
    # ZZ = re.sub(r'\s', ',', '\n'.join(Z))
    # pps = re.sub(r'\s', '', pp).replace('闵行校区', '闵行区')
    # #print(pps)
    # running_k = ''
    # _regex = r"(\S)，\s*(\d+)岁"
    # xx = re.findall(_regex, pps)
    # #x = re.findall(rf"(\S，\d+)岁\S+{zz}", pps)
    # xi = 0
    # data = {}
    # max_d = ''
    # max_dc = 0
    # _ZZ = ZZ.split(',')
    # for zi,zzz in enumerate(_ZZ):
    #     # if len( zz.strip() ) > 20: # 5/18 金山区
    #     #     print('%s\n' % zz.strip() )
    #     # elif zz.find('成功') > -1 or zz.find('目前') > -1:
    #     #     print('## 成功 | 目前\n%s\n' % zz.strip() )
    #     ####
    #     zz = zzz.replace('闵行校区', '闵行区')
    #     if not zz or zz in districts:
    #         running_k = zz
    #         continue
    #     if (zi+1) < len(_ZZ) and _ZZ[zi+1] == '宿舍':
    #         zz += _ZZ[zi+1]
    #         _ZZ[zi+1] = ''
    #     elif (zi+1) < len(_ZZ) and re.match(r'\d+\D', _ZZ[zi+1]):
    #         zz += _ZZ[zi+1]
    #         _ZZ[zi+1] = ''
    #     elif (zi+2) < len(_ZZ) and re.match(r'\d+$', _ZZ[zi+1]):
    #         zz += _ZZ[zi+1] + _ZZ[zi+2]
    #         _ZZ[zi+1] = ''
    #         _ZZ[zi+2] = ''
    #     if not zz in used_kd:
    #         used_kd += [running_k + zz]
    #     #if xi and not xi%20:# or xi in range(30,40): #@@@@
    #     if xi and not z[0] in checked_tags:
    #         print('    ', xi, ','.join(xx[xi]), zz)
    #     # 2022-6-16
    #     zz = uniq_a( '%s%s' % (running_k, zz) )[len(running_k):]
    #     try:
    #         if data.get(running_k + zz):
    #             data[running_k + zz] += [ xx[xi] ]
    #             datadata[running_k + zz] += [[z[0]] + list(xx[xi])]
    #             if len(data[running_k + zz]) > max_dc:
    #                 max_dc = len(data[running_k + zz])
    #                 max_d = running_k + zz
    #         else:
    #             data[running_k + zz] = [ xx[xi] ]
    #             datadata[running_k + zz] = [[z[0]] + list(xx[xi])]
    #     except:
    #         raise ValueError(z[0], running_k, zz, xi, len(xx) )
    #     xi += 1
    # if not z[0] in checked_tags:
    #     print('#%s最大' % z[0], max_d, max_dc ) #, data[max_d]
    #     print('%s' % z[1])
    # else:
    #     print('#%s最后一个' % z[0], ','.join(xx[xi-1]), zz)
    # # if max_dc != len(re.findall(max_d, pps)):
    # #     raise ValueError(z[0], max_d, max_dc, len(re.findall(max_d, pps)) )
    # _data[z[0]] = data
####

# from datetime import datetime
# fz = open('early%s.json' % z[0], 'w')
# fz.write( json.dumps({'version':str(datetime.now()),
#                       'by_day':_data,
#                       'by_address':datadata }, ensure_ascii=False) )
# fz.close()
