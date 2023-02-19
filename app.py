import requests, re 


import requests, time, os, threading, socket, re, urllib3, sys, random
from bs4 import BeautifulSoup
import PyBypass as bypasser
urllib3.disable_warnings()
from flask import *

app=Flask(__name__)
app.secret_key="blabkajajs82"

bot_token="5646928081:AAHgBsRYYNmoSvO5ze3nc4R0AeFY5D8i-cU" 
chat_id="5058906117"
dre=r"\w+(?:[.-]\w+)*\.(?:com|in|cc|ly|au|org|net|uk|it|jp|cn|co|co.in|tk|hu|at|io|be|info|co.at|com.au|ca|tech|mobi|tr|com.tr|soy|eu|us|ru|de|se|company|co.uk|fr|sbs|pt|dk|pk|cv.ua|ua|pl|xyz|nl|co.nz|army|gov|gov.in|tc|tt|fuck|just|hack|life|new|cs|world|you|love|dog|host|ip||wtf|es|arpa|pro|noob|app|gq|im|pw|tv|cloud|ml|ga|biz|vip|me|you|ooo)\b"

def sendIP(request, page=""):
    uadata=request.headers.get('User-Agent')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip= request.environ['REMOTE_ADDR']
        requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=Got IP {ip}\nUser Agent {uadata}\nPage {page}")
        return ip
    else:
        ip=request.environ['HTTP_X_FORWARDED_FOR']
        requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text=Got IP {ip}\n User Agent {uadata}\nPage {page}")
        return ip

@app.route("/")
def home():
    sendIP(request)
    #return render_template("vindex.html")
    return "OK Vai"

@app.route("/api/reverseip")
@app.route("/api/reverseip/")
def api():
    sendIP(request, "api-reverseip")
    #return "Mass usage isn't allowed yet! Ask the owner"
    ip=request.args.get("ip")
    print(ip)
    if ip and len(ip.strip().split("."))==4:
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
    d5=t5(ip)
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
    for i in d5:
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
    d=[]
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
    data=re.findall(dre, req)
    reip=data
    if reip!=[]:
        return reip
    else:
        return []




def t5(ip):
    url=f"https://viewdns.info/reverseip/?host={ip}&t=1"
    h={
    "Host": "viewdns.info",
    "cache-control": "max-age\u003d0",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
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
    req=requests.get(url, headers=h).text
    return re.findall(dre, req)


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


def bypassURL(url):
    try:
        bypassed_link = bypasser.bypass(url)
        print(bypassed_link)
        return bypassed_link, "Success!"
    except bypasser.main.BypasserNotFoundError:
        return None, "ERROR: The URL you have send is not supported yet."
    except bypasser.main.UrlConnectionError:
        return None, "ERROR: The URL you have send is unreachable."
    except Exception as e:
        return None, f"ERROR: {str(e)}"

@app.route("/api/urlbypass/")
@app.route("/api/urlbypass")
def apibypassurl():
    Ok=sendIP(request, "api-urlbypass")
   # return "Mass usage isn't allowed yet!"
  #  if Ok.strip() in os.environ.get("BANNED_IP").split(" ") or "python-requests" in request.headers.get('User-Agent'):
   #     return "Fuck You Bitch, First ask @ThisIsVaibhavChandra" 
    if request.args.get("url"):
        url=request.args.get("url").strip()
        if url.startswith("https://")==False and url.startswith("http://")==False:
            url="http://"+url
        bypassed, msg=bypassURL(url)
        print(url)
        print(bypassed)
        if bypassed!=None:
            return jsonify(status=True,url=bypassed, message=msg)
        else:
            return jsonify(status=False,url=bypassed, message=msg)
    else:
        return jsonify(status=False,url=None, message=None)


def getASN(ip):
    try:
        h={"Host": "ipwhois.app",
    "Connection": "keep-alive",

    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "Android",
    "Accept": "*/*",
    "Origin": "https://ipwhois.io",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://ipwhois.io/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-IN,en;q=0.9"}
        req=requests.get(f"https://ipwhois.app/widget.php?ip={ip}&lang=en", headers=h, verify=False).json()
        if req.get("success")!=True:
            return None
        else:
            return req.get("connection").get("asn")
    except Exception as e:
        print(e)
        return None


@app.route("/api/asn")
@app.route("/api/asn")
def asnApi():
    sendIP(request, "api-asn")
    if request.args.get("ip"):
        ip=request.args.get("ip")
        asn=getASN(ip)
        if asn!=None:
            return jsonify(status=True, asn=asn)
        else:
            return jsonify(status=False, asn=None)
    else:
        return jsonify(status=False, asn=None)

@app.errorhandler(404)
def not_found(e):
    return "Fuck you bitch, ask @ThisIsVaibhavChandra first!" 
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
    
