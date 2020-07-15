
from configparser import ConfigParser
from conf.constant import cons
import os

# 开关配置文件的路径
env_file_path = os.path.join(cons.CONF_PATH, 'env.ini')

class MyConfig(ConfigParser):
    """读取配置文件的类"""

    def __init__(self):
        super().__init__()

        c = ConfigParser()
        c.read(env_file_path,encoding='utf8')
        switch = c.getint('env','switch')
        # 根据开关的值，分别去读取不同环境的配置文件
        if switch == 1:
            self.read(os.path.join(cons.CONF_PATH,'conf.ini'), encoding='utf8')
        elif switch == 2:
            self.read(os.path.join(cons.CONF_PATH,'conf1.ini'),encoding='utf8')
        else:
            self.read(os.path.join(cons.CONF_PATH,'conf2.ini'),encoding='utf8')


myconf = MyConfig()
