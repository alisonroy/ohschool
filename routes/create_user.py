import pymysql
from db_config import mysql
from flask import jsonify, request
from datetime import datetime
from hashlib import sha256
from app import app, forbidden


@app.route('/create-user', methods=['POST'])
def create_user():
    try:
        _uid = request.args['uid']
        _name = request.args['name']
        _dob = request.args['dob']
        _date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        _date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        _balance = 0
        h = sha256()
        h.update(b'0000')
        _pin = h.hexdigest()

        if _uid and _name and _dob and _date_created and _date_modified and _pin and _balance == 0 and request.method == 'POST':
            # insert record in database
            sqlQuery = f"INSERT INTO user_details(uid,name,dob,date_created,date_modified,balance,pin) VALUES('{_uid}','{_name}','{_dob}','{_date_created}','{_date_modified}',{_balance},'{_pin}' )"
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery)
            conn.commit()
            cursor.close()
            conn.close()
            res = jsonify('User Details Created')
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)
