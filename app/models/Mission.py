from app import db

class Mission(db.Model):
    __tablename__ = 'mission'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    release_date = db.Column(db.Float)
    endpoint = db.Column(db.Float)
    mission_state = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    playload = db.Column(db.Float)
    duration = db.Column(db.Float)
    cast = db.Column(db.Integer)
    status = db.Column(db.Integer)


    def __init__(self, name, release_date, endpoint, mission_state, crew, playload, duration, cast, status):
        self.name = name
        self.release_date = release_date
        self.endpoint = endpoint
        self.mission_state = mission_state
        self.crew = crew
        self.playload = playload
        self.duration = duration
        self.cast = cast
        self.status = status

     
    def save_mission(self, name, release_date, endpoint, mission_state, crew, playload, duration, cast, status):
        try:
            add_banco = Products(name, release_date, endpoint, mission_state, crew, playload, duration, cast, status)
            print(add_banco)
            db.session.add(add_banco) 
            db.session.commit()
        except Exception as e:
            print(e)

    def update_mission(self, id, name, release_date, endpoint, mission_state, crew, playload, duration, cast, status):
        try:
            db.session.query(Mission).filter(Mission.id==id).update({"name":name,"release_date": release_date, "endpoint": endpoint, "mission_state": mission_state, "crew": crew, "playload": playload, "duration": duration, "cast": cast, "status": status})
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)

    def delete_mission(self, id):
        try:
            db.session.query(Mission).filter(Mission.id==id).delete()
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)

