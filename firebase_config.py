import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase with your credentials
cred = credentials.Certificate('https://console.firebase.google.com/u/0/project/weather-alert-app-a3018/database/weather-alert-app-a3018-default-rtdb/data/~2F?fb_gclid=Cj0KCQjw4cS-BhDGARIsABg4_J3OhPEYxhCvOktNezp9ql8v4aqM8UZpegBQzEvq-Z5SoaI-lUFQL1gaAqMvEALw_wcB.json')  # Path to your Firebase credentials
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()
