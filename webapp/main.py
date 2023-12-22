from flask import Flask, jsonify, request, make_response, render_template
from webapp.database import db
from webapp.models import User, Situation
from weasyprint import HTML
import webapp.mailSender as ms
from flask_cors import CORS 
from webapp.situationsList import Situations

app = Flask(__name__,template_folder="../templates/")
CORS(app) 
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
    situations = Situations
    for situation in situations:
        db.session.add(situation)

    db.session.commit()


def reset_Situation():
    db.session.query(Situation).delete()
    db.session.commit()


#-----------------------users------------------------------------#
 


# GET method to retrieve all users
@app.route('/users', methods=['GET'])
def getUsers():
    # populateUser()
    users = User.query.all()
    usersResponse = [user.serialize() for user in users]
    # response = jsonify([user.serialize() for user in users])
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3001')  # Adjust as needed

    return jsonify(usersResponse),200

# GET method to retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def getUserById(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.serialize())

# POST method to create a new user
@app.route('/users', methods=['POST'])
def createUser():
    data = request.json
    new_user = User(
        name=data.get('name'),
        nickname=data.get('nickname'),
        email=data.get('email'),
        age=data.get('age'),
        score=data.get('score')


    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

# PUT method to update a specific user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.name = data.get('name', user.name)
    user.nickname = data.get('nickname', user.nickname)
    user.email = data.get('email', user.email)
    user.age = data.get('age', user.age)
    user.score = data.get('score', user.score)
    db.session.commit()
    return jsonify(user.serialize())

# DELETE method to delete a specific user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})


#-----------------------situations------------------------------------#

@app.route('/populate')
def populateSituationz():
    reset_Situation()
    populateSituation()

    situations = Situation.query.all()
    situationsResponse = [situation.serialize() for situation in situations]
    return jsonify(situationsResponse),200

@app.route('/situations')
def getSituations():


    situations = Situation.query.all()
    situationsResponse = [situation.serialize() for situation in situations]
    return jsonify(situationsResponse),200

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



@app.route('/generate_certificate')
def generate_certificate():
    # Dummy data (you can replace this with your actual certificate data)
    certificate_data = {
        'course_name': 'Music Course',
        'date': 'December 21, 2023',
        'student_name': 'John Doe'
    }
    
    # Render the HTML template with certificate data
    rendered_html = render_template('certificate_template.html', certificate_data=certificate_data)
    
    # Generate PDF from the rendered HTML using WeasyPrint
    pdf = HTML(string=rendered_html).write_pdf()

    # Create a response with PDF content
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=certificate.pdf'

    return response


# -----------------------email------------------------------------#
@app.route('/send_email/<int:user_id>', methods=['GET'])
def trigger_email(user_id):
    user = User.query.get_or_404(user_id)
    ms.send_email( user.email)
    return "Email sent!"
