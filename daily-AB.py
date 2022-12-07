from bs4 import BeautifulSoup
from urllib import request
import re

# os.system('scrapy fetch --nolog https://www.cell.com/cell/newarticles > cell.txt')

z = [
#'1226',''] #### release in 2023
#'1225','']
#'1224','']
#'1223','']
#'1222','']
#'1221','']
#'1220','']
#'1219','']
#'1218','']
#'1217','']
#'1216','']
#'1215','']
#'1214','']
#'1213','']
#'1212','']
#'1211','']
#'1210','']
#'1209','']
#'1208','']
#'1207','']
'1206','']
#'1205','https://mp.weixin.qq.com/s/x53yWdk9Yh2NyCxTCmK2dA']
#'1204','https://mp.weixin.qq.com/s/RKAxWoVpT8Xf4FVxDjyGag']
#'1203','https://mp.weixin.qq.com/s/EH49z-wuXPbNqLrZzZQrqQ']
#'1202','https://mp.weixin.qq.com/s/rEiwTyxBmobwulZXY36gSQ']
#'1201','https://mp.weixin.qq.com/s/ZCBfncrbCt6qmpEB8JUfGg']
#'1130','https://mp.weixin.qq.com/s/Di0fZTA8StiemDfZ7SGT9Q']
#'1129','https://mp.weixin.qq.com/s/dEqtV2areiVBam4jOlYN6g']
#'1128','https://mp.weixin.qq.com/s/LCKA8pfmiJXzGV-_LBvQ7g']
#'1127','https://mp.weixin.qq.com/s/74TBVWQRtjztS12lpM1phQ']
#'1126','https://mp.weixin.qq.com/s/u9FvSTETKVZ6ZRvxqjoj3g']
#'1125','https://mp.weixin.qq.com/s/xuHtUpWv0AyUMm5V4TDGVQ']
#'1124','https://mp.weixin.qq.com/s/GalHrAmxvEji4HCHKYq-1g']
#'1123','https://mp.weixin.qq.com/s/ntMh6A_MxxV21yqAS_64YQ']
#'1122','https://mp.weixin.qq.com/s/Q6ZdCVvHhECMAEH71wH5kg']
#'1121','https://mp.weixin.qq.com/s/BxjwJU9WdmEbET4bZBG_og']
#'1120','https://mp.weixin.qq.com/s/9R2mvY0s9EXXNWiMjZLj9w']
#'1119','https://mp.weixin.qq.com/s/0C0fw_vkH-j52l-5SGV5lw']
#'1118','https://mp.weixin.qq.com/s/4rowIR5E0O4qIjhuCmsH7g']
#'1117','https://mp.weixin.qq.com/s/N9JrMm0gK-2ISnsvrSuxwA']
#'1116','https://mp.weixin.qq.com/s/1UhcmbUbYcOu4HSbMy4W5g'] #### release 12月 html 修改
#'1115','https://mp.weixin.qq.com/s/nde03aFQuJ3pv0te7tYfGA']
#'1114','https://mp.weixin.qq.com/s/9r7cOFIkNFiEed0fRiXPoA']
#'1113','https://mp.weixin.qq.com/s/ArcRHEN6tEVFEHIblTVZVg']
#'1112','']
#'1111','']
#'1110','https://mp.weixin.qq.com/s/A3WI4bD7t6nIwCuofJKrjw']
#'1109','https://mp.weixin.qq.com/s/4xSpWBp32Kn_rvnwHq6xqA']
#'1108','https://mp.weixin.qq.com/s/HiwRlbK8vt9qLeaTyu2O9g']
#'1107','https://mp.weixin.qq.com/s/V-mrRZUklGBGd48-4I7l_A']
#'1106','']
#'1105','https://mp.weixin.qq.com/s/YrEKCrxJucruSzxVS1NyZw']
#'1104','']
#'1103','https://mp.weixin.qq.com/s/pN2GxMfEp_FA4Y4Sn7DwJg']
#'1102','https://mp.weixin.qq.com/s/GWm_WechBE0cCcBrlhSGvA']
#'1101','']
#'1031','']
#'1030','https://mp.weixin.qq.com/s/IVedDEOChyGqu9jnqpHUpA']
#'1029','https://mp.weixin.qq.com/s/Xrn3UGRdjXN8We2znzpP6w']
#'1028','https://mp.weixin.qq.com/s/C10URiybQOjioMjMFOv_3w']
#'1027','https://mp.weixin.qq.com/s/J8hhoZK0_maxAw9QF9-qvg']
#'1026','https://mp.weixin.qq.com/s/mPvzsvsod-cUNXv_wBUWkw']
#'1025','https://mp.weixin.qq.com/s/WjCGAMkd_cpZswjLFFWL8A']
#'1024','https://mp.weixin.qq.com/s/B05-VEg-f26hqy3JZfz7kw']
#'1023','https://mp.weixin.qq.com/s/8W8QQEb9KhDHkB0qGFeVwQ']
#'1022','https://mp.weixin.qq.com/s/Y3I56x9aG1TjXEYsvZaLfg']
#'1021','https://mp.weixin.qq.com/s/CLO7GNohn8nc6-QCvnZ9uQ']
#'1020','https://mp.weixin.qq.com/s/foq6JP_Pr1cqPdinmk6tJQ']
#'1019','https://mp.weixin.qq.com/s/fNOBYrC4l6qHUs963-fj3A']
#'1018','https://mp.weixin.qq.com/s/kGhAoGp0BpM4oGmARphFPQ']
#'1017','https://mp.weixin.qq.com/s/HxUbP4hf5ReTIFjadN-g4g']
#'1016','https://mp.weixin.qq.com/s/JoM49IuJ7-9xq-BWG47Bkg']
#'1015','https://mp.weixin.qq.com/s/jQUIEpkWpU9x4RW61fd4Ew']
#'1014','https://mp.weixin.qq.com/s/riA0rzTwY98_ZUIbhLqjqA']
#'1013','https://mp.weixin.qq.com/s/-bhVGef3ndVD6NllrYBRCw']
#'1012','https://mp.weixin.qq.com/s/h4eg0fkNlB5okIn8Tv9LUg']
#'1011','https://mp.weixin.qq.com/s/TwdBb7E3y0Xjwksn48NzZQ']
#'1010','https://mp.weixin.qq.com/s/L9qrmc3Q0P0FDTuArPGmXw']
#'1009','https://mp.weixin.qq.com/s/WI74j6noML7zrPS-VpSlsw']
#'1008','https://mp.weixin.qq.com/s/VcxbqQuJ8PCiQma5SOuo-w']
#'1007','https://mp.weixin.qq.com/s/8m3_UzSVXzxXdlKx9D8boQ']
#'1006','https://mp.weixin.qq.com/s/CI1NPofVeFusmXTHLKseZg']
#'1005','https://mp.weixin.qq.com/s/CQveQLCYdDNgZEJQEFunsw']
#'1004','https://mp.weixin.qq.com/s/Qx_1tvzZAtHbGRurmEQ0Ew']
#'1003','']
#'1002','']
#'1001','https://mp.weixin.qq.com/s/r8d1dN-aIvJzL54JUhuQaQ']
#'0930','https://mp.weixin.qq.com/s/HmnPMLPRSaTjZMIbjKTF1Q']
#'0929','https://mp.weixin.qq.com/s/S9YKxPXc3V1Lql8j47AvfA']
#'0928','']
#'0927','']
#'0926','']
#'0925','']
#'0924','']
#'0923','']
#'0922','']
#'0921','']
#'0920','']
#'0919','']
#'0918','https://mp.weixin.qq.com/s/uaOV0vnkkcYEt72h2IDCHQ']
#'0917','']
#'0916','https://mp.weixin.qq.com/s/B8b-CD0pWgN227siwO-K0A']
#'0915','']
#'0914','']
#'0913','']
#'0912','']
#'0911','https://mp.weixin.qq.com/s/FbuE4MJ3uXbP0D02llfdSA']
#'0910','https://mp.weixin.qq.com/s/oRnNmamrl6_q2Wumr5Dmxg']
#'0909','https://mp.weixin.qq.com/s/WA4cV62lWfZqREIh2xlQKw']
#'0908','']
#'0907','https://mp.weixin.qq.com/s/HhuRDuNuhWKo_8GJdKe-AQ']
#'0906','']
#'0905','']
#'0904','']
#'0903','https://mp.weixin.qq.com/s/NZgo61Q5EuAi3MyShSLDow']
#'0902','https://mp.weixin.qq.com/s/wROVgmmruVHxifo2O5IR2g']
#'0901','https://mp.weixin.qq.com/s/ZAZN-AcBY9nLZgAHPYrvtw']
#'0831','']
#'0830','https://mp.weixin.qq.com/s/-wXZ9eji_Ti75ehisUi00Q']
#'0829','']
#'0828','']
#'0827','https://mp.weixin.qq.com/s/i9pRRQ2I_W-QB5Oxi4sVbw']
#'0826','https://mp.weixin.qq.com/s/O_fppcM1RK3gMS9_pFZS4g']
#'0825','https://mp.weixin.qq.com/s/pJAKtcQTAFYzgGeCiQT8BQ']
#'0824','https://mp.weixin.qq.com/s/dRwGHdjca7CWChOpJTStiw']
#'0823','']
#'0822','https://mp.weixin.qq.com/s/xz-fg_z6lthKPEyVDP7Nhg']
#'0821','https://mp.weixin.qq.com/s/8vcrmQHRclqw168oJhH6YQ']
#'0820','https://mp.weixin.qq.com/s/V3T9tJyHZeqhZ68W3knxEg']
#'0819','https://mp.weixin.qq.com/s/YV9b1CFkRnfS2Qt393VOEQ']
#'0818','https://mp.weixin.qq.com/s/nhmg543IewcaYiBhz0uylA']
#'0817','https://mp.weixin.qq.com/s/trCCdiZQVEU2pgcsLVe9NQ']
#'0816','https://mp.weixin.qq.com/s/UyrycYaMeR3wYfgk_QCsTg']
#'0815','https://mp.weixin.qq.com/s/OxNg-fU-KCLkg6Cm_2hTYA']
#'0814','https://mp.weixin.qq.com/s/qo6f4gsMvsMjBOlnLkoljA']
#'0813','https://mp.weixin.qq.com/s/6I3LrDBJpdhg577ohdnzOg']
#'0812','https://mp.weixin.qq.com/s/Lztvgq7XsdGxXTNWh03xfA']
#'0811','https://mp.weixin.qq.com/s/KIIeBO4ZKQrQ-RNwXDMtCA']
#'0810','']
#'0809','']
#'0808','']
#'0807','']
#'0806','']
#'0805','']
#'0804','']
#'0803','https://mp.weixin.qq.com/s/eHoqI4Dxt9JRXUFcWV-Vrg']
#'0802','']
#'0801','']
#'0731','']
#'0730','https://mp.weixin.qq.com/s/qKWVnS7ph0aNIIe-fctdgw']
#'0729','https://mp.weixin.qq.com/s/bSSsQkpNQGv_5aLb_ATE5g']
#'0728','https://mp.weixin.qq.com/s/stglzCvCZXSh6BzZ0586_Q']
#'0727','https://mp.weixin.qq.com/s/QLf0Mw9fBRcKgKn5qorRIw']
#'0726','https://mp.weixin.qq.com/s/A0T3m8QbboaHWWG3A2Dtlw']
#'0725','https://mp.weixin.qq.com/s/KdrQr4qzaGp1mTDIFFcotw']
#'0724','https://mp.weixin.qq.com/s/jTZaHiSl4kw6Mn_rruq_rw']
#'0723','https://mp.weixin.qq.com/s/4SkYPq1ujXhl3VP7oAVcvg']
#'0722','https://mp.weixin.qq.com/s/x_V84KfY9-68wp1pJFa8Mg']
#'0721','https://mp.weixin.qq.com/s/wqe1ROcRqVJHKQhHFjr9pA']
#'0720','https://mp.weixin.qq.com/s/9oYiG5YHSqT7Uk1rpwuewQ']
#'0719','https://mp.weixin.qq.com/s/LnSF6NOPWFmG5hupGarJZg']
#'0718','https://mp.weixin.qq.com/s/pDtSC5j2K2f0PJWQa0Sp6A']
#'0717','https://mp.weixin.qq.com/s/vavQTBsin99umUg5ExG5Rg']
#'0716','https://mp.weixin.qq.com/s/5dZJIfh39KT1P4oXzTZyaQ']
#'0715','https://mp.weixin.qq.com/s/5vXyOCCXlzPDBMcPCMov9w']
#'0714','https://mp.weixin.qq.com/s/-mJKaMKFrsKx8gO3HcpqAw']
#'0713','https://mp.weixin.qq.com/s/UviL3eGLHkBG37qhppSRzA']
#'0712','https://mp.weixin.qq.com/s/uUnv6k7BYk5bviTJBQweLA']
#'0711','https://mp.weixin.qq.com/s/eFiTJyRQO6ZhxNKbBsfggQ']
#'0710','https://mp.weixin.qq.com/s/1f8ZPdgWXUCnaMM_EwaI5A']
#'0709','https://mp.weixin.qq.com/s/exsx3D4y_Gam-vgta35dPA']
#'0708','https://mp.weixin.qq.com/s/3cjNWoQd-QcKl1OwT1KdBw']
#'0707','https://mp.weixin.qq.com/s/PaASuZWvgpty-q8PPl9IbA']
#'0706','https://mp.weixin.qq.com/s/YDPho6dvDMpOGB3VBqgKtg']
#'0705','https://mp.weixin.qq.com/s/mbSfVJlXGvGzhVklVi0nUw']
#'0704','https://mp.weixin.qq.com/s/ib4zxyzI2HDikz9ufqrwPA']
#'0703','https://mp.weixin.qq.com/s/3k5Yl-1l-2NPmWd55JWKyQ']
#'0702','https://mp.weixin.qq.com/s/tlGWBTWFyKkVi5p9v7qiqA']
#'0701','']
#'0630','']
#'0629','']
#'0628','']
#'0627','']
#'0626','https://mp.weixin.qq.com/s/ly38iFyOY_asZisiSoVyWA']
#'0625','']
#'0624','']
#'0623','https://mp.weixin.qq.com/s/QTlA_DirQA1P32hGA4vHKQ']
#'0622','https://mp.weixin.qq.com/s/AlxUN95U1wRGvQWD2NxO2Q']
#'0621','https://mp.weixin.qq.com/s/vLpGSe6jNrVajPurDqZqrw']
#'0620','https://mp.weixin.qq.com/s/IEugzGICkgeqP7zUYqBA4Q']
#'0619','https://mp.weixin.qq.com/s/ZoMYifQ9nBHNqLlAzEETUA']
#'0618','https://mp.weixin.qq.com/s/K2YZDEHeoJQC4oa2qN7rbA']
#'0617','https://mp.weixin.qq.com/s/CzHc-xFiTbldTrX5g6NzQA']
#'0616','https://mp.weixin.qq.com/s/86Ly4-B8zpVAtay0syJuwg']
#'0615','https://mp.weixin.qq.com/s/SHpQtAgzJRTHsypyDtEU3w']
#'0614','https://mp.weixin.qq.com/s/jNlwZj7s19emjB58lE9rzg']
#'0613','https://mp.weixin.qq.com/s/Brq4G4gZOj2y_F4O8cPm2A']
#'0612','https://mp.weixin.qq.com/s/7tHJuJUtYEEIqGlywmWpBg']
#'0611','https://mp.weixin.qq.com/s/BUs1bbsc_YTmyFkJ-xdPtw']
#'0610','https://mp.weixin.qq.com/s/Cv94y7zJ1THMXBkwKloHkA']
#'0609','https://mp.weixin.qq.com/s/IpYd6G-lavQmufm1DQiFVg']
#'0608','https://mp.weixin.qq.com/s/OKxw0qxTtCy_utS5ilh6Lw']
#'0607','https://mp.weixin.qq.com/s/W9tBwbc2tSNe7-zDWw_ViA']
#'0606','https://mp.weixin.qq.com/s/ft2t7EVyT96YmwXfvd-zQg']
#'0605','https://mp.weixin.qq.com/s/zERWgFNJzWTydSmvjRPFLw']
#'0604','https://mp.weixin.qq.com/s/2zJLbgq0spJfXHY9BLMhWA']
#'0603','https://mp.weixin.qq.com/s/z-v2eFk7btPaXEBZro8sqQ']
#'0602','https://mp.weixin.qq.com/s/eYimdanb4krg7j_vAJd33g']
#'0601','https://mp.weixin.qq.com/s/UnPUsNGUyL1_NxBKMQyZpA']
#'0531','https://mp.weixin.qq.com/s/CaM334YdoAxbwA8PJ19wcg']
#'0530','https://mp.weixin.qq.com/s/1AsoUPz51QTmNUPItNUCFg']
#'0529','https://mp.weixin.qq.com/s/kuCaSb1fFdzaUhwsc6KPSA']
#'0528','https://mp.weixin.qq.com/s/PHW04o9E4HKgkGE6wt3suA']
#'0527','https://mp.weixin.qq.com/s/A5CZRqmuMTdmYcZhdIi9rQ']
#'0526','https://mp.weixin.qq.com/s/edhko1xae7do5FhPSER7Qw']
#'0525','https://mp.weixin.qq.com/s/ofoMUIJOQNAtwGXn7Xqr3g']
#'0524','https://mp.weixin.qq.com/s/Zpll7k6wZfJiPNeV8sz6Ig']
#'0523','https://mp.weixin.qq.com/s/-8XvTb6gxkgfNzMxQ_COZw']
#'0522','https://mp.weixin.qq.com/s/FE5FmXxk7180mjqoj9jOSA']
#'0521','https://mp.weixin.qq.com/s/XWA8Pzf0DQ5i92si5Epsgg']
#'0520','https://mp.weixin.qq.com/s/APzs3KMMjfzAZzhypMXAEg']
#'0519','https://mp.weixin.qq.com/s/HIjthO2QrWMs3awazdyI5Q']
#'0518','https://mp.weixin.qq.com/s/rQ385zJfnJQVH1A9TE98TA']
#'0517','https://mp.weixin.qq.com/s/q2BapLzFqFVctV-g9xJYcw']
#'0516','https://mp.weixin.qq.com/s/gnW4IoImldVq9jotw_C1nw']
#'0515','https://mp.weixin.qq.com/s/19BHG_8SUwK07nUeNjc9Dw']
#'0514','https://mp.weixin.qq.com/s/d1qIhfwsisM2jQpfURml3A']
#'0513','https://mp.weixin.qq.com/s/lIMFiBlzIXvju2VV_I4j0g']
#'0512','https://mp.weixin.qq.com/s/YyhqHoMgyetDu6kP9-Ybpw']
#'0511','https://mp.weixin.qq.com/s/i4BwsY-a9zXjkJe-FTea4Q']
#'0510','https://mp.weixin.qq.com/s/V9gNghk8vWinad_VT_YAtg']
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
#'0306','https://wsjkw.sh.gov.cn/xwfb/20220307/6490dbd707674b278f40159595aa5cd9.html'] #首次出现区地址
# '0305','https://wsjkw.sh.gov.cn/xwfb/20220306/ce44bea5ad8e41bf85165cdf35c84bdb.html'] #新增本土0+28
# '0304','https://wsjkw.sh.gov.cn/xwfb/20220305/1fd23e48cc4f479ea8fc56c9e1052759.html'] #新增本土3+16
# '0303','https://wsjkw.sh.gov.cn/xwfb/20220304/164e0c9e7efe41fd91d6eb9e10967cdb.html'] #新增本土2+14
# '0302','https://wsjkw.sh.gov.cn/xwfb/20220303/c44474f0577a4e829896aadf668045b7.html'] #新增本土3+5
# '0301','https://wsjkw.sh.gov.cn/xwfb/20220302/e0c9d63937ed4cfba163c3c97ae05e1d.html'] #新增本土1+1
# '0228','https://wsjkw.sh.gov.cn/xwfb/20220301/b992a70472604bb7b72c86489baa1f7d.html'] #新增本土0+3
# '0227','https://wsjkw.sh.gov.cn/xwfb/20220228/1414e2d0a238477d8ec869c6a060c7b4.html'] #新增本土0+1
# '0226','https://wsjkw.sh.gov.cn/xwfb/20220227/6e6c8939bef34f59abb161cddd0391fb.html'] #新增本土0+1
# '0225','https://wsjkw.sh.gov.cn/xwfb/20220226/9ae3ec12e2484e4b920f5e681c0e15d0.html'] #新增本土0+1
# '0224','https://wsjkw.sh.gov.cn/xwfb/20220225/ff147b9957c34af0847c9ad201122404.html'] #新增本土0+1
# '0206','https://wsjkw.sh.gov.cn/xwfb/20220207/4852ce2f752d46c2a70e4d0b4d711bce.html'] #0207中风险清零
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
# '0404','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654524377&idx=1&sn=b50ea85ec4d5562054027ac55a22e38b&chksm=bd31cea28a4647b4f551c85b41ea01cc787917f6f4c3cf6c3b1408977b570209ce94bb84a131']
# '0403','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654524064&idx=1&sn=8d2e8b5ba80b1f44ae6c900b4304eee3&chksm=bd31cfdb8a4646cd90b686a7d20913c63d9b9516eca3e81be3418a58109309736a4343e7c8c9']
# '0402','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654523814&idx=1&sn=fadbd70496d55b598888393f73b3d2b6&chksm=bd31ccdd8a4645cb94d2dfe51313c7466eafd18cef19268599eea36123922b4105c454b9ac5a']
# '0401','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654523507&idx=1&sn=6f606c580a980252ae28eda6607e1be7&chksm=bd31cd088a46441e073ac309583ee3cff6e764dddd097df24f544d28a4f5142596155b8f7d6b']
# '0331','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654523089&idx=1&sn=e98984c433cdf7371b97b1889d1560aa&chksm=bd31d3aa8a465abc77c698dc3f55b73236d63ae64547c80dcac5c6cdd37c2b77c111af20903b']
# '0330','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654522572&idx=1&sn=296675317f74525a072aa9003baffdbe&chksm=bd31d1b78a4658a16dee2d94543cedd73f14c4927cd90d9b8f57637771e6eb8075959bd118d0']
# '0329','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654522433&idx=1&sn=7c55d1f38d41f388afde2f5e6c6d6e75&chksm=bd31d13a8a46582c2bc466f28366f5140b6404f528c3597e181db67787ff7b3e7596424dbaa4']
# '0328','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654522212&idx=1&sn=707a7e5adf72c2bade3473207509d3fe&chksm=bd31d61f8a465f097416adc882077f8237f0633f26ade099110abb3aa19fae663bec90e442d2']
#'0327','https://mp.weixin.qq.com/s/MfBzdO0bG4fbokKTRCWuIw']
# '0326','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654521587&idx=1&sn=12c3e3429d20f1d801e0c34ab5488e20&chksm=bd31d5888a465c9e0ce61c4a6fb59da5a46e75f0ecfee93929c36a73eeae786e4f28da6f7ded']
# '0325','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654521380&idx=1&sn=7e3a3d3b035cbc7a520278d5ec88571b&chksm=bd31d55f8a465c49df21b35dd5ee2a86d9f6530b9af581e53c8361f6323c95756466966e75b9']
# '0324','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654521097&idx=1&sn=470fce05c7b3d735fc3976f6c6f2ae2f&chksm=bd31da728a465364814e12e970da70dee62ade20e90d273eb25183a77aa0626fff781a0491d7']
# '0323','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520830&idx=1&sn=2e3e7e9a521714c3ff7b4a996ff95d83&chksm=bd31d8858a4651938b338ba2dc62aaa758ff9dd60d7a54c06a48c4917b9ac7b5a72c0901ac13']
# '0322','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520644&idx=1&sn=428742723dd66d56bdf0c5a0a252f37d&chksm=bd31d83f8a4651295d0dcc880d02c25569b5e732283a781c6685a2697855b96023153c0ee7dc']
# '0321','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520388&idx=1&sn=abc2cfa66fafebaa399e345898c117de&chksm=bd31d93f8a46502955728ff97269f071519d7390a40e19b9e3162cd4b544c60028fb6d739a62']
# '0320','http://mp.weixin.qq.com/s?__biz=MjM5NTA5NzYyMA==&mid=2654520238&idx=1&sn=47dd022fb617df72df0a0f486c9278c6&chksm=bd31ded58a4657c3afc7406744c71b2c50e2d204825e4059a13b47abd2e0412dc4cc7485a379']
#'0319','https://mp.weixin.qq.com/s/njMjbpRELpe7SWA7AnB5NA']
#'0318','https://mp.weixin.qq.com/s/xLVPnOTErTe3dmAenUyDGQ']
## no place info before 3/6
## 从3月18日起三天内，我市对非重点区域内人员分时分批次开展一次免费核酸检测
## 从3月13日启动校园封闭管理，5月31日结束本学期授课

