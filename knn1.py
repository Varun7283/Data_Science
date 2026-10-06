import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

data=pd.read_csv('Iris.csv')
print("first few rows of data")
print(data.head())
x=data.iloc[:,:5]
y=data.iloc[:,-1]
print('\n feature data(first 5 rows of data)')
print(x.head())
print('\n labels(first 5 rows of data)')
print(y.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
print('\n training feature data(first 5 rows of data)')
print(x_train.head())
print('\n testing feature data(first 5 rows of data)')
print(x_test.head())
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
clssifier=KNeighborsClassifier(n_neighbors=5)
print(clssifier.fit(x_train,y_train))
y_pred=clssifier.predict(x_test)
print("\n array ",y_pred)
print("\n actual labels ",y_test)
cm=confusion_matrix(y_test,y_pred)
ac=accuracy_score(y_test,y_pred)
print('\n confusion matrix')
print(cm)
print("\n accuracy score ",ac)