import pymysql
from db_config import mysql
from flask import jsonify, request
from datetime import date, datetime
from hashlib import sha256
from app import app, forbidden
import random


@app.route('/transaction', methods=['POST'])
def transaction():
    try:
        _uid = request.args['uid']
        _status = request.args['status']
        _tid = date.today().strftime("%Y%m%d")
        _transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        _amount = request.args['amount']
        _letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        _tid = _tid + "".join(random.choice(_letters) for i in range(8))

        if _uid and _status and request.method == 'POST':
            # insert record in database
            sqlQuery = f"INSERT INTO transa(uid,name,dob,date_created,date_modified,balance,pin) VALUES('{_uid}','{_name}','{_dob}','{_date_created}','{_date_modified}',{_balance},'{_pin}' )"
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
