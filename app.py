
import requests, time, os, threading, socket, re, urllib3, sys, random
from bs4 import BeautifulSoup

urllib3.disable_warnings()
from flask import *

app=Flask(__name__)
app.secret_key="blabkajajs82"

bot_token="5646928081:AAHgBsRYYNmoSvO5ze3nc4R0AeFY5D8i-cU" 
chat_id="5058906117"
dre=r"\w+(?:[.-]\w+)*\.(?:com|in|cc|ly|au|org|net|uk|it|jp|cn|co|co.in|tk|hu|at|io|be|info|co.at|com.au|ca|tech|mobi|tr|com.tr|soy|eu|us|ru|de|se|company|co.uk|fr|sbs|pt|dk|pk|cv.ua|ua|pl|xyz|nl|co.nz|army|gov|gov.in|tc|tt|fuck|just|hack|life|new|cs|world|you|love|dog|host|ip||wtf|es|arpa|pro|noob|app|gq|im|pw|tv|cloud|ml|ga|biz|vip|me|you|ooo|phd)\b"

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
        data=None
        try:
            data=reverse(ip)
        
            if data==None:
                return jsonify(status=False, data=None)
            elif data==[]:
                return jsonify(status=False, data=None)
            else:
                return jsonify(status=True, data=data)
        except Exception as e:
            print(str(e))
    else:
        return jsonify(status=False, data=None)

def reverse(ip):
    data=[]
    d1=t1(ip)
    d2= [] #t2(ip)
    d3=t3(ip)
    d4=t4(ip)
    d5=t5(ip)
    d6=t6(ip)
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
    for i in d6:
        if i not in data and "google" not in i and "cloudflare" not in i:
            data.append(i)
    return data


def t6(ip):
    u="https://api.hackertarget.com/reverseiplookup/?q="+ip 
    h={
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "dnt": "1",
    "sec-ch-ua-mobile": "?1",
    "user-agent": getUA(),
    "accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "x-prototype-version": "1.6.0",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://api.hackertarget.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://api.hackertarget.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-IN,en;q\u003d0.9"
        
    }
    try:
        return requests.get(url, headers=h).text.split("\n")
    except Exception as e:
        print(e)
        return []

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
    try:
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
    except Exception as e:
        print(e)
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
    
    try: 
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
    except Exception as e:
        print(e)
        return []


def t1(ip):
    reip=[]
    ua={"user-agent": getUA()
    }
    try:
        req = requests.get("https://rapiddns.io/sameip/" + ip + "?full=1#result", headers=ua, verify=False).text
        soup = BeautifulSoup(req, 'html.parser')
        data=[]
        for row in soup.find_all('tr')[1:]:
            try:
                data.append(row.find('td').text)
            except:
                continue
        return data
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
   # data=re.findall(dre, req)
    try:
        soup = BeautifulSoup(req, "html.parser")
        domain_list = soup.find_all("div", {"class": "flex two"})
        domain_list=domain_list[len(domain_list)-1]
        raw=domain_list.find_all("div")
        domain_names=[]
        for ok in range(0, len(raw)-1, 2):
            try:
                domain_names.append(domain_list.find_all("div")[ok].text.strip())
            except:
                continue

        data=[]
        for ok in domain_names:
            if ok not in ["Domain Name", "Last Updated"] and len(ok.split("."))>1:
                data.append(ok)
        #print(data)
        return data

    except Exception as e :
        print(e)
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
    try:
        soup = BeautifulSoup(req, "html.parser")
        tables = soup.find_all("table")
        table = tables[2] # Select the second table (index 1)
        table_data = []
        rows=table.find_all("tr")
        for row in rows:
            row_data = []
            try:
                for cell in row.find_all("td"):
                    row_data.append(cell.text.strip())
                table_data.append(row_data[0])
            except:
                continue
        return table_data
    except Exception as e:
        print(e)
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



@app.errorhandler(404)
def not_found(e):
    return "Fuck you bitch, ask @ThisIsVaibhavChandra first!" 
if __name__=="__main__":
    app.run()
    
