import configparser
import os

conf = configparser.ConfigParser()  # 类的实例化
curpath = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(curpath, 'cfg.ini')
conf.read(path, encoding="utf-8")
value = conf['select']['path']
print(value)