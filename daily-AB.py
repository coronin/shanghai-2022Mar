from bs4 import BeautifulSoup
from urllib import request

# os.system('scrapy fetch --nolog https://www.cell.com/cell/newarticles > cell.txt')

z = [
#'0515','']
#'0514','']
#'0513','']
#'0512','']
#'0511','']
'0510','']
#'0509','https://mp.weixin.qq.com/s/iUhgNb9-2Ofhsg9zxi2hiw']
#'0508','https://mp.weixin.qq.com/s/SU8bV1IqoaH2NeUs_HJBzg']
#'0507','https://mp.weixin.qq.com/s/Dt_Q7mwgzJIdn7NwqeGNeA']
#'0317','https://wsjkw.sh.gov.cn/xwfb/20220318/dc6e1aca667a45a682f32ac514c6062e.html']
#'0316','https://wsjkw.sh.gov.cn/xwfb/20220317/46f73d4d70b54982b04c925eea6cb031.html']
#'0315','https://wsjkw.sh.gov.cn/xwfb/20220316/18a627b694eb471f9a415dfa20b6d0b4.html'] #区地址个数 200
#'0314','https://wsjkw.sh.gov.cn/xwfb/20220315/e2b0122c52304fe0a41a8b726b3413d2.html'] #区地址个数 138
#'0313','https://wsjkw.sh.gov.cn/xwfb/20220314/ea83d1b33a2e40fea7de115c16cbae8a.html']
#'0312','https://wsjkw.sh.gov.cn/xwfb/20220313/ac598c0104ad49f8913df20d794d68d1.html'] #区地址个数 64
#'0311','https://wsjkw.sh.gov.cn/xwfb/20220312/559cc1eb3e9646b6a08b28ce340a3463.html'] #区地址个数 81
#'0310','https://wsjkw.sh.gov.cn/xwfb/20220311/a7bb01fac3664085a882d46dc4e194ba.html'] #区地址个数 74
#'0309','https://wsjkw.sh.gov.cn/xwfb/20220310/c7a3763da0cd46cbb563df4064ee1a15.html'] #区地址个数 77
#'0308','https://wsjkw.sh.gov.cn/xwfb/20220309/077a50ff4cf4422d836e857126008ff6.html']
#'0307','https://wsjkw.sh.gov.cn/xwfb/20220308/a2f9fa49a4274509a1a42fa871bf77ee.html'] #区地址个数 55
#'0306','https://wsjkw.sh.gov.cn/xwfb/20220307/6490dbd707674b278f40159595aa5cd9.html']
#'0305','https://wsjkw.sh.gov.cn/xwfb/20220306/ce44bea5ad8e41bf85165cdf35c84bdb.html']
#'0304','https://wsjkw.sh.gov.cn/xwfb/20220305/1fd23e48cc4f479ea8fc56c9e1052759.html']
#'0506','https://mp.weixin.qq.com/s/bqZp2AqqE-FPzJpx6FlhPA']
#'0505','https://mp.weixin.qq.com/s/IqIqMik_fGpPgfNgIZ8ieg']
#'0504','https://mp.weixin.qq.com/s/J68hA0ncRR_q91ccVINP0g']
#'0503','https://mp.weixin.qq.com/s/KyTRqsRBWbM5cEa2sk2wbg']
#'0502','https://mp.weixin.qq.com/s/s_spcc0OApRItbuq5DG2LA']
#'0501','https://mp.weixin.qq.com/s/agdZHOqVZh9atNHOQEFTog']
#'0430','https://mp.weixin.qq.com/s/qbB7VjEXMTK0zB6JIqBbAA']
#'0429','https://mp.weixin.qq.com/s/aQMZ8WmeYEaBPFv0yVs4BQ']
#'0428','https://mp.weixin.qq.com/s/aDU54MGe9XPWEMrdKMRFww']
#'0427','https://mp.weixin.qq.com/s/SKkU2W-Ic1H_qWnYC9NtXA']
#'0426','https://mp.weixin.qq.com/s/SIuDbITNdgWwYyM3eiyrgg']
#'0425','https://mp.weixin.qq.com/s/IrtFkZDWaB6io18QXwuQ9g']
#'0424','https://mp.weixin.qq.com/s/9-DRQF8pbz_2uivgscOmbw']
#'0423','https://mp.weixin.qq.com/s/YNeLEO7BZouZRfyD2TWOlA']
#'0422','https://mp.weixin.qq.com/s/LySBR0VJswl_ZI1KtWlXqw']
#'0421','https://mp.weixin.qq.com/s/qFvUyEB-R-GKP7vgKR-c3A']
#'0420','https://mp.weixin.qq.com/s/8qCvsE578Ehz6UcWYRBfXw']
#'0419','https://mp.weixin.qq.com/s/puNUP9bjYlZNELsse09Z0w']
#'0418','https://mp.weixin.qq.com/s/GWI6LxYLHOvv1dioN5olxg']
#'0417','https://mp.weixin.qq.com/s/LguiUZj-zxy4xy19WO0_UA']
#'0416','https://mp.weixin.qq.com/s/dRa-PExJr1qkRis88eGCnQ']
#'0415','https://mp.weixin.qq.com/s/ZkhimhWpa92I2EWn3hmd8w']
#'0414','https://mp.weixin.qq.com/s/5T76lht3s6g_KTiIx3XAYw']
#'0413','https://mp.weixin.qq.com/s/L9AffT-SoEBV4puBa_mRqg']
#'0412','https://mp.weixin.qq.com/s/OZGM-pNkefZqWr0IFRJj1g']
#'0411','https://mp.weixin.qq.com/s/vxFiV2HeSvByINUlTmFKZA']
#'0410','https://mp.weixin.qq.com/s/u0XfHF8dgfEp8vGjRtcwXA']
#'0409','https://mp.weixin.qq.com/s/_Je5_5_HqBcs5chvH5SFfA']
#'0408','https://mp.weixin.qq.com/s/79NsKhMHbg09Y0xaybTXjA']
#'0407','https://mp.weixin.qq.com/s/HTM47mUp0GF-tWXkPeZJlg']
#'0406','https://mp.weixin.qq.com/s/8bljTUplPh1q4MXb6wd_gg']
#'0405','https://mp.weixin.qq.com/s/djwW3S9FUYBE2L5Hj94a3A']
#'0404','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654524377&idx=1&sn=b50ea85ec4d5562054027ac55a22e38b&chksm=bd31cea28a4647b4f551c85b41ea01cc787917f6f4c3cf6c3b1408977b570209ce94bb84a131']
#'0403','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654524064&idx=1&sn=8d2e8b5ba80b1f44ae6c900b4304eee3&chksm=bd31cfdb8a4646cd90b686a7d20913c63d9b9516eca3e81be3418a58109309736a4343e7c8c9']
#'0402','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654523814&idx=1&sn=fadbd70496d55b598888393f73b3d2b6&chksm=bd31ccdd8a4645cb94d2dfe51313c7466eafd18cef19268599eea36123922b4105c454b9ac5a']
#'0401','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654523507&idx=1&sn=6f606c580a980252ae28eda6607e1be7&chksm=bd31cd088a46441e073ac309583ee3cff6e764dddd097df24f544d28a4f5142596155b8f7d6b']
#'0331','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654523089&idx=1&sn=e98984c433cdf7371b97b1889d1560aa&chksm=bd31d3aa8a465abc77c698dc3f55b73236d63ae64547c80dcac5c6cdd37c2b77c111af20903b']
#'0330','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654522572&idx=1&sn=296675317f74525a072aa9003baffdbe&chksm=bd31d1b78a4658a16dee2d94543cedd73f14c4927cd90d9b8f57637771e6eb8075959bd118d0']
#'0329','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654522433&idx=1&sn=7c55d1f38d41f388afde2f5e6c6d6e75&chksm=bd31d13a8a46582c2bc466f28366f5140b6404f528c3597e181db67787ff7b3e7596424dbaa4']
#'0328','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654522212&idx=1&sn=707a7e5adf72c2bade3473207509d3fe&chksm=bd31d61f8a465f097416adc882077f8237f0633f26ade099110abb3aa19fae663bec90e442d2']
#'0327','https://mp.weixin.qq.com/s/MfBzdO0bG4fbokKTRCWuIw']
#'0326','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654521587&idx=1&sn=12c3e3429d20f1d801e0c34ab5488e20&chksm=bd31d5888a465c9e0ce61c4a6fb59da5a46e75f0ecfee93929c36a73eeae786e4f28da6f7ded']
#'0325','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654521380&idx=1&sn=7e3a3d3b035cbc7a520278d5ec88571b&chksm=bd31d55f8a465c49df21b35dd5ee2a86d9f6530b9af581e53c8361f6323c95756466966e75b9']
#'0324','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654521097&idx=1&sn=470fce05c7b3d735fc3976f6c6f2ae2f&chksm=bd31da728a465364814e12e970da70dee62ade20e90d273eb25183a77aa0626fff781a0491d7']
#'0323','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520830&idx=1&sn=2e3e7e9a521714c3ff7b4a996ff95d83&chksm=bd31d8858a4651938b338ba2dc62aaa758ff9dd60d7a54c06a48c4917b9ac7b5a72c0901ac13']
#'0322','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520644&idx=1&sn=428742723dd66d56bdf0c5a0a252f37d&chksm=bd31d83f8a4651295d0dcc880d02c25569b5e732283a781c6685a2697855b96023153c0ee7dc']
#'0321','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520388&idx=1&sn=abc2cfa66fafebaa399e345898c117de&chksm=bd31d93f8a46502955728ff97269f071519d7390a40e19b9e3162cd4b544c60028fb6d739a62']
#'0320','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520238&idx=1&sn=47dd022fb617df72df0a0f486c9278c6&chksm=bd31ded58a4657c3afc7406744c71b2c50e2d204825e4059a13b47abd2e0412dc4cc7485a379']
#'0319','https://mp.weixin.qq.com/s/njMjbpRELpe7SWA7AnB5NA']
#'0318','https://mp.weixin.qq.com/s/xLVPnOTErTe3dmAenUyDGQ']
# no place info before 3/18
# 从3月18日起三天内，我市对非重点区域内人员分时分批次开展一次免费核酸检测
# 从3月13日启动校园封闭管理

