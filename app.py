from flask import Flask, request, render_template, redirect, url_for, abort
app = Flask(__name__) 

@app.route('/') 
def index(): 
    return 'mainpage!' 

@app.route('/hello/') 
def hello(): 
    return 'Hello, World!' 

@app.route('/hello/<name>') 
def hellovar(name): 
    return 'Hello, {}!'.format(name)

@app.route('/input/<int:num>') 
def input_num(num): 
    if num == 1:
        return "도라에몽"
    elif num == 2:
        return "노진구"
    elif num == 3:
        return "jaian"
    else:
        return "nothing"    
    
    #return 'Hello, {}!'.format(name)    

# login
@app.route('/login', methods=['GET','POST']) 
def login(): 
    if request.method == 'GET':
        return render_template('login.html') 
    else:
        id = request.form['id']
        pw = request.form['pw']
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀 틀.
        if id == 'abc' and pw == '1234':
            return "hi {}".format(id)
        else:
            return "check u r id or pw"    

@app.route('/form') 
def form(): 
    return render_template('test.html')

@app.route('/method', methods=['GET','POST']) 
def method(): 
    if request.method == 'GET':
        return 'GET 으로 전송이다'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        return 'POST 으로 전송이다 학번은: {} 이름은: {}'.format(num, name)    
    
@app.route('/naver') 
def naver():
    return redirect("https://www.naver.com/")   
#    return render_template("naver.html") 
  
@app.route('/kakao') 
def daum(): 
    return redirect("https://www.daum.net/")     

@app.route('/urltest') 
def url_test(): 
    return redirect(url_for('naver'))    

@app.route('/move/<site>') 
def move_site(site): 
    if site == 'naver':
        return redirect(url_for('naver'))        
    elif site == 'daum':     
        return redirect(url_for('daum'))
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없어요. URL을 보세요", 404 

@app.route('/img') 
def img():
    return render_template("image.html")
            
if __name__ == '__main__': 
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=false)
