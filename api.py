""" 
o e-mail que eu criei pra  você é o luis.puc.es@hotmail.com a senha dele é Qwer!@34
seu github é https://github.com/luispuc-es a senha dele é 43@!Rewq
não posso mandar links pela plataforma só posso mandar a atividade uma vez pela plataforma
então se ficar faltando alguma coisa, a gente vai conversando pelo chat e eu te mando nesse e-mail
 """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    funds_wallet = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"User(login = {self.login}, e-mail = {self.email})"

class EventModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, foreign_key=True)
    title = db.Column(db.String(50),unique = True, nullable = False)
    description = db.Column(db.String(150),unique = True, nullable = False)
    quota_value = db.Column(db.Float, nullable = False)
    init_date = db.Column(db.Date, nullable = False)
    end_date = db.Column(db.Date, nullable = False)
    event_date = db.Column(db.Date, nullable = False)
    event_status = db.Column(db.String(15))
    event_evaluation = db.Column(db.String(15))

    def __repr__(self) -> str:
        return f"Event(title = {self.title}, description = {self.description}, event date = {self.event_date})"
    




user_args = reqparse.RequestParser()
user_args.add_argument('login', type=str, required=True, help="login cannot be blank")
user_args.add_argument('email', type=str, required=True, help="E-mail cannot be blank")

event_args = reqparse.RequestParser()
event_args.add_argument('id_user', type=int, required=True, help="User id cannot be blank")
event_args.add_argument('title', type=str, required=True, help="title id cannot be blank")
event_args.add_argument('description', type=str, required=True, help="description id cannot be blank")
event_args.add_argument('quota_value', type=float, required=True, help="quota_value id cannot be blank")
event_args.add_argument('init_date', type=str, required=True, help="init_date id cannot be blank")
event_args.add_argument('end_date', type=str, required=True, help="end_date id cannot be blank")
event_args.add_argument('event_date', type=str, required=True, help="event_date id cannot be blank")
event_args.add_argument('event_status', type=str)
event_args.add_argument('event_evaluation', type=str)



userFields = {
    'id':fields.Integer,
    'login':fields.String,
    'email':fields.String,
    'funds_wallet':fields.Float,

}

class SignUp(Resource):      
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(login=args["login"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201


class UserLogin(Resource):
    @marshal_with(userFields)
    def get(self, id):
        #todo create validation to find out user in the list
        user = UserModel.query.filter_by(id==id).first()
        if not user:
            abort(404,"User not found")
        return user
    
class AddNewEvent(Resource):
    def post(self):
        #todo
        return
        



class GetEvents(Resource):
    def get(self):
        #todo
        return
        


class DeleteEvent(Resource):
    def delete(self):
        #todo
        return


class EvaluateNewEvent(Resource):
    def patch(self, id):
        #todo
        return

class AddFunds(Resource):
    def put(self):
        #todo
        return

class WithdrawFunds(Resource):
    def put(self):
        #todo
        return

class BetOnEvent(Resource):
    def put(self):
        #todo
        return

class FinishEvent(Resource):
    def put(self):
        #todo
        return

class SearchEvents(Resource):
    def get(self):
        #todo
        return

api.add_resource(SignUp, '/signUp/')
api.add_resource(UserLogin, '/login/<int:id>')
api.add_resource(AddNewEvent, '/addnewevent/')
api.add_resource(GetEvents, '/getevents/')
api.add_resource(DeleteEvent, '/deleteevent/')
api.add_resource(EvaluateNewEvent, '/evaluatenewevent/')
api.add_resource(AddFunds, '/addfunds/')
api.add_resource(WithdrawFunds, '/withdrawfunds/')
api.add_resource(BetOnEvent, '/betonevent/')
api.add_resource(FinishEvent, '/finishevent/')
api.add_resource(SearchEvents, '/searchevents/')

@app.route('/')
def home():
    return '<h1>Bet Flask REST API</h1>'


if __name__ == '__main__':
    app.run(debug=True)