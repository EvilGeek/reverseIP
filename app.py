import os, re, time, requests
from flask import *

app=Flask(__name__)
app.secret_key="blabkajajs82"

@app.route("/api")
def api():
    ip=request.args.get("ip")
    print(ip)
    if ip:
        data=reverse(ip)
        print(data)
        if data==None:
            return jsonify(status=False, data="")
        elif data==[]:
            return jsonify(status=False, data="")
        else:
            return jsonify(status=True, data=data)
    else:
        return jsonify(status=False, data="")
        
def reverse(ip):
    reip=[]
    ua={"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
    }
    try:
        req = requests.get("https://rapiddns.io/sameip/" + ip + "?full=1#result", headers=ua).content.decode("utf-8")
       # print(req)
        pattern = r"</th>\n<td>(.*?)</td>"
        results = re.findall(pattern, req)
        #print(results)
        for line in results:
            line = line.strip()
            if line not in reip:
                reip.append(line)
        return reip
    except Exception as e:
        print(e)
        return None
        

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
