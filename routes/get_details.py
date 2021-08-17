import pymysql
from db_config import mysql
from flask import jsonify, request
from app import app, forbidden


@app.route('/get-details', methods=['POST'])
def get_details():
    try:
        _uid = request.args['uid']

        if _uid and request.method == 'POST':
            # insert record in database
            sqlQuery = f"SELECT `uid`,`name`,`dob`,`date_created`,`date_modified`,`balance` FROM user_details WHERE (`uid` = '{_uid}');"
            print(sqlQuery)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            res = jsonify(rows)
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)
