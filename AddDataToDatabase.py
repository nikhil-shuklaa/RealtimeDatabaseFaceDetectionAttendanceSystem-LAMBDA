import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"#",
     'storageBucket':"#"
})

ref = db.reference('Students')

data = {
    "CSE21-073" : {
        "name": "Nikhil Shukla",
        "department": "ComputerScience",
        "starting_year": 2021,
        "total_attendance": 2,
        "standing": "B1",
        "year": 2,
        "last_attendance_time": "2023-03-19 04:03:00"
    },
    "CSE21-060": {
        "name": "Lawnish",
        "department": "ComputerScience",
        "starting_year": 2021,
        "total_attendance": 1,
        "standing": "A1",
        "year": 2,
        "last_attendance_time": "2023-03-19 04:03:00"
    }
}


for key,value in data.items():
    ref.child(key).set(value)