from webapp.database import db


class User(db.Model):
    __tablename__ = 'User'
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    nickname = db.Column(db.String(250))
    email = db.Column(db.String(250))
    age = db.Column(db.Integer)
    score = db.Column(db.Integer)



    def serialize(self):
        return {
            'id_user': self.id_user,
            'name': self.name,
            'nickname': self.nickname,
            'email': self.email,
            'age': self.age,
            'score': self.score

        }
    

class Situation(db.Model):
    __tablename__ = 'Situation'
    id_situation = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    first_choice = db.Column(db.String(250))
    first_choice_electric_charge = db.Column(db.Integer)
    seconde_choice = db.Column(db.String(250))
    seconde_choice_electric_charge = db.Column(db.Integer)
    third_choice = db.Column(db.String(250))
    third_choice_electric_charge = db.Column(db.Integer)
    right_answer = db.Column(db.String(250))
    category = db.Column(db.String(250))
    advice = db.Column(db.String(1000))


    def serialize(self):
        return {
            'id_situation' : self.id_situation,
            'question' : self.question,
            'first_choice' : self.first_choice,
            'first_choice_electric_charge' : self.first_choice_electric_charge,
            'seconde_choice' : self.seconde_choice,
            'seconde_choice_electric_charge' : self.seconde_choice_electric_charge,
            'third_choice' : self.third_choice,
            'third_choice_electric_charge' : self.third_choice_electric_charge,
            'right_answer' : self.right_answer,
            'category' : self.category,
            'advice' : self.advice
        }

    