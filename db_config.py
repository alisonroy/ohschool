from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "tux"
app.config['MYSQL_DATABASE_PASSWORD'] = "Licet@123"
app.config['MYSQL_DATABASE_DB'] = "wallets"
app.config['MYSQL_DATABASE_HOST'] = "vmlinuz.pattarai.in"
mysql.init_app(app)
