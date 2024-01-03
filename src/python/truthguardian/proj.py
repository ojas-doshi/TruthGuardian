from flask import Flask, render_template, request
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import itertools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import VotingClassifier

d=[]
app = Flask(__name__)
username=None
@app.route('/details', methods=['POST'])
def details():

    return render_template('profile.html',name=name,email=email,location=location,company=company,followers=followers,following=following,hireable=hireable)

@app.route('/result',methods=['POST','GET'])
def result():
    df = pd.read_csv('C://Users/chelseaforlife/Desktop/fake_or_real_news_2.csv')
    y = df.label

    text= request.form['text']
    text=[text]

  


    clf_pa = PassiveAggressiveClassifier()
    X_train, X_test, y_train, y_test = train_test_split(
    df['text'],
    y,
    test_size=0.2,
    random_state=42)
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    tfidf_train = tfidf_vectorizer.fit_transform(X_train)
    tfidf_test = tfidf_vectorizer.transform(X_test)
    tfidf_text = tfidf_vectorizer.transform(text)
    clf_pa = PassiveAggressiveClassifier()
    clf_pa.fit(tfidf_train,y_train)
    pred_final = clf_pa.predict(tfidf_text)
    pred_final=str(pred_final[0])
    if pred_final=='FAKE':
        return render_template('fake.html')
    else:
        return render_template('real.html')    

   
@app.route('/' ,methods=['POST','GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)