day0x0x = {
'浦东新区': '', # 浦东发布
'黄浦区': '',
'静安区': '',
'徐汇区': '',
'长宁区': '',
'普陀区': '',
'虹口区': '',
'杨浦区': '',
'宝山区': '',
'闵行区': '', # 今日闵行
'嘉定区': '',
'金山区': '',
'松江区': '',
'青浦区': '', # 绿色青浦
'奉贤区': '',
'崇明区': '' }

day0509 = {
'浦东新区': 'https://mp.weixin.qq.com/s/S4yC-h1VVR-0ED0vlHCtsQ', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/RXsvHMUhcTgQC8OjK4pgsg',
'静安区': 'https://mp.weixin.qq.com/s/weL60QYWebORHo8U_QfZTA',
'徐汇区': 'https://mp.weixin.qq.com/s/Jxk-oJavNfkJijnYNDRyEA',
'长宁区': 'https://mp.weixin.qq.com/s/SN1m-kjoeGuhnNp5fKtDoQ',
'普陀区': 'https://mp.weixin.qq.com/s/bobQCBxMhl2rENLUuBnr3Q',
'虹口区': 'https://mp.weixin.qq.com/s/747u0xbA-9XVvK3QgBgqyA',
'杨浦区': 'https://mp.weixin.qq.com/s/tDu5kerQhruyVoVAOC8IHQ',
'宝山区': 'https://mp.weixin.qq.com/s/gB6O8dKR1CJxJ3Z2IpoOIg',
'闵行区': 'https://mp.weixin.qq.com/s/VEHu6X2b8f_Lq5_-WZqInQ', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/ENfosZJPkQxcd2cMIlanFQ',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/F73rHoyDdDztsKIsZQ5zxw',
'青浦区': 'https://mp.weixin.qq.com/s/QjGyiI0hmoD_gNeFcUEGQw', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/JmxeH9jEIhArsWwfqVx4pA',
'崇明区': 'https://mp.weixin.qq.com/s/04lTr76cq5ICe2uYks9bhA' }

