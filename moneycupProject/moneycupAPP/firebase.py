import pyrebase
from django.shortcuts import render, redirect
from django.contrib import messages 



# cambiar la cofiguracion de la base firabse 
config = {
    "apiKey": "AIzaSyDwk4NCdylO1dCORe4jOF0gGclK8I6BJt8",
    "authDomain": "money-16143.firebaseapp.com",
    "databaseURL": "https://money-16143-default-rtdb.firebaseio.com",
    "projectId": "money-16143",
    "storageBucket": "money-16143.appspot.com",
    "messagingSenderId": "564025411265",
    "appId": "1:564025411265:web:24766f64311fa2d4943640",
    "measurementId": "G-T03KM4H7BF"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()
db = firebase.database()


