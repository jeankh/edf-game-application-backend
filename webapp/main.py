from flask import Flask, jsonify, request
from webapp.database import db
from webapp.models import User, Situation

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///edt.db"
db.init_app(app)
with app.app_context():
    db.create_all()

def populateUser():
    user1 = User(name="John", nickname="Johnny", email='alice@example.com', age=25, score=10)
    user2 = User(name="Alice", nickname="Allie", email='alice@example.com', age=25, score=10)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

def populateSituation():
    situation1 = Situation(
    question='What is the capital of France?',
    first_choice='London',
    seconde_choice='Paris',
    third_choice='Berlin',
    right_answer='Paris'
    )

    situation2 = Situation(
        question='Which planet is known as the Red Planet?',
        first_choice='Earth',
        seconde_choice='Mars',
        third_choice='Venus',
        right_answer='Mars'
    )
    db.session.add(situation1)
    db.session.add(situation2)
    db.session.commit()


def reset_database():
    db.session.query(User).delete()
    db.session.query(Situation).delete()
    db.session.commit()


#-----------------------users------------------------------------#
@app.route('/users')
def getUsers():

    # teste only 
    reset_database()
    populateUser()


    users = User.query.all()
    return jsonify( [e.serialize() for e in users] )

#-----------------------situations------------------------------------#

@app.route('/situations')
def getSituations():

    # teste only 
    reset_database()
    populateSituation()


    situations = Situation.query.all()
    return jsonify( [e.serialize() for e in situations] )

# GET method to retrieve a specific situation by ID
@app.route('/situations/<int:situation_id>', methods=['GET'])
def getSituationById(situation_id):
    situation = Situation.query.get_or_404(situation_id)
    return jsonify(situation.serialize())


# POST method to create a new situation
@app.route('/situations', methods=['POST'])
def createSituation():
    data = request.json
    new_situation = Situation(
        question=data.get('question'),
        first_choice=data.get('first_choice'),
        seconde_choice=data.get('seconde_choice'),
        third_choice=data.get('third_choice'),
        right_answer=data.get('right_answer')
    )
    db.session.add(new_situation)
    db.session.commit()
    return jsonify(new_situation.serialize()), 201

# PUT method to update a specific situation by ID
@app.route('/situations/<int:situation_id>', methods=['PUT'])
def updateSituation(situation_id):
    situation = Situation.query.get_or_404(situation_id)
    data = request.json
    situation.question = data.get('question', situation.question)
    situation.first_choice = data.get('first_choice', situation.first_choice)
    situation.seconde_choice = data.get('seconde_choice', situation.seconde_choice)
    situation.third_choice = data.get('third_choice', situation.third_choice)
    situation.right_answer = data.get('right_answer', situation.right_answer)
    db.session.commit()
    return jsonify(situation.serialize())

# DELETE method to delete a specific situation by ID
@app.route('/situations/<int:situation_id>', methods=['DELETE'])
def deleteSituation(situation_id):
    situation = Situation.query.get_or_404(situation_id)
    db.session.delete(situation)
    db.session.commit()
    return jsonify({'message': 'Situation deleted successfully'})
