from flask import Flask,render_template,request
import speedtest 

app = Flask(__name__)
 
st=speedtest.Speedtest()


st.get_servers()
st.get_best_server()

@app.route('/')
@app.route('/home')
def test():
    return render_template("body.html")

@app.route('/index',methods=['POST','GET'])   
def download_test():
    d="{:.2f}".format(st.download()/1024/1024)
    u="{:.2f}".format(st.upload()/1024/1024)
    p="{:.2f}".format(st.results.ping)
    d=str(d)
    
    u=str(u)
    p=str(p)
    print(d)
    print(u)
    print(p)
    return render_template("index.html",Speed1=d,Speed2=u,Ping=p)


if __name__=="__main__":
    app.run(debug=True,port=8000)
