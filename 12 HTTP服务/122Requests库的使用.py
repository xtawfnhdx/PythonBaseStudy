import requests
r = requests.get("http://httpbin.org/get")
print(r)
print(r.text)

payload = {'page': '1', 'per_page': '10'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.text)
print(r.url)

payload = {'page': 1, 'per_page': 10}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)



url = 'http://httpbin.org/post'
payload = {'page': 1, 'per_page': 10}
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

r = requests.post("http://httpbin.org/post", json=payload, headers=headers)
print(r.request.headers)


urls = 'http://exmaple.com/some/cookie/setting/url'
r = requests.get(urls)
print(r.cookies['some_key'])
