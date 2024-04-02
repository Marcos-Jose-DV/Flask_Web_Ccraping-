from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PremierLeagueTeam(db.Model):
    __tablename__ = 'PremierLeagueTeam'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    stadium = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<PremierLeagueTeam {self.name}>'

class Teams:
    Name = str
    City = str
    Stadium = str