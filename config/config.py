from Models.Teams import db, PremierLeagueTeam
from flask import Flask
from config.development_config import DevelopmentConfig

class ConnectionDataBase:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(DevelopmentConfig)

        db.init_app(self.app)

    def Seed(self):
        with self.app.app_context():
            db.create_all()

            if PremierLeagueTeam.query.count() == 0:
                team1 = PremierLeagueTeam(name='Arsenal', city='London',
                                          stadium='Emirates Stadium')
                team2 = PremierLeagueTeam(
                    name='Chelsea', city='London', stadium='Stamford Bridge')
                team3 = PremierLeagueTeam(name='Manchester United',
                                          city='Manchester', stadium='Old Trafford')

                # Adicione os times ao banco de dados
                db.session.add_all([team1, team2, team3])
                db.session.commit()
