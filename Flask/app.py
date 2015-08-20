from flask import Flask
from flask import jsonify,request
import database

app = Flask(__name__)

@app.route('/user_details',methods=['GET','POST'])
def user_details():
    if request.method == 'POST':
        user = request.form['user']
        result = database.user_detail(user)
        #abc = {'user':'Utkarsh'}
        a=[]
        for i in result:
            a.append(i)
        u = {'data':a}
        #print a
        #return 'abc'
        return jsonify(u)

@app.route('/get_user',methods=['GET','POST'])
def get_user():
    user = database.get_user()
    abc = {'user':'Utkarsh'}
    a=[]
    for i in user:
        a.append(i)
    u = {'data':a}
    print a
    #return 'abc'
    return jsonify(u)

@app.route('/post_user',methods=['GET','POST'])
def post_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        result = database.post_user(user,password)
        abc = {'user':'Utkarsh'}
        #a=[]
        #for i in user:
        #    a.append(i)
        #u = {'data':a}
        #print a
        return result
        #return jsonify(u)

    
@app.route('/view_case',methods=['GET','POST'])
def view_case():
    if request.method == 'POST':
        user = request.form['user']

if __name__=='__main__':
    app.run(debug=True,host = '192.168.20.78' , port = 5000 )
    # Add your IP Address as host and run your android device on same network

