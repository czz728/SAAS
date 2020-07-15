import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler

from common.config import myconf
from conf.constant import cons

log_level = myconf.get('LOG','log_level')
sh_level = myconf.get('LOG','sh_level')
fh_level = myconf.get('LOG','fh_level')
date = time.localtime()
date_name = '_'.join([str(date.tm_year), str(date.tm_mon), str(date.tm_mday)])
log_file_name = date_name + '.log'



class  MyLog():
        def __new__(cls, *args, **kwargs):
            # 一：创建日志收集器对象
            mylog = logging.getLogger("mylog")
            mylog.setLevel(log_level)
            # 二：创建日志输出渠道
            # 1、输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(sh_level)
            # 2、输出到文件
            # fh = logging.FileHandler()
            # 日志轮转
            # 按时间间隔轮转
            fh = TimedRotatingFileHandler(filename=os.path.join(cons.LOG_PATH,log_file_name), when='D', interval=1, backupCount=2, encoding='utf8' )
            fh.setLevel(fh_level)
            # 按文件大小轮转
            # 8bit=1bytes(字节)，1024字节=1kb,1024kb=1mb,1024mb=1GB
            # fh = RotatingFileHandler(filename='D:\API\logs\log.log', mode='a', maxBytes=1024*1024*20, backupCount=2, encoding='utf8')
            # 三：将日志收集器对象和日志输出渠道绑定
            mylog.addHandler(fh)
            mylog.addHandler(sh)
            # 四：设置日志输出格式
            formatter = logging.Formatter("%(asctime)s -- [%(filename)s-->%(funcName)s-->line:%(lineno)d] - %(levelname)s: %(message)s")
            # 将日志输出格式和日志输出渠道绑定
            sh.setFormatter(formatter)
            fh.setFormatter(formatter)

            return mylog

log = MyLog()

# log.debug('---debug等级日志，一般用于调试')
# log.info('---info等级日志，常规信息的输出')
# log.warning('---warning等级日志，警告信息')
# log.error('---error等级日志，错误信息')
# log.critical('---critical等级日志，严重错误，程序要崩溃')


