from flask import Flask, render_template
appFlask = Flask(__name__)

import pandas as pd
import sqlite3
from sqlite3 import Error


@appFlask.route('/home/<int:score>')
def homeTemplate(score):
    dict = {'Physics':97,'Computers':98,'Mathematics':99}
    return render_template('flaskTemplate_1.html',name = "AmKy", marks = score, result = dict)

@appFlask.route('/test1/<int:score>')
def test1(score):
    print("score:", score)
    return "this is route test1, score="+str(score)

@appFlask.route('/test2')
def test2():
    print("route test2 start.")
    db_filename="trip_times_over_day_1.db"
    conn = sqlite3.connect(db_filename)
    print("connected to database.")
    cur = conn.cursor()
    sql = """select time, num_steps, overall_distance, overall_duration, overall_duration_in_traffic
      from total_trip
      where start_addr like '%3259 Moggill Rd%'
        and end_addr like '%575 Moggill Rd, Chapel Hill%';"""
    print("executing sql")
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return "this is route test2"


if __name__ == '__main__':
    print("start flask server main method.")
    appFlask.run(debug = True)
