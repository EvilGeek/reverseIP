import requests, time, os, threading, socket, re, urllib3, sys, random
from bs4 import BeautifulSoup

urllib3.disable_warnings()
from flask import *

app=Flask(__name__)
app.secret_key="blabkajajs82"

@app.route("/")
def home():
    return render_template("vindex.html")
@app.route("/api")
def api():
    ip=request.args.get("ip")
    print(ip)
    if ip:
        data=reverse(ip)
        print(data)
        if data==None:
            return jsonify(status=False, data=None)
        elif data==[]:
            return jsonify(status=False, data=None)
        else:
            return jsonify(status=True, data=data)
    else:
        return jsonify(status=False, data=None)

def reverse(ip):
    data=[]
    d1=t1(ip)
    d2=t2(ip)
    d3=t3(ip)
    d4=t4(ip)
    for i in d1:
        if i not in data and "google" not in i and "cloudflare" not in i:
            data.append(i)
    for i in d2:
        if i not in data and "google" not in i and "cloudflare" not in i:
            data.append(i)
    for i in d3:
        if i not in data and "google" not in i and "cloudflare" not in i:
            data.append(i)
    for i in d4:
        if i not in data and "google" not in i and "cloudflare" not in i:
            data.append(i)
    return data

def t3(ip):
    u="https://domains.yougetsignal.com/domains.php"
    h={
    "Host": "domains.yougetsignal.com",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "dnt": "1",
    "sec-ch-ua-mobile": "?1",
    "user-agent": getUA(),
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "x-prototype-version": "1.6.0",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://www.yougetsignal.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.yougetsignal.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-IN,en;q\u003d0.9"
        
    }
    post="remoteAddress="+ip+"&key=&_="
    req=requests.post(u, headers=h, data=post, verify=False).json()
    #print(req)
    reip=[]
    if req.get("status")=="Success":
        d=req.get("domainArray")
    for j in d:
        reip.append(j[0])
    if reip!=[]:
        return reip
    else:
        return []


def t2(ip):
    url = "https://mip.chinaz.com/Ip/IpSame/?query="+ip
    h={
    "Host": "mip.chinaz.com",
    "content-length": "13",
    "cache-control": "max-age\u003d0",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://mip.chinaz.com",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": getUA(),
    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://mip.chinaz.com/Ip/IpSame/?query\u003d1.1.1.1",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    "cookie": "inputbox_urls\u003d%5B%221.1.1.1%22%5D"
    }
    reip=[]
    reqs = requests.post(url, headers=h, data="query="+ip, verify=False)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all("td"):
        if "1.1.1.1" not in link.text:
            reip.append(link.text)
   # print(reip)
    if reip != []:
        return reip
    else:
        return []


def t1(ip):
    reip=[]
    ua={"user-agent": getUA()
    }
    try:
        req = requests.get("https://rapiddns.io/sameip/" + ip + "?full=1#result", headers=ua, verify=False).content.decode("utf-8")
       # print(req)
        pattern = r"</th>\n<td>(.*?)</td>"
        results = re.findall(pattern, req)
        #print(results)
        reip=results
        if reip!=[]:
            return reip
        else:
            return []
    except Exception as e:
        print(e)
        return []
def t4(ip):
    regex=r"\w+(?:[.-]\w+)*\.(?:com|in|cc|ly|au|org|net|uk|it|jp|cn|co|co.in|tk|hu|at|io|be|info|co.at|com.au|ca|tech|mobi|tr|com.tr|soy|eu|us|ru|de|se|company|co.uk|fr|sbs|pt|dk|pk|cv.ua|ua|pl|xyz|nl|co.nz|army|gov|gov.in|tc|tt|fuck|wtf|es|arpa|pro|noob|app|gq|im|pw|tv|cloud|ml|ga|biz|vip|me|you|ooo)\b"
    #regex="(https?:\/\/)?([w]{3}\.)?(\w*.\w*)([\/\w]*)"
    h={
    "Host": "askdns.com",
    "cache-control": "max-age\u003d0",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": getUA(),
    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7"
    }
    
    req=requests.get("https://askdns.com/ip/"+ip, headers=h).text
    #print(req)
    data=re.findall(regex, req)
    reip=data
    if reip!=[]:
        return reip
    else:
        return []

def getUA():
    ua=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/109.0.5414.83 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/109.0.5414.83 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPod; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/109.0.5414.83 Mobile/15E148 Safari/604.1"]
    return random.choice(ua)
    
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
