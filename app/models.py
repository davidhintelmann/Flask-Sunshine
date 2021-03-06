from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Sunshine(db.Model):
    __tablename__ = 'sunshine'

    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(56), index=True)
    last_name = db.Column(db.String(26), index=True)
    first_name = db.Column(db.String(25), index=True)
    salary = db.Column(db.DECIMAL(asdecimal=False), index=True)
    taxable = db.Column(db.DECIMAL(asdecimal=False), index=True)
    employer = db.Column(db.String(193))
    job_title = db.Column(db.String(300))
    calendar_year = db.Column(db.Integer, index=True)

    """
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    """

    def __repr__(self):
        return "<Sunshine(first_name={}, last_name={}, employer={})>".format(self.first_name, self.last_name, self.employer)

"""
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
"""


"""
id bigint,
sector VARCHAR(56),
last_name VARCHAR(26),
first_name VARCHAR(25),
salary decimal(12,2),
taxable decimal(11,2),
employer VARCHAR(193),
job_title VARCHAR(300),
calendar_year bigint
"""
