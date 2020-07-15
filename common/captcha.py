#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

from conf.constant import cons

"""通过第三方平台超级鹰识别验证码
注意：需要注册平台账号，收费识别成功一次1分钱
"""


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,}
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',}


    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()


    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()



def get_captcha():
    """获取验证码"""
    # username, password超级鹰平台的用户名和密码，soft_id==》超级鹰>>用户中心>>软件ID 生成一个替换
    chaojiying = Chaojiying_Client('zydx728', 'dengyun20200604','15d13c8f659c84fd7379a0ea04e622bb')
    im = open(cons.CAPTCHA_PATH, 'rb').read()  # 验证码截图本地文件路径
    captcha = chaojiying.PostPic(im,1902)['pic_str']  # 1902 验证码类型  官方网站>>价格体系
    return captcha




