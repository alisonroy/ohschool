import pymysql
from db_config import mysql
from flask import jsonify, request
from datetime import datetime
from hashlib import sha256
from app import app, forbidden


@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form.get("username")
        paswd = request.form.get("pass")
        h = sha256()
        h.update(b'{paswd}')
        password = h.hexdigest()
        last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if username and password and request.method == 'POST':
            # insert record in database
            sqlQuery = f"INSERT INTO ohs_user_details(usern,name,dob,date_created,date_modified,balance,pin) VALUES('{_uid}','{_name}','{_dob}','{_date_created}','{_date_modified}',{_balance},'{_pin}' )"
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
