from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.Mission import Mission

#para adicionar
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str)
argumentos.add_argument('release_date', type=float)
argumentos.add_argument('endpoint', type=float)
argumentos.add_argument('mission_state', type=str)
argumentos.add_argument('crew', type=float)
argumentos.add_argument('playload', type=float)
argumentos.add_argument('duration', type=float)
argumentos.add_argument('cast', type=float)
argumentos.add_argument('status', type=str)



#para atualizar
argumentos_update = reqparse.RequestParser() #definir os argumentos da solicitação HTTP
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('name', type=str)
argumentos.add_argument('release_date', type=float)
argumentos.add_argument('endpoint', type=float)
argumentos.add_argument('mission_state', type=str)
argumentos.add_argument('crew', type=float)
argumentos.add_argument('playload', type=float)
argumentos.add_argument('duration', type=float)
argumentos.add_argument('cast', type=float)
argumentos.add_argument('status', type=str)
#deletar
argumentos_deletar = reqparse.RequestParser()
argumentos_deletar.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class MissionCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            Products.save_products(self, datas['name'], datas['release_date'], datas['endpoint'], datas['mission_state'], datas['crew'], datas['playload'], datas['duration'], datas['cast'], datas['status'])
            return {"message": 'Mission create successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Products.update_products(self, datas['id'], 
            datas['name'],
            datas['release_date'],
            datas['endpoint'],
            datas['mission_state'],
            datas['crew'],
            datas['playload'],
            datas['duration'],
            datas['cast'],
            datas['status'],
            )
            return {"message": 'Mission update successfully!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            Mission.delete_products(self,datas['id'])
            return {"message": 'Mission delete successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

