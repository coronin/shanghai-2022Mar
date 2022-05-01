from bs4 import BeautifulSoup
from urllib import request

# os.system('scrapy fetch --nolog https://www.cell.com/cell/newarticles > cell.txt')

z = [
#'','']
#'','']
#'','']
#'','']
#'','']
#'','']
#'','']
#'','']
'0430','https://mp.weixin.qq.com/s/qbB7VjEXMTK0zB6JIqBbAA']
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

wx = BeautifulSoup(request.urlopen(z[1]).read(), features="lxml")
wxx = wx.find('div', {'id' : 'img-content'})
res = wxx.get_text().replace('，', ',').replace('。', ',').replace('、', ',').replace('；', ',').replace(';', ','
                   ).replace(' ', ',').replace('\t', ','
                   ).replace('分别居住于', ',').replace('：', ',')

Z = [ s.strip() for s in list(filter(None, res.split(',') )) ]
print(len(Z))
for zz in Z:
    if len(zz) > 50:
        print('\n', zz, '\n')
    elif zz.find('成功') > -1 or zz.find('目前') > -1:
        print(zz)
print(z[1])
fz = open('%s.txt' % z[0], 'w')
fz.write( u'\n'.join(Z) )
fz.close()

print('CAUTION: please check %s.txt for missing line break' % z[0] )
