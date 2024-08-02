import json
import random
import time

import requests

def get_new_ip():
    ip_api_url = "http://v2.api.juliangip.com/dynamic/getips?auto_white=1&num=1&pt=1&result_type=text&split=1&trade_no=1288076745950119&sign=6416670a5837d30576ac8913f96fef18"
    response = requests.get(ip_api_url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception(f"Failed to fetch IP: {response.status_code}")

# 将Cookie字符串
def parse_cookie_string(cookie_string):
    cookies = {}
    for item in cookie_string.split('; '):
        if '=' in item:
            key, value = item.split('=', 1)
            cookies[key] = value
    return cookies


# 设置请求头
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://prodev.m.jd.com',
    'Referer': 'https://prodev.m.jd.com/mall/active/4RBT3H9jmgYg1k2kBnHF8NAHm7m8/index.html?cu=true&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001264867_&utm_term=ad1d5b582cd7483c9b7302fdb16204fd&preventPV=1&forceCurrentView=1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/126.0.0.0'
}

# 提供的Cookie字符串
cookie_1 = '''shshshfpa=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; shshshfpx=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; jcap_dvzw_fp=aWDiG0w3vbXOad_P1AAPQph64DqNwbze59w280AcnJGgnOFTTJ30-AzERQQaNFYT7PSqqks_bcdH40iTdjv3Nw==; __jdu=17178085403861917072205; TrackID=1xvkNaBPTzyhPs3SgJD_wQTy9nWM3Qg4EkJHYSbF-jxieaE0XJTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcy9PXLGBmIg1O9TITsIMVEhtRwlmlJ4eGF9g9kx3hs_G8S; pinId=LSHQBcNvtzrumTqZbZboCw; whwswswws=; 3AB9D23F7A4B3C9B=6IFHPLLS6L5VWEZXAGHDUFEDUTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcUFUICY5YIQSGA3YM52PWK7257DQDGD4; areaId=21; ipLoc-djd=21-1836-0-0; PCSYCityID=CN_360000_360300_0; mba_muid=17178085403861917072205; wxa_level=1; cid=9; jxsid=17212897646850511218; appCode=ms0ca95114; webp=1; __jdc=76161171; visitkey=5408506319593022841; TrackerID=qH9sOl_fbpA4-SlJ1gTEgCWGVScWAmR6kBA7skqx_BYtSUB9XkwLqzUJp1GPk36vwQwDkF0IbNmlhZV5cM4okULly6bVjjDm6WQI_VSX0DVnA-SGQBWxmFLuerWrlqFGlCcM5Y8P92ifjZ7vwLKDOQ; pt_key=AAJmmM6YADC0okkBux11GH0LWMdQHvVZ1pK9Vs98LewxAe6AnsuPuIF8B0Noo_ux1ywG1HxbwfM; pt_pin=jd_CFyGpvOhmTRo; pt_token=bvqwzi8v; pwdt_id=jd_CFyGpvOhmTRo; sfstoken=tk01mc0cd1c64a8sMisyeDErMXgzmYeSkU6C2Ni7+TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc4w0lWv3JIud548wyz; sbx_hot_h=null; sc_width=375; language=zh_CN; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; retina=1; autoOpenApp_downCloseDate_jd_homePage=1721304177829_1; jxsid_s_u=https%3A//so.m.jd.com/ware/search.action; downloadAppPlugIn_downCloseDate=1721304308832_86400000; rurl=%2F%2Fwq.jd.com%2Fpinbind%2Fpintokenredirect%3Ftype%3D1%26biz%3Djm-business-center%26rurl%3Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fcommon%252FsaveWqToken%253Furl%253Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fsign%252FsignActivity%253FactivityId%253D276b7ea5ea794d02957882a0da83164e%2526venderId%253D1000000864%26scope%3D0%26sceneid%3D9001%26btnTips%3D%26hideApp%3D0; b_webp=1; b_avif=1; jxsid_s_t=1721304603197; warehistory="100098552521,100102708034,"; __wga=1721304608642.1721304146348.1721296409732.1721290471708.9.3; PPRD_P=UUID.17178085403861917072205-LOGID.1721306413050.1890921497; RT="z=1&dm=jd.com&si=3m1732qecil&ss=lyr9ekhc&sl=1&tt=jh&ld=1sc&ul=84p&hd=84w"; __jda=76161171.17178085403861917072205.1717808540.1721306413.1721359456.13; autoOpenApp_downCloseDate_auto=1721359457132_1800000; unpl=JF8EAJ9nNSttXk4AVRsEHRsTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLclVdWBRKER9vbxRUXlNKVA4fBysSEHtdVV9dC0wSCmhhNWRVUCVUSBtsGHwTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcVJfWwtIFgdfZjVUW2h7ZAQrAysTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcF5VWm0JexQ; mba_sid=17213594564031916255067002852.3; 3AB9D23F7A4B3CSS=jdd036IFHPLLS6L5VWEZXAGHDUFEDUTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcUFUICY5YIQSGA3YM52PWK7257DQDGD4AAAAMQZETVCGYAAAAACZDS4MJT4FSXHYX; _gia_d=1; __jdb=76161171.5.17178085403861917072205|13.1721359456; __jdv=76161171%7Ckong%7Ct_1001264867_%7Cjingfen%7C74ea177824d04b17a1dd53a99b8e7435%7C1721361717639; b_dw=375; b_dh=667; b_dpr=2.0000000298023224; joyytokem=babel_2DWXWszt6VvNx4HDctSa4TA7rHh6MDFQZkNIazk5MQ==.YVFxeVhmV3R5UmJSdDYuaVYicQpmES4aFWFKdWRafFc9ehVhGAEJGwgFegVfJh81HippVzQRHR8oAn4aEiEmJl0ENm4SNBIKGwoMIVIXcRMaVxMsMTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcoFwkeOWQnPTY=.966bf643; shshshfpb=BApXcG_YvyvVA91wYvONA6qBGen6TP-Z_BlXBgq4S9xJ1PdZfQqXwiz37mgTyPrJBfNWWtadi8qJVR4A; __jd_ref_cls=Babel_dev_other_sign; joyya=1721361717.1721361739.59.0jl3uxe'''
cookie_2 = '''shshshfpa=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; shshshfpx=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; jcap_dvzw_fp=aWDiG0w3vbXOad_P1AAPQph64DqNwbze59w280AcnJGgnOFTTJ30-AzERQQaNFYT7PSqqks_bcdH40iTdjv3Nw==; __jdu=17178085403861917072205; TrackID=1xvkNaBPTzyhPs3SgJD_wQTy9nWM3Qg4EkJHYSbF-jxieaE0XJTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcy9PXLGBmIg1O9TITsIMVEhtRwlmlJ4eGF9g9kx3hs_G8S; pinId=LSHQBcNvtzrumTqZbZboCw; whwswswws=; 3AB9D23F7A4B3C9B=6IFHPLLS6L5VWEZXAGHDUFEDUTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcUFUICY5YIQSGA3YM52PWK7257DQDGD4; areaId=21; ipLoc-djd=21-1836-0-0; PCSYCityID=CN_360000_360300_0; mba_muid=17178085403861917072205; wxa_level=1; cid=9; jxsid=17212897646850511218; appCode=ms0ca95114; webp=1; __jdc=76161171; visitkey=5408506319593022841; TrackerID=qH9sOl_fbpA4-SlJ1gTEgCWGVScWAmR6kBA7skqx_BYtSUB9XkwLqzUJp1GPk36vwQwDkF0IbNmlhZV5cM4okULly6bVjjDm6WQI_VSX0DVnA-SGQBWxmFLuerWrlqFGlCcM5Y8P92ifjZ7vwLKDOQ; pt_key=AAJmmM6YADC0okkBux11GH0LWMdQHvVZ1pK9Vs98LewxAe6AnsuPuIF8B0Noo_ux1ywG1HxbwfM; pt_pin=jd_CFyGpvOhmTRo; pt_token=bvqwzi8v; pwdt_id=jd_CFyGpvOhmTRo; sfstoken=tk01mc0cd1c64a8sMisyeDErMXgzmYeSkU6C2Ni7+TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc4w0lWv3JIud548wyz; sbx_hot_h=null; sc_width=375; language=zh_CN; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; retina=1; autoOpenApp_downCloseDate_jd_homePage=1721304177829_1; jxsid_s_u=https%3A//so.m.jd.com/ware/search.action; downloadAppPlugIn_downCloseDate=1721304308832_86400000; rurl=%2F%2Fwq.jd.com%2Fpinbind%2Fpintokenredirect%3Ftype%3D1%26biz%3Djm-business-center%26rurl%3Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fcommon%252FsaveWqToken%253Furl%253Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fsign%252FsignActivity%253FactivityId%253D276b7ea5ea794d02957882a0da83164e%2526venderId%253D1000000864%26scope%3D0%26sceneid%3D9001%26btnTips%3D%26hideApp%3D0; b_webp=1; b_avif=1; jxsid_s_t=1721304603197; warehistory="100098552521,100102708034,"; __wga=1721304608642.1721304146348.1721296409732.1721290471708.9.3; PPRD_P=UUID.17178085403861917072205-LOGID.1721306413050.1890921497; RT="z=1&dm=jd.com&si=3m1732qecil&ss=lyr9ekhc&sl=1&tt=jh&ld=1sc&ul=84p&hd=84w"; unpl=JF8EAJ9nNSttCB5UUB9RHxsTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLclVdWBRKER9vbxRUXVNIUQ4bBSsSEHtdVV9dC0wSCmhhNWRVUCVUSBtsGHwTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcVJfWwtIFgdfZjVUW2h7ZAQrAysTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcF5VWm0JexQ; __jda=76161171.17178085403861917072205.1717808540.1721306413.1721359456.13; mba_sid=17213594564031916255067002852.1; 3AB9D23F7A4B3CSS=jdd036IFHPLLS6L5VWEZXAGHDUFEDUTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcUFUICY5YIQSGA3YM52PWK7257DQDGD4AAAAMQZECNZ3AAAAAADVH5GO2NRFSOWAX; _gia_d=1; autoOpenApp_downCloseDate_auto=1721359457132_1800000; __jdb=76161171.2.17178085403861917072205|13.1721359456; __jdv=76161171%7Ckong%7Ct_1001264867_%7Cjingfen%7Cad1d5b582cd7483c9b7302fdb16204fd%7C1721359460407; b_dw=375; b_dh=667; b_dpr=2.0000000298023224; joyytokem=babel_4RBTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcDk5MQ==.W1ZQYntfWFZleV1YVS0NWFlRJiUAWQQeNltNVH95RlAcYTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc5KCYHPX4+MU8JFygNOhEvG1U0ajAgUDI3EgwwEws/AxtRZCUNNRsDOiAjBB0fPRUDNSYUHw==.33f129b3; shshshfpb=BApXcJHgMyvVA91wYvONA6qBGen6TP-Z_BlXBgq4U9xJ1PdZfQqXwiz37mgTyPrJBfNWWtafn; __jd_ref_cls=Babel_dev_other_sign; joyya=1721359460.1721359465.59.0z0h88u'''
cookie_3 = '''shshshfpa=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; shshshfpx=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; jcap_dvzw_fp=aWDiG0w3vbXOad_P1AAPQph64DqNwbze59w280AcnJGgnOFTTJ30-AzERQQaNFYT7PSqqks_bcdH40iTdjv3Nw==; __jdu=17178085403861917072205; TrackID=1xvkNaBPTzyhPs3SgJD_wQTy9nWM3Qg4EkJHYSbF-jxieaE0XJTl1KsGSSd2bv3cvZLL2it38JHCAlI5HVD9y9PXLGBmIg1O9TITsIMVEhtRwlmlJ4eGF9g9kx3hs_G8S; pinId=LSHQBcNvtzrumTqZbZboCw; whwswswws=; 3AB9D23F7A4B3C9B=6IFHPLLS6L5VWEZXAGHDUFEDUTWXLJMC342PWTO5WVKAWYEDLIVZQQJNIODUFUICY5YIQSGA3YM52PWK7257DQDGD4; areaId=21; ipLoc-djd=21-1836-0-0; PCSYCityID=CN_360000_360300_0; mba_muid=17178085403861917072205; wxa_level=1; cid=9; jxsid=17212897646850511218; appCode=ms0ca95114; webp=1; __jdc=76161171; visitkey=5408506319593022841; TrackerID=qH9sOl_fbpA4-SlJ1gTEgCWGVScWAmR6kBA7skqx_BYtSUB9XkwLqzUJp1GPk36vwQwDkF0IbNmlhZV5cM4okULly6bVjjDm6WQI_VSX0DVnA-SGQBWxmFLuerWrlqFGlCcM5Y8P92ifjZ7vwLKDOQ; pt_key=AAJmmM6YADC0okkBux11GH0LWMdQHvVZ1pK9Vs98LewxAe6AnsuPuIF8B0Noo_ux1ywG1HxbwfM; pt_pin=jd_CFyGpvOhmTRo; pt_token=bvqwzi8v; pwdt_id=jd_CFyGpvOhmTRo; sfstoken=tk01mc0cd1c64a8sMisyeDErMXgzmYeSkU6C2Ni7+Tc4SjZjY9tKyPI21h5aZARyMrpi7rzIa704w0lWv3JIud548wyz; sbx_hot_h=null; sc_width=375; language=zh_CN; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; retina=1; autoOpenApp_downCloseDate_jd_homePage=1721304177829_1; jxsid_s_u=https%3A//so.m.jd.com/ware/search.action; downloadAppPlugIn_downCloseDate=1721304308832_86400000; rurl=%2F%2Fwq.jd.com%2Fpinbind%2Fpintokenredirect%3Ftype%3D1%26biz%3Djm-business-center%26rurl%3Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fcommon%252FsaveWqToken%253Furl%253Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fsign%252FsignActivity%253FactivityId%253D276b7ea5ea794d02957882a0da83164e%2526venderId%253D1000000864%26scope%3D0%26sceneid%3D9001%26btnTips%3D%26hideApp%3D0; b_webp=1; b_avif=1; jxsid_s_t=1721304603197; warehistory="100098552521,100102708034,"; __wga=1721304608642.1721304146348.1721296409732.1721290471708.9.3; PPRD_P=UUID.17178085403861917072205-LOGID.1721306413050.1890921497; RT="z=1&dm=jd.com&si=3m1732qecil&ss=lyr9ekhc&sl=1&tt=jh&ld=1sc&ul=84p&hd=84w"; unpl=JF8EAJ9nNSttC0xdBB9WGEcZTlwDW11dTh8AbTAEVllfHFIASAoSEEB7XlVdWBRKER9vbxRUWVNJXQ4YCisSEHtdVV9dC0wSCmhhNWRVUCVUSBtsGHwTBhAZbl4IexYzb2EFUlRZQlAAGgASFRBDXVJfWwtIFgdfZjVUW2h7ZAQrAysTIAAzVRNdDksRCm5uAVFcWkJTBRMCHRMWSF5VWm0JexQ; __jda=76161171.17178085403861917072205.1717808540.1721359456.1721374708.14; mba_sid=17213747085691715939717853598.1; 3AB9D23F7A4B3CSS=jdd036IFHPLLS6L5VWEZXAGHDUFEDUTWXLJMC342PWTO5WVKAWYEDLIVZQQJNIODUFUICY5YIQSGA3YM52PWK7257DQDGD4AAAAMQZHWZQYIAAAAADP6J5ZL54QAXYYX; _gia_d=1; autoOpenApp_downCloseDate_auto=1721374709645_1800000; __jdb=76161171.2.17178085403861917072205|14.1721374708; __jdv=76161171%7Ckong%7Ct_1001264867_%7Cjingfen%7Cb6805e2d840f41d4923f0356f74b983a%7C1721374732831; b_dw=375; b_dh=667; b_dpr=2.0000000298023224; joyytokem=babel_3S28janPLYmtFxypu37AYAGgivfpMDF6dHptTTk5MQ==.S0NIXH5NQE1eeU1GTRMIETc2XnlPRTFYM0tYTEF8VkUEXzNLCjgsPSIXFho/Fg0MOwxDRQ00OzU6O1s8ODMfA3suJFc3EjgYIi8qC0AoVDUwRSoJFxwlCzU6Ew5JWiAdIAM9PzA2HCMaLQAbCSRCBTA7H041BBM=.e6085dfc; shshshfpb=BApXcKWzlyvVA91wYvONA6qBGen6TP-Z_BlXBgq4Q9xJ1PdZfQqXwiz37mgTyPrJBfNWWtadi8qJVR4A; __jd_ref_cls=Babel_dev_other_sign; joyya=1721374732.1721374738.59.1s8mj4p'''
cookie_4 = '''shshshfpa=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; shshshfpx=b801f208-4ea4-ae5e-128f-130928f957a5-1717808581; jcap_dvzw_fp=aWDiG0w3vbXOad_P1AAPQph64DqNwbze59w280AcnJGgnOFTTJ30-AzERQQaNFYT7PSqqks_bcdH40iTdjv3Nw==; __jdu=17178085403861917072205; TrackID=1xvkNaBPTzyhPs3SgJD_wQTy9nWM3Qg4EkJHYSbF-jxieaE0XJTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcy9PXLGBmIg1O9TITsIMVEhtRwlmlJ4eGF9g9kx3hs_G8S; pinId=LSHQBcNvtzrumTqZbZboCw; whwswswws=; 3AB9D23F7A4B3C9B=6IFHPLLS6L5VWEZXAGHDUFEDUTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcUFUICY5YIQSGA3YM52PWK7257DQDGD4; areaId=21; ipLoc-djd=21-1836-0-0; PCSYCityID=CN_360000_360300_0; mba_muid=17178085403861917072205; wxa_level=1; cid=9; jxsid=17212897646850511218; appCode=ms0ca95114; webp=1; __jdc=76161171; visitkey=5408506319593022841; TrackerID=qH9sOl_fbpA4-SlJ1gTEgCWGVScWAmR6kBA7skqx_BYtSUB9XkwLqzUJp1GPk36vwQwDkF0IbNmlhZV5cM4okULly6bVjjDm6WQI_VSX0DVnA-SGQBWxmFLuerWrlqFGlCcM5Y8P92ifjZ7vwLKDOQ; pt_key=AAJmmM6YADC0okkBux11GH0LWMdQHvVZ1pK9Vs98LewxAe6AnsuPuIF8B0Noo_ux1ywG1HxbwfM; pt_pin=jd_CFyGpvOhmTRo; pt_token=bvqwzi8v; pwdt_id=jd_CFyGpvOhmTRo; sfstoken=tk01mc0cd1c64a8sMisyeDErMXgzmYeSkU6C2Ni7+TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc4w0lWv3JIud548wyz; sbx_hot_h=null; sc_width=375; language=zh_CN; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; retina=1; autoOpenApp_downCloseDate_jd_homePage=1721304177829_1; jxsid_s_u=https%3A//so.m.jd.com/ware/search.action; downloadAppPlugIn_downCloseDate=1721304308832_86400000; rurl=%2F%2Fwq.jd.com%2Fpinbind%2Fpintokenredirect%3Ftype%3D1%26biz%3Djm-business-center%26rurl%3Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fcommon%252FsaveWqToken%253Furl%253Dhttps%253A%252F%252Fcjhy-isv.isvjcloud.com%252Fsign%252FsignActivity%253FactivityId%253D276b7ea5ea794d02957882a0da83164e%2526venderId%253D1000000864%26scope%3D0%26sceneid%3D9001%26btnTips%3D%26hideApp%3D0; b_webp=1; b_avif=1; jxsid_s_t=1721304603197; warehistory="100098552521,100102708034,"; __wga=1721304608642.1721304146348.1721296409732.1721290471708.9.3; PPRD_P=UUID.17178085403861917072205-LOGID.1721306413050.1890921497; RT="z=1&dm=jd.com&si=3m1732qecil&ss=lyr9ekhc&sl=1&tt=jh&ld=1sc&ul=84p&hd=84w"; __jda=76161171.17178085403861917072205.1717808540.1721359456.1721374708.14; autoOpenApp_downCloseDate_auto=1721374709645_1800000; joyytokem=babel_3S28janPLYmtFxypu37AYAGgivfpMDF6dHptTTk5MQ==.S0NIXH5NQE1eeU1GTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcgsPSIXFho/Fg0MOwxDRQ00OzU6O1s8ODMfA3suJFc3EjgYIi8qC0AoVDUwRSoJFxwlCzU6Ew5JWiAdIAM9PzA2HCMaLQAbCSRCBTA7H041BBM=.e6085dfc; joyya=1721374732.1721375461.58.01jcnxr; 3AB9D23F7A4B3CSS=jdd036IFHPLLS6L5VWEZXAGHDUFEDUTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcUFUICY5YIQSGA3YM52PWK7257DQDGD4AAAAMQZH4TNUAAAAAADMJKXEAQSFHWVEX; _gia_d=1; unpl=JF8EAJ9nNSttUE5VBhtQSxRAGFVRW10AGB8EbjMEXVhZHgdVHwUZRRJ7XlVdWBRKER9vbxRUWVNPVA4ZASsSEHtdVV9dC0wSCmhhNWRVUCVUSBtsGHwTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcVJfWwtIFgdfZjVUW2h7ZAQrAysTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcF5VWm0JexQ; mba_sid=17213747085691715939717853598.5; cartNum=20; __jdb=76161171.6.17178085403861917072205|14.1721374708; __jdv=76161171%7Ckong%7Ct_1001264867_%7Cjingfen%7C94021ca7ab94419b960e0840dba563f3%7C1721375495528; b_dw=375; b_dh=667; b_dpr=2.0000000298023224; cartLastOpTime=1721375497; shshshfpb=BApXcbwnxyvVA91wYvONA6qBGen6TP-Z_BlXBgq4Q9xJ1PdZfQqXwiz37mgTyPrJBfNWWtadi8qJVR4A; __jd_ref_cls=Babel_dev_other_sign'''
cookie_5 = ''''''

