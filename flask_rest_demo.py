from flask import Flask, render_template
from flask_restful import Api, Resource
import sqlite3
from sqlite3 import Error


app =   Flask(__name__)

api =   Api(app)

class returnjson(Resource):
    def get(self):
        data={"data":
            [{
                "Modules": 15,
                "Subject": "Data Structures and Algorithms"
            },
            {
                "Modules": 16,
                "Subject": "Algorythms"
            },
            {
                "Modules": 17,
                "Subject": "Machine Learning"
            }]
        }
        return data

api.add_resource(returnjson,'/returnjson')

class returnsqljson(Resource):
    def get(self):
        db_filename="trip_times_over_day_1.db"
        conn = sqlite3.connect(db_filename)
        print("connected to database.")
        cur = conn.cursor()
        sql = """select overall_duration_in_traffic
          from total_trip
          where start_addr like '%3259 Moggill Rd%'
            and end_addr like '%575 Moggill Rd, Chapel Hill%';"""
        print("executing sql")
        cur.execute(sql)
        rows = cur.fetchall()
        print("num rows = ", len(rows))
        data = []
        time = 0
        for row in rows:
            time += 1
            dict_ = {
                "time":time,
                "trip_length":row[0],
            }
            data.append(dict_)
        return data

api.add_resource(returnsqljson,'/returnsqljson')


@app.route('/chart')
def homeTemplate():
    return render_template('chart.html')

@app.route('/')
def home():
    return "home page."


if __name__=='__main__':
    app.run(debug=True)
