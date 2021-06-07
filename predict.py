from flask import *
import pymysql
from joblib import dump, load

obj=Flask(__name__)
@obj.route('/')
def main():
    return render_template('diabet.html')

@obj.route('/btnclk',methods=['POST'])
def btnclk():

    name=request.form['Name']
    #gend=request.form['radiobutton']
    Age=request.form['Age']
    Glucose= request.form['Glucose']
    BloodPressure=request.form['BloodPressure']
    BMI=request.form['BMI']
    DiabetesPedigreeFunction=request.form['DiabetesPedigreeFunction']
    Pregnancies=request.form['Pregnancies']
    #Result=request.form['label']
     #gend=request.form['label']

    lis=[float(Age), float(Glucose),float(BloodPressure),float(BMI),float(DiabetesPedigreeFunction),float(Pregnancies)]
    svc = load('filename.joblib')

    p = svc.predict([lis])
    print(p[0])
    res=p[0]
    if res=="0":
        print("0")
        #return '''<script>alert("Don't worry, you are in safe zone");window.location='/'</script>'''
        return render_template('diabet.html',prediction_text="Don't worry, you are in safe zone ")

    else:
        #return '''<script>alert('You are in trouble , please consult a doctor');window.location='/'</script>'''
        return render_template('diabet.html', prediction_text="You are in trouble , please consult a doctor")

obj.run()
# if __name__ == "__home__" :
#     app.run(debug=True)