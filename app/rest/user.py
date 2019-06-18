import json 
from flask import Blueprint, Response


blueprint = Blueprint('user',__name__)

# コレ2つ必要か？ここですでに依存していていいの？ユースケースだけじゃないのか？
from app.repository.in_memory_repository import InMemoryRepository
from app.use_case import user_list as ul
from app.domain.user import User

@blueprint.route('/users',methods=['GET'])
def user():
    data = [
        {'user_id':'hoge','user_name':'hoge','email':'hoge@example.com'},
        # {'user_id':'hoga','user_name':'hoga','email':'hoga@example.com'},
        # {'user_id':'foge','user_name':'foge','email':'foge@example.com'},
    ]

    # これは全部flask_app.pyにいるべきでは？この呼び方をしないとパッチが聞かないのは何なのか。
    repository = InMemoryRepository(data)
    use_case = ul.UserList(repository)
    result = use_case.execute()
    print('called?')
    # これもシリアライザーを知ってないと成り立たないのでは。
    return Response(json.dumps(result, cls=User.Serializer), mimetype='application/json', status=200)


