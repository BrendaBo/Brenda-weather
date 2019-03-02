import requests
import re
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://movie.douban.com/chart", headers=headers)
pattern = re.compile('<p class="ul"></p>.*?nbg.*?title="(.*?)">.',re.S)
items = re.findall(pattern, r.text)
for item in items:
    print(item)