# 设置多个账号的cookies
cookies_list = [
    parse_cookie_string(cookie_1),
    parse_cookie_string(cookie_2),
    parse_cookie_string(cookie_3),
    parse_cookie_string(cookie_4),
]

# 设置请求的data
data_list = [
    {
        "appid": "babelh5",
        "body": {
            "sourceCode": "acetttsign",
            "encryptProjectId": "4S2AbgQzWsZRaPieo6H87H9QdBTe",
            "encryptAssignmentId": "4AkNcU2XKqbEAdptFV9arNrPqxQL",
            "completionFlag": 'true',
            "itemId": "1",
            "extParam": {
                "forceBot": "1",
                "businessData": {
                    "random": "RynYH4jm"
                },
                "signStr": "1721359466603~1k96V1GY5PgMDFqYWJTSDk5MQ==.W1ZQYntfWFZleV1YVS0NWFlRJiUAWQQeNltNVH95RlAcYTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc5KCYHPX4+MU8JFygNOhEvG1U0ajAgUDI3EgwwEws/AxtRZCUNNRsDOiAjBB0fPRUDNSYUHw==.33f129b3~1,1~71497324F344AF9B9B02C870ED8E7BC051D63744~09c4k55~C~TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcwBCHMZBh4FCAQZQxIZGlACGgd6FAEBGwQEbxgEGQAFCBhBFW0ZGlNHWRIPCRgXREMXAhYEAAIECwEMAwYFCw0FAAUAABYZFUdQXBYPFURBTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcZFU14XAm8BBhwHDAQZBQUZCQYZBBwEZRgXXVoXAgUZFVNGGg4XBgRRCwJRVlEBDgAHBAgCWlcDB1ZWXFUDAVUDDgQHAVIXFBZbRxIPGmNcWQMHGhgXQxIPCQMHBgMAAQADAQYFCxgXXVsXAhZUFRwXXkRXFQoXenVFb1N/cFN4TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcxtelNEA2UMQH4EZ1RvXmVEb0dcQgcCWldhQWRHfXJTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcxoXGxJbWUIXDRJWGhgXRFNHGg5uAQYCFAcCAm0ZGkZaFQpuGlUXGxJUGhgXVhIZGlUXGxJUGhgXVhIZGlUXahwXUVtUFQoXXlJTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcQUbChYZFVNTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcm19A1pYGhgXWloXAm8EGwAZCGkZFVJZV1MXDRJUGhgXWkNSGg4XVhJI~0h221tz",
                "sceneid": "babel_4RBT3H9jmgYg1k2kBnHF8NAHm7m8"
            },
            "activity_id": "4RBT3H9jmgYg1k2kBnHF8NAHm7m8",
            "template_id": "00019605",
            "floor_id": "105891269",
            "enc": "0431F5489541F2AEBADF1FCA5FA4DCBEB9804C0FC1BA1229EA2B3AAB43C95DB43E514A969F5D97F59569030643A850354BF23DC63E6B4B12713B018DD9D32553"
        },
        "sign": '11',
        "t": '1721359465667'
    },
    {
        "appid": "babelh5",
        "body": {
            "sourceCode": "acetttsign",
            "encryptProjectId": "3b3eCQtp6QpSP7SASCPQMbW3Y6Ff",
            "encryptAssignmentId": "2adXGHCEQyKuvG2K7rQffGkGKNjv",
            "completionFlag": 'true',
            "itemId": "1",
            "extParam": {
                "forceBot": "1",
                "businessData": {
                    "random": "Jiw85cR5"
                },
                "signStr": "1721361740334~1ucwpe9jsE7MDFQZkNIazk5MQ==.YVFxeVhmV3R5UmJSdDYuaVYicQpmES4aFWFKdWRafFc9ehVhGAEJGwgFegVfJh81HippVzQRHR8oAn4aEiEmJl0ENm4SNBIKGwoMIVIXcRMaVxMsMTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcoFwkeOWQnPTY=.966bf643~1,1~79EAA32F939D7F58FCB9C70C30A22EB45AC073FD~1jn2eme~C~TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc1xf2caBh8GBgAaQxMaFFQBGgkAGgZgG3Z9fBwHGQEGBhxCFWwaFFdEWRMMBxwUREIUDBIHAAMHBQYHAAABDgcCAgMGABIaFUZTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLckVCQlAUGhJGU18UDGsDAR0DBgEaBQQaBwIaBR0HaxwUXVsUDAEaFVJFFAoUBgVSBQZSVlACAAQEBAkBVFMAB1dVUlEAAVQAAAAEAVMUGhJYRxMMFGdfWQIEFBwUQxMMBwcEBgIABwcCBwIFAhwUXVoUDBJXFR0UUEBUFQsUdHFGb1JxaWlATQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc1udFdHA2IPTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcdhQ1BSXwhHfWdkAnEUGxNYQBIMFXZZWVdaUhF/WFMYFR0UWFFAFQsUVRIaFUJVRBIMbAcAARwFAARrGhJEWBMMbRJXFR0UVxIaFVAUGhJXFR0UVxIaFVAUGhJXFWwaFFlZVhMMFFZQUVdQUERCFR0UV1oUDRNDFBwUVFgUDBJBBB8DGAIUGxNVUG9AFQsUDwkUGxNUUhIMFUNXWFRZWgx8X0cOAlJkAxIaFVxcFAptBh0GGgBrGxNUWl9RFQsUVxIaFVxFURIMFVAUSw==~1jn59jq",
                "sceneid": "babel_2DWXWszt6VvNx4HDctSa4TA7rHh6"
            },
            "activity_id": "2DWXWszt6VvNx4HDctSa4TA7rHh6",
            "template_id": "00019605",
            "floor_id": "107544264",
            "enc": "EE9D28C22E838CDEAB430A4B4CA444F515D98600E45377CAFE2BC6CF024A9D8BD5AC7D40435A9825686C8B00E4A4D4F2DCFDCA0A887989ECA31E3E5C796FE4F3"
        },
        "sign": "11",
        "t": "1721361739377"
    },
    {
        # "functionId": "doInteractiveAssignment",
        "appid": "babelh5",
        "body": {
            "sourceCode": "acetttsign",
            "encryptProjectId": "3xxdfoHPKSyuwryhhEX8en1ZAT6A",
            "encryptAssignmentId": "csYHwSFWAjtcuxyYXpZYSecsH6P",
            "completionFlag": 'true',
            "itemId": "1",
            "extParam": {
                "forceBot": "1",
                "businessData": {
                    "random": "sY1nU5f2"
                },
                "signStr": "1721374739292~1L9b3i1Est1MDF6dHptTTk5MQ==.S0NIXH5NQE1eeU1GTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcgsPSIXFho/Fg0MOwxDRQ00OzU6O1s8ODMfA3suJFc3EjgYIi8qC0AoVDUwRSoJFxwlCzU6Ew5JWiAdIAM9PzA2HCMaLQAbCSRCBTA7H041BBM=.e6085dfc~1,1~4200A9A3DB13513A083868BD6743972BD10E6539~1c87gaq~C~TQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcwMBA0UBh4IBAgUQxIUFlwPGggJGA0NGwQKAxQJGQAIBBRMFW0UFl9KWRICBRQaREMaDhoJAAIJBw8MAAMKDQwOBQIPBhoUFUddUBoCFURMQF5MQ1ZeFhQaQFVZFgIaUVZMQE1MQlEaGBpIU14aDmMMABwKDAEUBQUUBQoUBRwJaRQaXVoaDgkUFVNLFgIaBgRcBw5cVlEMAgwKBAgPVlsOB1ZbUFkOAVUOAggKAVIaGBpWRxICFm9RWQMKFhQaQxICBQ8KBgMPAA8LDgIBBhQaXVsaDhpZFRwaUkhaFQoadnlIb1NzY0JUTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLcxgdl9JA2EBTQ8419uEC2UaRX7itXEQBGMDPvrmRgnZLc9vQ1FcXQBJfWZqAHkaGxJWQhoCFXdXW19UUhBxWlsWFRwaWllOFQoaVxoUFUNbRhoCbAYOAxQLAAVlGBpKWBICbxpZFRwaVRoUFVEaGBpZFRwaVRoUFVEaGBpZFW0UFlFXVhICFl5eUVZeUkxMFRwaVVIaDRJNFhQaVFkaDhpPBB4NGgoaGxJbUmdOFQoaDQEaGxJaUBoCFUJZWlxXWg1LbQlWYgVeBhoUFV1SFgJjBhwIGAhlGxJaWFdfFQoaVRoUFV1LUxoCFVEaSQ==~18x3nah",
                "sceneid": "babel_3S28janPLYmtFxypu37AYAGgivfp"
            },
            "activity_id": "3S28janPLYmtFxypu37AYAGgivfp",
            "template_id": "00019605",
            "floor_id": "100946655",
            "enc": "C1B9C77BFE2A5FBE7E63802784C8CEA840A5D2C95D0FDED1306B529C41E10CA177915857298E447E0B8CBF565C0BD03C716D79F6BF5A4F38295E00B7A1E3428C"
        },
        "sign": "11",
        "t": "1721374738241"
    },
    {
      "appid": "babelh5",
      "body": {
        "sourceCode": "acetttsign",
        "encryptProjectId": "cLL8ubm28wZ2kSs4YEq4rf61tFa",
        "encryptAssignmentId": "2aZUnxTZKBb8pYQQtiEqGYELvvB4",
        "completionFlag": 'true',
        "itemId": "1",
        "extParam": {
          "forceBot": "1",
          "businessData": {},
          "signStr": "-1",
          "sceneid": "babel_4RYbb8NtVAegmT35SuM2N3KKYLWt"
        },
        "activity_id": "4RYbb8NtVAegmT35SuM2N3KKYLWt",
        "template_id": "00035605",
        "floor_id": "106061428",
        "enc": "082F6E6EB76A8CBEE15FCF7E92519D4A0C14A052EDB9C9248A0F4121699403D3BD36268425A591B4168556839656A0E7B71133FE4AECBA7E880BCF8B32A5BA27"
      },
      "sign": "11",
      "t": "1721375502754"
    },

]

# 遍历每个账号的cookies和data并发送请求
for cookies, data in zip(cookies_list, data_list):
    time.sleep(random.uniform(7,10))

    headers['Cookie'] = '; '.join([f"{key}={value}" for key, value in cookies.items()])
    headers['X-Forwarded-For'] = get_new_ip()

    # 扁平化 message 字典
    flattened_data = {
        "appid": data['appid'],
        "body": json.dumps(data['body']),  # 将嵌套的字典转换为 JSON 字符串
        "sign": data['sign'],
        "t": data['t']
    }

    response = requests.post(
        url='https://api.m.jd.com/client.action?functionId=doInteractiveAssignment',
        headers=headers,
        data=flattened_data  # 使用扁平化后的表单数据
    )

    # 打印响应内容
    print(f"Status code for account {cookies['pt_pin']}: {response.status_code}")
    print(response.json())
