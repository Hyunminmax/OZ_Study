from    flask               import Flask
from    flask_mysqldb       import MySQL
from    flask_smorest       import Api
from    user_routes         import create_user_blueprint
import  yaml

app = Flask(__name__)

# MYSQL 연동설정
db_info = yaml.load(open('H:/My Drive/InBox/000000OZ/OZ_Study/ETC/Database/db_oz.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db_info['mysql_host']
app.config['MYSQL_USER'] = db_info['mysql_user']
app.config['MYSQL_PASSWORD'] = db_info['mysql_password']
app.config['MYSQL_DB'] = db_info['mysql_db']

mysql = MySQL(app)

# blueprint 설정 및 등록
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SQAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SQAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
user_blp = create_user_blueprint(mysql)
api.register_blueprint(user_blp)

# html 코드로 flask-mysql 테스트
from flask import render_template
@app.route('/user_interface')
def user_interface():
    return render_template('users.html')