day0x2x = {
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

day0529 = {
'浦东新区': 'https://mp.weixin.qq.com/s/yyYQOZcIH5bonYKC09ZJtw', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/yjAd5aD_9Kf1BHnmb-LW3g',
'静安区': 'https://mp.weixin.qq.com/s/biE3ojKp6AiCatp1TjNnQA',
'徐汇区': 'https://mp.weixin.qq.com/s/H-q712YhpURzWPum5UjFOQ',
'长宁区': 'https://mp.weixin.qq.com/s/VQPNne9OP52YMZQ-fBDB7g',
'普陀区': 'https://mp.weixin.qq.com/s/ycaJr5At-bpCelBXqvZ-CA',
'虹口区': 'https://mp.weixin.qq.com/s/fxf5gs8r2_7BRUCyijt1oQ',
'杨浦区': 'https://mp.weixin.qq.com/s/lz8jTrOaLggKIPmEdZOZqA',
'宝山区': 'https://mp.weixin.qq.com/s/GCHp_8wx6ii8vZYjdMvYww',
'闵行区': 'https://mp.weixin.qq.com/s/38_knIEVOK8GyhF3o-RgoA', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/U7xiw8svCy1mrkGUt4X_tQ',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/CUdENMvaQv6YfYfNZzMuiQ',
'青浦区': 'https://mp.weixin.qq.com/s/upJfdSRRuUt0hKjaH58t2Q', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/jeSV9QOPs5l6paPgk8QBuw',
'崇明区': 'https://mp.weixin.qq.com/s/whfG9A7ik-3WMZgDE-mmAg' }

day0528 = {
'浦东新区': 'https://mp.weixin.qq.com/s/Bo2B-jNOSiY72ala5To0og', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/SBu6SVu1KVdU4m40jutWJQ',
'静安区': 'https://mp.weixin.qq.com/s/DQ1xkm8o3jAkR70dBjchnQ',
'徐汇区': 'https://mp.weixin.qq.com/s/P2dPs1rEMCbEfcvgGm_F4g',
'长宁区': 'https://mp.weixin.qq.com/s/eCjtpBIcG_lD6H5kJ2rfLw',
'普陀区': 'https://mp.weixin.qq.com/s/dyesG6DCITjLuDtKX4wZrQ',
'虹口区': 'https://mp.weixin.qq.com/s/rk0xMpbg_2VKeLRRFzO4vw',
'杨浦区': 'https://mp.weixin.qq.com/s/ZUWquB5OLzDOBSSj3Bv1Yw',
'宝山区': 'https://mp.weixin.qq.com/s/wm9aLrY8ukose-lsxDubgg',
'闵行区': 'https://mp.weixin.qq.com/s/J3y2rlXqozB6nwsbb_3-xQ', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/aaotu7mr79OjbuqMIeV4vQ',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/9IuLbAzvIRMNVySfExzI-Q',
'青浦区': 'https://mp.weixin.qq.com/s/dFFdqqktNkv9TLVL-UNceA', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/RyNYBPgKsOZk8l_BgxXeFw',
'崇明区': 'https://mp.weixin.qq.com/s/9zIQ6SYjErh0_et1JELcuw' }

day0527 = {
'浦东新区': 'https://mp.weixin.qq.com/s/_ylKQHmyuP39Xs6IY1ALYA', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/QuW8a8PeYxX5qaMUyy3Kzw',
'静安区': 'https://mp.weixin.qq.com/s/LiZk6Cw3uQm4UT6_0ix-ig',
'徐汇区': 'https://mp.weixin.qq.com/s/giVpmqs7yLPONgUU7uu17g',
'长宁区': 'https://mp.weixin.qq.com/s/dnePF5KjhLrHVUSjnywfRQ',
'普陀区': 'https://mp.weixin.qq.com/s/Wd42x8--V7vlIuffpDswIQ',
'虹口区': 'https://mp.weixin.qq.com/s/Rg1A76_6u7Gn5P2SXm6B7A',
'杨浦区': 'https://mp.weixin.qq.com/s/bUv1ZSytYFDp_h3_2XxSrA',
'宝山区': 'https://mp.weixin.qq.com/s/CIZ1lkX_tARZ24nVIpNWtw',
'闵行区': 'https://mp.weixin.qq.com/s/v1UH-Iz18_1rHcaC7hjTMg', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/EqjNAgYHWIbwJmbXak-eRg',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/9BHIALYLCDFPqxDp-k_PMQ',
'青浦区': 'https://mp.weixin.qq.com/s/EVlW7T404uaK93k76sTjkA', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/1jqSxwTFN8Df2YFRtq0G4A',
'崇明区': 'https://mp.weixin.qq.com/s/SggzloJf15M-IT0QZynRbg' }

day0525 = {
'浦东新区': 'https://mp.weixin.qq.com/s/d5AUpd7EmQI_w4yl6RwIlg', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/dYaFRFv3ujfZ4q520Gj0wA',
'静安区': 'https://mp.weixin.qq.com/s/SyxO5x-NyQncThpTNdNZLw',
'徐汇区': 'https://mp.weixin.qq.com/s/ON1WaHHbINBz_y4q_-jYfQ',
'长宁区': 'https://mp.weixin.qq.com/s/iIGRpdOZbJQbNYbKDGq4pA',
'普陀区': 'https://mp.weixin.qq.com/s/v07CVfl6BXj7AaQ-fj2BLw',
'虹口区': 'https://mp.weixin.qq.com/s/c7UllL_uj2LuCpcQzAVStQ',
'杨浦区': 'https://mp.weixin.qq.com/s/Oo7j7B6msoLuc7PAUhbIlQ',
'宝山区': 'https://mp.weixin.qq.com/s/IkZmngERkOEbozUT7U4IWA',
'闵行区': 'https://mp.weixin.qq.com/s/94XJZ3DBtqa6TFJI9XLOUg', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/4bNFHUEBG3ZfeGL1Jznw7Q',
'金山区': 'https://mp.weixin.qq.com/s/HoQ-D-tJ1bf9e11htBtpHQ',
'松江区': 'https://mp.weixin.qq.com/s/eA_UrBCerl-fZ_oY4p79WQ',
'青浦区': 'https://mp.weixin.qq.com/s/YDJkBmDez_-OeDoTprgwUQ', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/EcfriFVs8j0W7A-_kHE4dw',
'崇明区': 'https://mp.weixin.qq.com/s/dFVRV6N0ETlnzNN6XfIZng' }

day0522 = {
'浦东新区': 'https://mp.weixin.qq.com/s/T0t5dPEOHXyTUxmNVgsWCw', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/NvXZigkgzyArQ_ASzcYLUQ',
'静安区': 'https://mp.weixin.qq.com/s/01Pnw5ba04dsbqzl6BdxdA',
'徐汇区': 'https://mp.weixin.qq.com/s/x-Wgbl5Wq4VswHEpQwyj0A',
'长宁区': 'https://mp.weixin.qq.com/s/dUsBgO62gYGjPGSbv2tIqA',
'普陀区': 'https://mp.weixin.qq.com/s/jlWMnvAF8BYecot-0bi2NQ',
'虹口区': 'https://mp.weixin.qq.com/s/fT_pEuz31aNshll-jlqKAg',
'杨浦区': 'https://mp.weixin.qq.com/s/5DMz0AugUA4VQVczidgOaw',
'宝山区': 'https://mp.weixin.qq.com/s/H573ECdcPI_GEKzty5nT8Q',
'闵行区': 'https://mp.weixin.qq.com/s/uhcRKlLtJkFdpj-6LAYKeQ', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/1Qk6OK-wERATUVsE9GZQsQ',
'金山区': 'https://mp.weixin.qq.com/s/u94QcD38_Dxr8KamX1bizA',
'松江区': 'https://mp.weixin.qq.com/s/CBkSYF9V7Fp138PBV8MmIw',
'青浦区': 'https://mp.weixin.qq.com/s/Qvid27sVL7di8TknFJPjEA', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/Uhc7wOfYg2079xATjf62Nw',
'崇明区': 'https://mp.weixin.qq.com/s/DAj0BN-VyXCm_OBd2zuXTg' }

day0521 = {
'浦东新区': 'https://mp.weixin.qq.com/s/dFidfJSNO3m2eliO-dOESg', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/spHKYQRqra8uU5PQoijbjA',
'静安区': 'https://mp.weixin.qq.com/s/2Zaas-M_Pyf-dqD0yYmC7w',
'徐汇区': 'https://mp.weixin.qq.com/s/Eywcm6jPC5nMpSTpTOk2QA',
'长宁区': 'https://mp.weixin.qq.com/s/VOK4XBsjnhlFLoiheFfCxQ',
'普陀区': 'https://mp.weixin.qq.com/s/lbfavKoWb882Jj_JE4iYgQ',
'虹口区': 'https://mp.weixin.qq.com/s/Bn2rWaEdOkr-Y2R5zLS86g',
'杨浦区': 'https://mp.weixin.qq.com/s/y19ARLsY6lETYIZfZnhrJg',
'宝山区': 'https://mp.weixin.qq.com/s/684PIb-Z1z3jfEvMAaDxlw',
'闵行区': 'https://mp.weixin.qq.com/s/T9ntQmRIrh7CN8RSSi0wzQ', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/vtNlYIb2AOQfWYutH9FosA',
'金山区': 'https://mp.weixin.qq.com/s/yQst6HViNkothQQCpHwNPw', # 反推 检查了4月1日之后的
'松江区': 'https://mp.weixin.qq.com/s/Qw0wx3hiQ8KWsPqvUJOR0g',
'青浦区': 'https://mp.weixin.qq.com/s/jeR7Ixf4nvZ17MSIq6gPog', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/4mpvam5Otvm8km6HT4vOfQ',
'崇明区': 'https://mp.weixin.qq.com/s/bzeHzRNkczaQxwUjKXdTUw' }

day0520 = {
'浦东新区': 'https://mp.weixin.qq.com/s/rvDN5LEoJp1SNMsS7X1Eqg', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/uz9MDgVvigr2vRRdIyN4Pg',
'静安区': 'https://mp.weixin.qq.com/s/TrbXtDs2NA4ex9IaZMX0kw',
'徐汇区': 'https://mp.weixin.qq.com/s/_8XEsr24B9h1vtm9aV2VyA',
'长宁区': 'https://mp.weixin.qq.com/s/Z9hHMufHXRafJ0mcvcwnKA',
'普陀区': 'https://mp.weixin.qq.com/s/P7IC0n14_ipb1jbGULhwzg',
'虹口区': 'https://mp.weixin.qq.com/s/2VyAXZU8f860dCDckwbfmg',
'杨浦区': 'https://mp.weixin.qq.com/s/TBzcX6SRmi3sdaJnT4wcDQ',
'宝山区': 'https://mp.weixin.qq.com/s/MNPJWaHjzSYYMPqJ_e7mtQ',
'闵行区': 'https://mp.weixin.qq.com/s/7I36fAmuhgAL0907bitWnw', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/xqydBO5rcxaBTmCQQb_yWw',
'金山区': 'https://mp.weixin.qq.com/s/tYg0PDyFruEVD0ZrTC4gcQ',
'松江区': 'https://mp.weixin.qq.com/s/qG-ORl6rqQabQ9Be1ydlHQ',
'青浦区': 'https://mp.weixin.qq.com/s/00qVn74lnkCRrd2_gYxxow', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/1Ne_PJKXvPY9dj6Pjsj-FA',
'崇明区': 'https://mp.weixin.qq.com/s/HlJLrICwr4VL1b6YqdYe7Q' }

day0519 = {
'浦东新区': 'https://mp.weixin.qq.com/s/2xz1WJ5R7Nx0v6sQEFMTnQ', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/xv4YCm5_8mHaxh8-Pya3bQ',
'静安区': 'https://mp.weixin.qq.com/s/EDjB7G7NbapgUvT2AJbp-w',
'徐汇区': 'https://mp.weixin.qq.com/s/lLjXWgbjvvRCxY32O43rOg',
'长宁区': 'https://mp.weixin.qq.com/s/ZiNUJXGYIGOswHuyu7hqqg',
'普陀区': 'https://mp.weixin.qq.com/s/2RozWVnCCNpr5lLFzQZyAA',
'虹口区': 'https://mp.weixin.qq.com/s/Yv0YuNRsnkSlmQoNhNQFHQ',
'杨浦区': 'https://mp.weixin.qq.com/s/xo5Eflg9BiQAVKjS44FNvw',
'宝山区': 'https://mp.weixin.qq.com/s/1fppPDqcL3h_DBqPIbkhjw',
'闵行区': 'https://mp.weixin.qq.com/s/TKW11owAyOhCF_xOzaNjuw', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/FpYoZ_IXMUCSPj4XsRjSBQ',
'金山区': 'https://mp.weixin.qq.com/s/1yi3LuZTZ0Nb1EXaYoKMng',
'松江区': 'https://mp.weixin.qq.com/s/hIIJdNUCmjRHpMbY6JfDmA',
'青浦区': 'https://mp.weixin.qq.com/s/fYWI0vz15hm14sIphz1eSQ', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/ubppdt0wI2JRC-UKsCsthQ',
'崇明区': 'https://mp.weixin.qq.com/s/JdDJs1g6_2sl5s4JvSKmLw' }

day0518 = {
'浦东新区': 'https://mp.weixin.qq.com/s/dKOcL5W6qJwOlUd0VTTVNQ', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/Iv2-UKwul6l-1xewanwyQw',
'静安区': 'https://mp.weixin.qq.com/s/pAIuLM_iuUlsUj_pR0vTRA',
'徐汇区': 'https://mp.weixin.qq.com/s/Rzof0E8MPxDq824V3mbD3Q',
'长宁区': 'https://mp.weixin.qq.com/s/qY2N7XII4OxaskyOimS6qw',
'普陀区': 'https://mp.weixin.qq.com/s/chTLmsUBGC4fVyAR35192A',
'虹口区': 'https://mp.weixin.qq.com/s/MBIdJzTjwvrgs-EAwpNZew',
'杨浦区': 'https://mp.weixin.qq.com/s/_JUU0B3tEek3d2TsAbdv2w',
'宝山区': 'https://mp.weixin.qq.com/s/6wzy3MxzpBvgQRdk6jTkIw',
'闵行区': 'https://mp.weixin.qq.com/s/QRQ_jet26z7d-2ckibbRZQ', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/KtWn9zD4n3fXLdLAPadzZg',
'金山区': 'https://mp.weixin.qq.com/s/hwpY9tACteauy_-PoeYYZA',
'松江区': 'https://mp.weixin.qq.com/s/Z-wQKqtbzD2fUAd6r-Emuw',
'青浦区': 'https://mp.weixin.qq.com/s/9YkWp3h5tNO0INa8uPWX0A', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/1iqbysiFxfUsUC-gsorevA',
'崇明区': 'https://mp.weixin.qq.com/s/aHxZoWwjb2b30XFj2Gl-kQ' }

day0517 = {
'浦东新区': 'https://mp.weixin.qq.com/s/HzNCRH9s6PEnQbuAYuYN3w', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/MoBw2czZTXcGbjxDsNPC1w',
'静安区': 'https://mp.weixin.qq.com/s/vNOHpR9a-7_aSZtJlv8Zfg',
'徐汇区': 'https://mp.weixin.qq.com/s/FOJcvSvn0nEXU7GlqULqaA',
'长宁区': 'https://mp.weixin.qq.com/s/LQXH-yVOWCzDmHJEE9yPRw',
'普陀区': 'https://mp.weixin.qq.com/s/6061EQ9_1ZDM6u3U2bHFng',
'虹口区': 'https://mp.weixin.qq.com/s/YHvpzgI0aIHGzEbDJENMsg',
'杨浦区': 'https://mp.weixin.qq.com/s/SbOOQuP5BMz-KxHOAPJPCg',
'宝山区': 'https://mp.weixin.qq.com/s/1K98DVM2BvwmZ6UlXF1JPQ',
'闵行区': 'https://mp.weixin.qq.com/s/DZmr41Nik0iKdk6odh5KRQ', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/fNYGP8Cb6Ooz5IaVlVv3bg',
'金山区': 'https://mp.weixin.qq.com/s/xH7bsdWp-Nf1JYTo4-B9WA',
'松江区': 'https://mp.weixin.qq.com/s/U6MRSphsxP_SLXX7BTgswg',
'青浦区': 'https://mp.weixin.qq.com/s/FIgNcxcP1GzxAmW2PsksWw', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/3xu28JQxrDaCYfK6EBY-oA',
'崇明区': 'https://mp.weixin.qq.com/s/NILTzIVeoYc35a1LJEGTQw' }

day0514 = {
'浦东新区': 'https://mp.weixin.qq.com/s/rgGTNinnNGKFOmtCS5nGpQ', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/F4vLNus4DY1IYYLEMzNVgQ',
'静安区': 'https://mp.weixin.qq.com/s/PCSn0NJ5eyVckeApVTaiNw',
'徐汇区': 'https://mp.weixin.qq.com/s/Gw6WqR01uQNCNIAdMHUNHw',
'长宁区': 'https://mp.weixin.qq.com/s/_opF_nkJ1wdbYk5ThBkpeA',
'普陀区': 'https://mp.weixin.qq.com/s/eQdn_gV3KSB1XoX_oFgcwQ',
'虹口区': 'https://mp.weixin.qq.com/s/Ptnd2bc0Dt0LPsf3timHYQ',
'杨浦区': 'https://mp.weixin.qq.com/s/lXBH3hGs574TrzEFg9y-6Q',
'宝山区': 'https://mp.weixin.qq.com/s/F07oGa4YJyq8mxMDyGFDgg',
'闵行区': 'https://mp.weixin.qq.com/s/VRNAfCoAOgXA_BRCmDEDRg', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/4FdPLlfsCyqzIF-IWW-wLw',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/BEU1Wf1FFl4TCxBIGdwnng',
'青浦区': 'https://mp.weixin.qq.com/s/67zTH05kuHKkPTkdC7NU5w', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/5Ekh0lyIb6pXTK-_7XUL9g',
'崇明区': 'https://mp.weixin.qq.com/s/V6an8Xa-lOLXIOZf1RwKhg' }

day0513 = {
'浦东新区': 'https://mp.weixin.qq.com/s/bsALQdI41d_RFiS9eiJAQg', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/2Q2CIEmvEEywaet9lbZ2qQ',
'静安区': 'https://mp.weixin.qq.com/s/zsbCsxns0nLTYxGVKdv0_A',
'徐汇区': 'https://mp.weixin.qq.com/s/2gfmMMcBj2WIVezDbQHZxg',
'长宁区': 'https://mp.weixin.qq.com/s/gj7kSRq8U9p1zRWTFu4M7g',
'普陀区': 'https://mp.weixin.qq.com/s/0wFVYaFiJ2UjAa-GTkha6A',
'虹口区': 'https://mp.weixin.qq.com/s/NOcgGCwC9gYln2EskZd4BQ',
'杨浦区': 'https://mp.weixin.qq.com/s/nxf5Bxfpu2NImlQT1eAarA',
'宝山区': 'https://mp.weixin.qq.com/s/NBCcjC8JPgzN-sEYyWyH8w',
'闵行区': 'https://mp.weixin.qq.com/s/e9RhbA_GRlj1hxkBIiGV2g', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/SUGnc5l8PscdDjK7wyS4IA',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/rjfp3yTTL2f3vuo0OvtFlw',
'青浦区': 'https://mp.weixin.qq.com/s/nh9C04QcAB5EuJcn9-Kxzw', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/_QLqFIfY18iaRnmSkXvKcA',
'崇明区': 'https://mp.weixin.qq.com/s/Ot-4bFNfR-1_4u2BAOHzWA' }

day0512 = {
'浦东新区': 'https://mp.weixin.qq.com/s/k-cU1TRrg7uvqvucuIIzhg', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/HZ05OzoN3NaekXzjLZmOYA',
'静安区': 'https://mp.weixin.qq.com/s/hKcuDIouQPMSezAPNk2EYw',
'徐汇区': 'https://mp.weixin.qq.com/s/SXJxXjypFg_929Zvs40afA',
'长宁区': 'https://mp.weixin.qq.com/s/-DRmxjKzSD5ZnJHdqrGGuQ',
'普陀区': 'https://mp.weixin.qq.com/s/ntFJdeGulEu5L0vwp-Dcog',
'虹口区': 'https://mp.weixin.qq.com/s/triwjjimQVfnHeSnrRM3bQ',
'杨浦区': 'https://mp.weixin.qq.com/s/byR-wdlKHgMGJxOfpM2xcA',
'宝山区': 'https://mp.weixin.qq.com/s/ENYHtEmEgAts920VW5aBjQ',
'闵行区': 'https://mp.weixin.qq.com/s/6RXAAU90rZB_scsyTzp-1w', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/654nzaUv92vdAf3C4cWTHw',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/lKykWzAY5VRKfC7EVkC46Q',
'青浦区': 'https://mp.weixin.qq.com/s/F3jdgXji3DM5Iv2F7lIXPg', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/HeCDLJId226fdiEQzd_9ig',
'崇明区': 'https://mp.weixin.qq.com/s/CS6ykiSZ6F4H3m-T-YmzoQ' }

day0511 = {
'浦东新区': 'https://mp.weixin.qq.com/s/quvJbSPMMJPgm_tvL5QHTg', # 浦东发布
'黄浦区': 'https://mp.weixin.qq.com/s/c8kLCfnKDbBcnBd-P0GLZw',
'静安区': 'https://mp.weixin.qq.com/s/tv9adeb3Iv8SzJsA_Lj05w',
'徐汇区': 'https://mp.weixin.qq.com/s/q1ijPTbqa4OaFT17EnaaUA',
'长宁区': 'https://mp.weixin.qq.com/s/ba_ss54xA2dpOg1e0iFaZA',
'普陀区': 'https://mp.weixin.qq.com/s/19MkLbJy2ChTtXjtTaqiNA',
'虹口区': 'https://mp.weixin.qq.com/s/HRNwyTx2J48LksJGWZsK8Q',
'杨浦区': 'https://mp.weixin.qq.com/s/Wk1WcuxmWdn-2-TJGN6rdg',
'宝山区': 'https://mp.weixin.qq.com/s/UjOkuA51zmqRdqhXHxbH9w',
'闵行区': 'https://mp.weixin.qq.com/s/Yf2cx5I9UK1mBKE6dQ551g', # 今日闵行
'嘉定区': 'https://mp.weixin.qq.com/s/-b8DPzz4gX-sdXpDy8DbgQ',
'金山区': '',
'松江区': 'https://mp.weixin.qq.com/s/QPpTt54kOy_OV9PLUcTa4Q',
'青浦区': 'https://mp.weixin.qq.com/s/P6B4Zcs5_7WUtsXHQVFsUg', # 绿色青浦
'奉贤区': 'https://mp.weixin.qq.com/s/Aql6VsMHIN74bKHS0IUpqQ',
'崇明区': 'https://mp.weixin.qq.com/s/jbugkxd2Hdtrlg9PMnKdEg' }

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
'金山区': 'https://mp.weixin.qq.com/s/RnVphrJDFPpnAccLD4RB8g',
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
            wx_ = wx.find('div', {'id' : 'img-content'}).get_text("\n", strip=True)
            if wx_.find('%s月%s日' % (int(z[0][:2]), int(z[0][2:])) ) < 0:
                print('day%s %s的链接没有有效日期' % (z[0],zz0[i]) )
                raise
            try:
                spl = re.findall(r'\d+例本土无症状感染者', wx_)
                if len(spl) >= 1:
                    spl0 = wx_.split(spl[0])
                    if len(spl0) == 2:
                        wxx += '\n\n\n\n%s' % spl0[0]
                        wxx += '\n\n\n\n%s' % spl0[1].split( spl[0].replace('例本土','例') )[-1]
                    else:
                        wxx += '\n\n\n\n%s\n\n\n\n%s' % (spl0[0], spl0[-1])
                else:
                    spl = re.findall(r'\d+例无症状感染者', wx_)
                    spl0 = wx_.split(spl[0])
                    if len(spl0) < 3:
                        wxx += '\n\n\n\n%s' % wx_
                    else:
                        wxx += '\n\n\n\n%s\n\n\n\n%s' % (spl0[0], spl0[-1])
            except:
                wxx += '\n\n\n\n%s' % wx_
            # 32例本土无症状感染者
            # 32例无症状感染者
elif z[1].endswith('.html'):
    import os
    if not os.path.isfile('shanghaifabu/%s%s.txt' % (z[0],z[0])):
        os.system('scrapy fetch --nolog %s > %s%s.txt' % (z[1], z[0],z[0]) )
    f = open('shanghaifabu/%s%s.txt' % (z[0],z[0]), 'r')
    page = f.read()
    f.close()
    pp = BeautifulSoup(page, features="lxml").find('div', {'id' : 'ivs_content'}).get_text("\n", strip=True)
    ppp = re.findall(r'，居住于(\S{2,3}区[^，。]+)', pp) + re.findall(r'，居住地为(\S{2,3}区[^，。]+)', pp)
    print('就读于', re.findall(r'，就读于(\S{2,3}区[^，。]+)', pp) )
    print('外省市', re.findall(r'，外省市([^，。]+)', pp) )
    print('搜到区地址个数', len(ppp))
    #print('\n'.join(ppp) )
    print('搜到新增本土数', '+'.join( re.findall('24时，新增本土[^0-9]+(\d{1,3})', pp)[1:]) )
    wxx = re.sub(r'(\S{2,3})区', r'\1区,', '\n'.join(ppp) )
else:
    import os
    if not os.path.isfile('html-files/%s.htm' % z[0]):
        print( z[1] )
        os.system('scrapy fetch --nolog %s > html-files/%s.htm' % (z[1], z[0]) )
    f = open('html-files/%s.htm' % z[0], 'r')
    page = f.read()
    f.close()
    wx = BeautifulSoup(page, features="lxml")
    #wx = BeautifulSoup(request.urlopen(z[1]).read(), features="lxml")
    wxx = wx.find('div', {'id' : 'img-content'}).get_text("\n", strip=True)
res = wxx.replace('，', ',').replace('。', ',').replace('、', ',').replace('；', ',').replace(';', ','
        ).replace(' ', ',').replace('\t', ','
        ).replace('分别居住于', ',').replace('：', ','
        ).replace('我区', ',,,,').replace('已对相关', ',')

#Z = [ s.strip() for s in list(filter(None, res.split(',') )) ]
Z = [ s.strip() for s in filter(None, res.split(',') ) ]
#print(len(Z))
for zz in Z:
    #if len( zz.strip() ) > 20: # 5/18 金山区 5/26 关闭长度提醒
    #    print('%s\n' % zz.strip() )
    if zz.find('成功') > -1 or zz.find('目前') > -1:
        print('## 成功 | 目前\n%s\n' % re.sub(r'\s', '', zz) )
    if zz.find('住宅小区') > -1:
        print('## 住宅小区 \n%s\n' % re.sub(r'\s', '', zz) )
    if zz.find('当前中风险等级地区') > -1:
        print('## 中风险 \n%s\n' % re.sub(r'\s', '', zz) )
print(z[1])
if not z[1]:
    print('###           shanghaifabu')
    print('# shanghaifabu 如用请补一行')
    print('###           shanghaifabu')
    fz = open('%s%s.txt' % (z[0],z[0]), 'w')
else:
    fz = open('%s.txt' % z[0], 'w')
fz.write( u'\n'.join(Z) )
fz.close()
print('CAUTION: please check %s.txt for missing line break' % z[0] )