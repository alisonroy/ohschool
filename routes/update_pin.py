import pymysql
from db_config import mysql
from flask import jsonify, request
from datetime import datetime
from hashlib import sha256
from app import app, forbidden


@app.route('/update-pin', methods=['POST'])
def update_pin():
    try:
        _uid = request.args['uid']
        _date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        _pin_entered = request.args['pin']
        h = sha256()
        h.update(b'_pin_entered')
        _pin = h.hexdigest()

        if _uid and _date_modified and _pin and request.method == 'POST':
            # insert record in database
            sqlQuery = f"UPDATE user_details SET `pin`='{_pin}' , `date_modified`='{_date_modified}' WHERE (`uid` = '{_uid}'); "
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery)
            conn.commit()
            cursor.close()
            conn.close()
            res = jsonify('Pin Updated')
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)