day0508 = {
'浦东新区': 'https://mp.weixin.qq.com/s/LdeyRZqanZ676LutgnMbfw', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/xyzkwszLGGQLy_-0UJn0HA',
'静安区': 'https://mp.weixin.qq.com/s/Aqx4ACAmPWbv84wTMfxnFA',
'徐汇区': 'https://mp.weixin.qq.com/s/vdHTHPNO2FWa3a_vgeYZQQ',
'长宁区': 'https://mp.weixin.qq.com/s/DcCX9Yv3y-Ejm97y0m2sFA',
'普陀区': 'https://mp.weixin.qq.com/s/IYH41kqB5UfoCZu-EPce8g',
'虹口区': 'https://mp.weixin.qq.com/s/kdjBE0w6B0X_FBuEZS9Law',
'杨浦区': 'https://mp.weixin.qq.com/s/lGunXB2rLrMljB9jkqFVUg',
'宝山区': 'https://mp.weixin.qq.com/s/tc9p5zf9QQp5H77ktMTz7A',
'闵行区': 'https://mp.weixin.qq.com/s/H3va1UF4qnQX2YLKWhUsgg', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/G4GI_mIBHXBCOXXia2oXCg',
'金山区': 'https://mp.weixin.qq.com/s/P9hc1lD5zssWnOHSvR2Org',
'松江区': 'https://mp.weixin.qq.com/s/qra7ygWTdaGwXnAtVxPoaw',
'青浦区': 'https://mp.weixin.qq.com/s/qpZZqrOhVLV-RtLWJIMfSA', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/WZ2IDzejXoztxUzhIU5Z5Q',
'崇明区': 'https://mp.weixin.qq.com/s/1Nwsc03LgKwnSddp3dyPRQ' }

