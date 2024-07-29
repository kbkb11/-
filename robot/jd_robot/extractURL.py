import re
import time

def extract_http_urls(text):
    # 定义正则表达式模式来匹配以 http: 或 https: 开头的 URL
    pattern = r'https?://[^\s"]+'
    # 使用正则表达式查找所有匹配的 URL
    urls = re.findall(pattern, text)
    return urls

text='''
开启更多功能，提升办公效能
没有上限店铺签到
循环签到

https://u.jd.com/ebZW7Mt

https://u.jd.com/eiZWkxE

https://u.jd.com/ezZWjoM

https://u.jd.com/ebZWjxy

https://u.jd.com/euZWfiA

https://u.jd.com/eqZW5ZO

https://u.jd.com/eQZWhIv

https://u.jd.com/eQZWlru

https://u.jd.com/ezZWH34

https://u.jd.com/eqZWUxt

https://u.jd.com/eqZWkeu

https://u.jd.com/eiZW9AH

https://u.jd.com/esZWHKM

https://u.jd.com/e8ZWcOZ

https://u.jd.com/ebZWRWO

https://u.jd.com/esZWxPw

啕宝签到??7天最高666元

http://navo.top/QRNRfa

http://navo.top/3aMZRz

店铺签到

七???新增

7天50豆,15天150豆,30天300豆-亿色

https://suz011.kuaizhan.com/?44l0xW

3天3豆,5天5豆,7天10豆-澳诺

https://suz011.kuaizhan.com/?4kvB3V

7天50豆-洁柔

https://suz011.kuaizhan.com/?3wEe2E

15天15豆-路酒

https://suz011.kuaizhan.com/?2mJNBA

28天50豆,30天实物-王小卤

https://suz011.kuaizhan.com/?vAIYMY

14天100豆-哈根达斯

https://suz011.kuaizhan.com/?20cV4U

20天29豆-九阳

https://suz011.kuaizhan.com/?4aOfI3

————7.3————

5天800豆-健安喜

https://suz011.kuaizhan.com/?1Yssi7

?10天10豆-荷美尔

https://suz011.kuaizhan.com/?3o8V2r

?10天5豆,25天15豆-西麦

https://suz011.kuaizhan.com/?31gmtD

?15天3豆,25天5豆-骁龙

http://navo.top/eQjmIr

?20天实物-古井贡酒

https://suz011.kuaizhan.com/?1n84Zf

————7.2————

15/30天实物-劲牌

https://suz011.kuaizhan.com/?esNuxY

————7.1————

签到7天抽50/100豆-雀巢咖啡

http://navo.top/veyMvy

签到抽200/30豆/实物-闪迪大师

https://suz011.kuaizhan.com/?Iphu1Y

1-7天共50豆-馥蕾诗

https://suz011.kuaizhan.com/?2FEpnK

7天100豆-多加多母婴

https://suz011.kuaizhan.com/?3lmPkw

7天20豆-三星自营

https://suz011.kuaizhan.com/?2zNJzI

7天20豆-卫龙

https://suz011.kuaizhan.com/?1rRnpw

7天20豆-朗仕

https://suz011.kuaizhan.com/?1gfW3p

7天10豆-PICO

https://suz011.kuaizhan.com/?1jdLPJ

7天10豆-纪梵希

https://suz011.kuaizhan.com/?yteJOY

7天10豆-安慕希

https://suz011.kuaizhan.com/?4cJos5

7天10豆-伊利牛奶官方

https://suz011.kuaizhan.com/?3gVBrW

7天10豆-苏酒双沟

https://suz011.kuaizhan.com/?1XKOeA

7天10豆-普丽普莱

https://suz011.kuaizhan.com/?1SFFlh

7天5豆-金典

https://suz011.kuaizhan.com/?sZs1ZY

7天5豆-盛宝

https://suz011.kuaizhan.com/?1CzAbm

7天5豆-雅觅

https://suz011.kuaizhan.com/?1XJDRp

7天5豆-苏菲

https://suz011.kuaizhan.com/?40BpIO

7天5豆-三元官方

https://suz011.kuaizhan.com/?166QqV

7天实物-方回春堂

https://suz011.kuaizhan.com/?1WhZxq

8天100豆-悦鲜活自营

https://suz011.kuaizhan.com/?28TfDc

8天20豆-悦鲜活官方

https://suz011.kuaizhan.com/?2GnsQW

10天10豆-安视优

http://navo.top/f6vMJb

10天5豆-倩碧

http://navo.top/yIZ32m

15天1000豆-皇家

http://navo.top/ZZfAVn

15天500豆-惠氏

http://navo.top/vmQNBf

15天10豆-进口超市

https://suz011.kuaizhan.com/?1Ozes9

18天50豆-红星

https://suz011.kuaizhan.com/?13UTj2

20/25/29天??-李宁

https://suz011.kuaizhan.com/?30dPIm

20天100豆-毛铺

https://suz011.kuaizhan.com/?2yCTeu

20天99豆,25天实物-自然堂

https://suz011.kuaizhan.com/?TvKghY

20天20豆,30天50豆-万家乐

https://suz011.kuaizhan.com/?2xI165

20天10豆-天梭自营

https://suz011.kuaizhan.com/?3c3GRs

20天10豆-爱乐维

https://suz011.kuaizhan.com/?1ALSKC

20天10豆,30天20豆-澳佳宝

https://suz011.kuaizhan.com/?3MPYpL

20天10豆,30天20豆-MichaelKors

https://suz011.kuaizhan.com/?12ZGuo

20天5豆,30天10豆-福临门

https://suz011.kuaizhan.com/?nBSKlY

20/30天实物-宾三得利

https://suz011.kuaizhan.com/?1y88IU

21天5000豆-爱他美官方

https://suz011.kuaizhan.com/?4q24Ff

21天5000豆-爱他美海外

https://suz011.kuaizhan.com/?3pz7XI

21天20豆-达仁堂

https://suz011.kuaizhan.com/?3hC16R

21天实物-高露洁

https://suz011.kuaizhan.com/?1XfARa

21天/30天实物-百草味

https://suz011.kuaizhan.com/?3WBncz

22天3豆,30天5豆-九芝堂

https://suz011.kuaizhan.com/?3exohs

23天实物-黛珂

https://suz011.kuaizhan.com/?3OmXA5

24天25豆,30天实物-百雀羚①

http://navo.top/6JBBVn

25天5e卡-君乐宝乳品

https://suz011.kuaizhan.com/?3BiwTT

25天300豆-杰士邦

https://suz011.kuaizhan.com/?nRo9JY

25天100豆-芬兰蔚优

https://suz011.kuaizhan.com/?s9NGOY

25天30豆-第六感

https://suz011.kuaizhan.com/?41Xx4y

25天20豆,30天50豆-李锦记

https://suz011.kuaizhan.com/?pxx1cY

25天10豆-天梭官方

https://suz011.kuaizhan.com/?4fQ25z

25天10豆-欧康维视

https://suz011.kuaizhan.com/?1TEE48

25天5豆-北极清水

https://suz011.kuaizhan.com/?4nG3mZ

25天实物-悦木之源

https://suz011.kuaizhan.com/?1odT3N

28天50豆-忆江南

https://suz011.kuaizhan.com/?2z25Fq

30天1000豆-雀巢成人

http://navo.top/yEvyE3

30天50豆-伊藤园自营

https://suz011.kuaizhan.com/?1dYVm4

30天50豆-伊藤园旗舰

https://suz011.kuaizhan.com/?3zGvyZ

30天50豆-青花郎

https://suz011.kuaizhan.com/?2PjvIG

30天50豆-博朗

http://navo.top/JZvmIf

30天50豆-百雀羚②

http://navo.top/BZfaUz

30天45豆-珠江自营

https://suz011.kuaizhan.com/?xJo06Y

30天30豆-三生花

http://navo.top/e2MjAz

30天30豆-诺优能

http://navo.top/Y7Zvq2

30天30豆-爱他美自营

http://navo.top/yURvUf

30天30豆-徐福记

https://suz011.kuaizhan.com/?4qwJek

30天20豆-好来

http://navo.top/JvmMji

30天10豆-李氏大药厂

https://suz011.kuaizhan.com/?2SJNUd

30天实物-源究所

https://suz011.kuaizhan.com/?tTJE3Y

30天实物-滋源

https://suz011.kuaizhan.com/?33KDdh

30天实物-口子窖

https://suz011.kuaizhan.com/?2Q4ulO

30天实物-狮王

https://suz011.kuaizhan.com/?DhbzeY

30天实物-黄天鹅

https://suz011.kuaizhan.com/?mcXFtY

31天20豆-CURRENTBODY

https://suz011.kuaizhan.com/?H5NFcY

31天实物-蒙牛低温

https://suz011.kuaizhan.com/?rn2hxY

六???未完

16天100豆-bebetour

https://suz011.kuaizhan.com/?4wUm9i

?20天10豆,31天Plus年卡-鱼跃

https://suz011.kuaizhan.com/?1eUjBq







十八万四千六百六十二  阅举报
'''

urls = extract_http_urls(text)
for i in range(len(urls)):
    print(urls[i])