import pymysql
from db_config import mysql
from flask import jsonify, request
from datetime import datetime
from app import app, forbidden


@app.route('/update-user', methods=['POST'])
def update_user():
    try:
        _uid = request.args['uid']
        _name = request.args['name']
        _dob = request.args['dob']
        _date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if _uid and _name and _dob and _date_modified and request.method == 'POST':
            # insert record in database
            sqlQuery = f"UPDATE user_details SET `name`='{_name}' , `dob` ='{_dob}', `date_modified`='{_date_modified}' WHERE (`uid` = '{_uid}'); "
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery)
            conn.commit()
            cursor.close()
            conn.close()
            res = jsonify('User Details Updated')
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)