day0507 = {
'浦东新区': 'https://mp.weixin.qq.com/s/XTQnkZwu4v5rkCXurVAJZg', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/UEncM5wqRWQprNuzIChSzw',
'静安区': 'https://mp.weixin.qq.com/s/tLQ8TXlYjM4LExBCuHHuSg',
'徐汇区': 'https://mp.weixin.qq.com/s/jT5sOaouLFhX-f6UgrguJQ',
'长宁区': 'https://mp.weixin.qq.com/s/v-WL0fTIwC3tbjpkxfFp3Q',
'普陀区': 'https://mp.weixin.qq.com/s/baKLjhEmtxbzOoWtGPldOw',
'虹口区': 'https://mp.weixin.qq.com/s/UQNfeKWC951wRSieDIf-kg',
'杨浦区': 'https://mp.weixin.qq.com/s/Fqixdx8jmLffzOgbWnIBLw',
'宝山区': 'https://mp.weixin.qq.com/s/97qo9ApMpMDUJL2szWeqLA',
'闵行区': 'https://mp.weixin.qq.com/s/LAIFzFcpQNq7RPvNL_PxLg', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/0j5N6ErSQbx46IUUveiHCQ',
'金山区': 'https://mp.weixin.qq.com/s/-yY0SMP0pMqgcoE-bBagRA',
'松江区': 'https://mp.weixin.qq.com/s/JAq9g1PvPdsivhL4JDxpvQ',
'青浦区': 'https://mp.weixin.qq.com/s/FxVt2D_EO8G9SC00LhhNoQ', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/o7MPXckAbicMdURmBoz49w',
'崇明区': 'https://mp.weixin.qq.com/s/7wHGOFOqck6-3vMNVUFBlg' }

