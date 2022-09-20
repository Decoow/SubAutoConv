import requests 
import configparser

conf=configparser.ConfigParser()

conf.read("./config.ini")

courls= conf.options('clash')
vourls = conf.options('mixed')

for ourl in courls:
                type = 'clash'
                url = conf.get(type, ourl)
                api = conf.get('common','api')
                endurl = r'target='+type+r'&url='+url

                # 目标链接
                tarurl = api+endurl
                r = requests.get(tarurl,allow_redirects=True)
                
                filepath = "./sub/clash/"+ourl+'.yaml' 
                with open(filepath, "wb") as code:
                        code.write(r.content)

                print(tarurl) 


for ourl in vourls:
                type = 'mixed'
                url = conf.get(type, ourl)
                api = conf.get('common','api')
                endurl = r'target='+type+r'&url='+url

                # 目标链接
                tarurl = api+endurl
                r = requests.get(tarurl,allow_redirects=True)
                
                filepath = "./sub/v2/"+ourl+'.txt' 
                with open(filepath, "wb") as code:
                        code.write(r.content)

                print(tarurl) 

