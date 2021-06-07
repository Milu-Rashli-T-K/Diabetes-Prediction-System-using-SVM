from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
# loading the iris dataset
from joblib import dump, load
import numpy as np

# import pymysql
# con=pymysql.connect (host="localhost" , user="root", password="", port=3306 , db="diabet")
# cmd=con.cursor()


data_set=None
X=y=None

# dividing X, y into train and test data
def svmtrain(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0,test_size=.25)
    svm_model_linear = SVC(kernel='linear', C=1).fit(X, y)

    dump(svm_model_linear, 'filename.joblib')
    svm_predictions = svm_model_linear.predict(X_test)
    print(len(X_test))
    # print(svm_predictions)

    for i in range(0,len(y_test)):
        print(svm_predictions[i],y_test[i])


# model accuracy for X_test
    accuracy = svm_model_linear.score(X_test, y_test)
    print("accuracy "+str(accuracy))
    #cmd.execute("insert into accuracy values('svm','"+str(accuracy)+"')")
    #con.commit()

# creating a confusion matrix
    cm = confusion_matrix(y_test, svm_predictions)
    print(cm)
X=[]
y=[]
def traing():
    with open("diabetes.csv") as f:
        data = f.readlines()
    lines = np.array(data)

    i=0
    for d in lines:
     if i!=0:
        dd=d.replace('N/A','0').replace('Unknown','0').split(',')
        print("dddddddd",dd)
        y.append(dd[8].replace('\n',''))
        xx=[]


        xx.append(dd[0])
        xx.append(dd[1])
        xx.append(dd[2])
        #xx.append(dd[3])
        #xx.append(dd[4])
        xx.append(dd[5])
        xx.append(dd[6])
        xx.append(dd[7])

        print(xx)
        X.append(xx)
     i=i+1


    svmtrain(X,y)

def glfeature(a):
    pass


def predict(fn):
    glt = glfeature(fn)

    svc = load('filename.joblib')
    p = svc.predict([glt])
    print(p)
    return p

# predict("static/dataset/normal/frame4300.jpg")
traing()