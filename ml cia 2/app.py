from flask import Flask, request, \
    render_template
app = Flask(__name__)
import pickle
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Raveesh123'
app.config['MYSQL_DB'] = 'recommenderdb'
mysql = MySQL(app)


model = pickle.load(open('car_pred_model.pkl','rb'))

@app.route("/")
def main():
    return render_template("login2.html")

@app.route("/login")
def login():
     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from user_details where username = %s and password = %s',(username,password))
        us_acc = cursor.fetchone()

        if us_acc:
            return render_template('main page.html')
        else:
            msg = 'Incorrect username / password !'
            return render_template('login2.html')

        return render_template('login2.html')

@app.route("/predict", methods=['post'])
def pred():
    features = [float(i) 
                for i in 
                (request.form.values())]
    pred = car_pred_model.predict([features])
    pred = round(pred[0],2)
    return render_template("success.html",
                           data=pred)
    
if __name__=='__main__':
    app.run(host='localhost',port=5000)
    
    
    
    
    
    
    
    
    