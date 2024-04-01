from    flask_smorest           import Blueprint, abort
from    flask                   import request, jsonify

def create_user_blueprint(mysql):
    user_blp = Blueprint('user_routes', __name__, url_prefix='/users')

    # 전체 유저 데이터를 불러오는 코드
    @user_blp.route('/', methods=['GET'])
    def get_users():
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall() # 결과는 튜플

        cursor.close()

        users_list = []

        for user in users:
            users_list.append({
                'id':       user[0],
                'name':     user[1],
                'email':    user[2]
            })
        return users_list
    
    # 유저를 생성하는 함수
    @user_blp.route('/', methods=['POST'])
    def add_user():
        user_data = request.json

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", 
                       (user_data['name'], user_data['email']))
        mysql.connection.commit()
        cursor.close()
        # return {'msg': 'successfully added user'}, 201
        return jsonify({'message': 'User added successfully'}), 201
    
    # 유저를 업데이트하는 경우
    @user_blp.route('/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user_data = request.json
    
        cursor = mysql.connection.cursor()
        cursor.execute('update users set name = %s, email = %s where id = %s', 
                       (user_data['name'], user_data['email'], user_id))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'User updated successfully'}), 201

    # 유저를 삭제하는 함수
    @user_blp.route('/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,)) # 단일 값을 가진 튜플을 넘기는 경우 끝네 ','를 붙여야 튜플로 인식함. 
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'User deleted successfully'}), 201

    return user_blp