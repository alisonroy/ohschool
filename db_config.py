from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "STRTjSSGl1"
app.config['MYSQL_DATABASE_PASSWORD'] = "l3lrCnqDoF"
app.config['MYSQL_DATABASE_DB'] = "STRTjSSGl1"
app.config['MYSQL_DATABASE_HOST'] = "remotemysql.com"
mysql.init_app(app)
