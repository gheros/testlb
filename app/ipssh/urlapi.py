import urllib

def _request_(param):
    url ="https://dnsapi.cn/Info.Version -d 'login_token=9a2e50dabb92eda52d8d5828bfa2c1a3&format=json'"
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print(data)
    print("接口调用完成")
    return data

print(_request_)


import urllib


test_data = 'login_token=login_token=40101,9a2e50dabb92eda52d8d5828bfa2c1a3&format=json'
test_data_urlencode = urllib.urlencode(test_data)

requrl = "https://dnsapi.cn/Info.Version"
data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)
page = request.urlopen(req).read()
page = page.decode('utf-8')



req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res