day0506 = {
'浦东新区': 'https://mp.weixin.qq.com/s/ITILcJZ4bDb4_knaukb6Uw', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/H4hfCQcYCwSvpfIL63a9aw',
'静安区': 'https://mp.weixin.qq.com/s/FgINfp4st8V-rmFMahIy0g',
'徐汇区': 'https://mp.weixin.qq.com/s/pGWBQY4kbvd2fqgNhTGGYg',
'长宁区': 'https://mp.weixin.qq.com/s/DHblFAhkoq76iLGIi_r-1w',
'普陀区': 'https://mp.weixin.qq.com/s/CVeRIZv88LZoFmLcV3HEzA',
'虹口区': 'https://mp.weixin.qq.com/s/9AH4e7IxtAMxr9GCxJSnOQ',
'杨浦区': 'https://mp.weixin.qq.com/s/fgxZ7ttJBlxI0c00js32gw',
'宝山区': 'https://mp.weixin.qq.com/s/4z2hEoN8m6goBTsqtPc4BA',
'闵行区': 'https://mp.weixin.qq.com/s/Y7JSTCiyTHfDm8k8vQwuKQ', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/gx4PxwNB-2Ry7YtqsjTsow',
'金山区': 'https://mp.weixin.qq.com/s/FXQq3TzL0g4fuyTkGBm3ow',
'松江区': 'https://mp.weixin.qq.com/s/87zaEsN5q1NnYO1xfHhodg',
'青浦区': 'https://mp.weixin.qq.com/s/bno49i-jXiSl2g9nW-bkkA', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/9rGKkG6R4Q2iwt8LroHO9g',
'崇明区': 'https://mp.weixin.qq.com/s/fr4fO4fQROhn0Up8j-Qutg' }


if not z[1]:
    day = globals()['day%s' % z[0]]
    zz0 = list(day.keys())
    zz1 = list(day.values())
    wxx = '\n\n\n\n'
    for i,z1 in enumerate(zz1):
        if not z1:
            print('day%s 没有%s的链接' % (z[0],zz0[i]) )
        else:
            wx = BeautifulSoup(request.urlopen(z1).read(), features="lxml")
            wx_ = wx.find('div', {'id' : 'img-content'}).get_text()
            if wx_.find('%s月%s日' % (int(z[0][:2]), int(z[0][2:])) ) < 0:
                print('day%s %s的链接没有有效日期' % (z[0],zz0[i]) )
                raise
            wxx += '\n\n\n\n%s' % wx_
elif z[1].endswith('.html'):
    import os
    if not os.path.isfile('shanghaifabu/%s%s.txt' % (z[0],z[0])):
        os.system('scrapy fetch --nolog %s > %s%s.txt' % (z[1], z[0],z[0]) )
    f = open('shanghaifabu/%s%s.txt' % (z[0],z[0]), 'r')
    page = f.read()
    f.close()
    pp = BeautifulSoup(page, features="lxml").find('div', {'id' : 'ivs_content'}).get_text()
    import re
    ppp = re.findall(r'，居住于(\S{2,3}区[^，。]+)', pp) + re.findall(r'，居住地为(\S{2,3}区[^，。]+)', pp)
    print('就读于', re.findall(r'，就读于(\S{2,3}区[^，。]+)', pp) )
    print('外省市', re.findall(r'，外省市([^，。]+)', pp) )
    print('搜到区地址个数', len(ppp))
    #print('\n'.join(ppp) )
    print('搜到新增本土数', '+'.join( re.findall('24时，新增本土[^0-9]+(\d{1,3})', pp)[1:]) )
    wxx = re.sub(r'(\S{2,3})区', r'\1区,', '\n'.join(ppp) )
else:
    wx = BeautifulSoup(request.urlopen(z[1]).read(), features="lxml")
    wxx = wx.find('div', {'id' : 'img-content'}).get_text()
res = wxx.replace('，', ',').replace('。', ',').replace('、', ',').replace('；', ',').replace(';', ','
        ).replace(' ', ',').replace('\t', ','
        ).replace('分别居住于', ',').replace('：', ','
        ).replace('我区', ',,,,')

Z = [ s.strip() for s in list(filter(None, res.split(',') )) ]
#print(len(Z))
for zz in Z:
    if len(zz) > 50:
        print('\n', zz, '\n')
    elif zz.find('成功') > -1 or zz.find('目前') > -1:
        print(zz)
print(z[1])
if not z[1]:
    fz = open('%s%s.txt' % (z[0],z[0]), 'w')
else:
    fz = open('%s.txt' % z[0], 'w')
fz.write( u'\n'.join(Z) )
fz.close()
print('CAUTION: please check %s.txt for missing line break' % z[0] )