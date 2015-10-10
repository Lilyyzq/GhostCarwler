#-*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import requests
import poster
import re
import os
import time

def upload_img(cj,path,ticket,token):		
	opener = poster.streaminghttp.register_openers()  
	opener.add_handler(urllib2.HTTPCookieProcessor(cj))		
	datagen,headers = multipart_encode({'file':open(path,'rb')})
	#print datagen
	#print headers
	uploadUrl = 'https://mp.weixin.qq.com/cgi-bin/filetransfer?action=upload_material&f=json&writetype=doublewrite&groupid=1&ticket_id=xiuseyizhan&ticket=' + ticket + '&token=' + token + '&lang=zh_CN'
	req3 = urllib2.Request(uploadUrl,datagen,headers)
	req3.add_header('Accept','*/*')
	req3.add_header('Accept-Encoding','gzip, deflate')
	req3.add_header('Accept-Language','en-US,en;q=0.8')
	req3.add_header('Connection','keep-alive')
	#req3.add_header('Content-Length','1385')
	#req3.add_header('Content-Type','multipart/form-data; boundary=----WebKitFormBoundaryFap8PGqwcplNlhxA')
	#req3.add_header('Cookie','noticeLoginFlag=1; pgv_pvi=1648069632; noticeLoginFlag=1; data_bizuin=3075402655; data_ticket=AgVpzO8C20Hjd9sf8kIap89tAwGUiiXJsIcGa0T+qNU=; slave_user=gh_e59bae02ed96; slave_sid=ZEVxS2tINkloOUJ6Sjl2MVZoN3U4WlFLZ09aQTdKZWZrZ2ZlSUhONHJha1BXMW9vR1JBQ3VWcms2U0hibmpySENId1U5SVZ1eENIZ1B4ZmtkSkFidFdYZmx5bWF1NzVhTEdCcGpoQV9jNnBXalJOWjhIamRJcjZNRVlqMWttdUs=; bizuin=3272065571')
	req3.add_header('Host','mp.weixin.qq.com')
	req3.add_header('Origin','https://mp.weixin.qq.com')
	Referer = 'https://mp.weixin.qq.com/cgi-bin/filepage?type=2&begin=0&count=12&t=media/img_list&token=' + token + '&lang=zh_CN'
	req3.add_header('Referer',Referer)
	req3.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
	while 1:
		try:
			ret3 = urllib2.urlopen(req3)
			break
		except urllib2.HTTPError,e:
			print str(e)
		except urllib2.URLError,e:
			print str(e)			
	print ret3.read()
	

cj = cookielib.LWPCookieJar()
print cj
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

print cj
paras = {'username':'strwolf@163.com','pwd':'76a22e07a46aea62ef5b6cfd11191c46','imgcode':'','f':'json'}
req = urllib2.Request('https://mp.weixin.qq.com/cgi-bin/login',urllib.urlencode(paras))
req.add_header('Accept','*/*')
req.add_header('Accept-Encoding','gzip, deflate')
req.add_header('Accept-Language','en-US,en;q=0.8')
req.add_header('Connection','keep-alive')
req.add_header('Content-Length','79')
req.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
#req.add_header('Cookie','noticeLoginFlag=1; pgv_pvi=1648069632; noticeLoginFlag=1')
req.add_header('Host','mp.weixin.qq.com')
req.add_header('Origin','https://mp.weixin.qq.com')
req.add_header('Referer','https://mp.weixin.qq.com/')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
req.add_header('X-Requested-With','XMLHttpRequest')
ret = urllib2.urlopen(req)
retread = ret.read()
retcontent = json.loads(retread)
print retcontent['base_resp']['err_msg']
RedirectUrl = retcontent['redirect_url']
#token = RedirectUrl.split('token=')[1]
token = retcontent['redirect_url'][44:]
print token

print cj
paras2 = {'token':token,'lang':'zh_CN','f':'json','ajax':1,'random':0.3910328117199242,'type':1,'content':'中文测试','tofakeid':'2302469181','imgcode':''}
#print paras2
msgUrl = 'https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&f=json&token=' + token + '&lang=zh_CN'
Referer = 'https://mp.weixin.qq.com/cgi-bin/singlesendpage?t=message/send&action=index&tofakeid=2302469181&token=' + token + '&lang=zh_CN'
req2 = urllib2.Request(msgUrl,urllib.urlencode(paras2))
req2.add_header('Accept','application/json, text/javascript, */*; q=0.01')
req2.add_header('Accept-Encoding','gzip, deflate')
req2.add_header('Accept-Language','en-US,en;q=0.8')
req2.add_header('Connection','keep-alive')
#req2.add_header('Content-Length','130')
req2.add_header('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
#req2.add_header('Cookie','noticeLoginFlag=1; pgv_pvi=1648069632; data_bizuin=3075402655; data_ticket=AgVzD9024FGFJJqdeNC/QnaGAwHaBavJhzBklHevKJo=; noticeLoginFlag=1; slave_user=gh_e59bae02ed96; slave_sid=UnBITHBiMDFGQUM4WktlWUhwTnZrM2FCVzJJUlZPMHJzNDA3ajFLN0FaeUpEellLV3FTYktSVmNPU0UwWGhSTEhzSXNLdmJDeDFJek9DR3FQdjJqZlFFT3FEbGFKNkxQSmx3aUZLYVZxSXd1enRYSW1aWkRpU3pGOXdtVkxiUDA=; bizuin=3272065571')
req2.add_header('Host','mp.weixin.qq.com')
req2.add_header('Origin','https://mp.weixin.qq.com')
req2.add_header('Referer',Referer)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
req2.add_header('X-Requested-With','XMLHttpRequest')
ret2 = urllib2.urlopen(req2)
print ret2.read()



ticketUrl = 'https://mp.weixin.qq.com/cgi-bin/filepage?type=2&begin=0&count=12&t=media/img_list&token=' + token + '&lang=zh_CN'
Referer_ticket = 'https://mp.weixin.qq.com/cgi-bin/appmsg?begin=0&count=10&t=media/appmsg_list&type=10&action=list_card&lang=zh_CN&token=' + token
req_ticket = urllib2.Request(ticketUrl)
req_ticket.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
#req_ticket.add_header('Accept-Encoding','gzip, deflate, sdch')
req_ticket.add_header('Accept-Language','en-US,en;q=0.8')
req_ticket.add_header('Connection','keep-alive')
req_ticket.add_header('Host','mp.weixin.qq.com')
req_ticket.add_header('Referer',Referer_ticket)
req_ticket.add_header('Upgrade-Insecure-Requests',1)
req_ticket.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36')
ret_ticket = urllib2.urlopen(req_ticket)
page = ret_ticket.read()
re1 = r'ticket:"(.+?)"'
ticket_re = re.compile(re1)
ticket = re.findall(ticket_re,page)
print ticket[0]









#register_openers()
#获取图片路径
file_name = os.listdir(os.getcwd())
folder_name=[]
for fn in file_name:
	if os.path.isdir(fn):
		folder_name.append(fn)

for folder in folder_name:
	#在每个文件夹下找到图片名的集合
	sub_dir = os.path.join(os.getcwd(),folder)
	img_name = os.listdir(sub_dir)
	#print img_name
	for img in img_name:
		up_dir = os.path.join(sub_dir,img)
		#print up_dir
		upload_img(cj,up_dir,ticket[0],token)
		time.sleep(1)


