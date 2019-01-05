from scrapy.cmdline import execute
import os
import sys


#得到main文件的路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#执行命令scrapy crawl jobbole
execute(['scrapy', 'crawl', 'jobbole'])
