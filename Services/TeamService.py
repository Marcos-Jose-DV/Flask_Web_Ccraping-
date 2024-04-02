from Models.Teams import db, PremierLeagueTeam
from config.config import ConnectionDataBase

class TeamService:
    def __init__(self):
        self.app = ConnectionDataBase().app
        pass

    def creatTeam(self, team):
        with self.app.app_context():
            new_team = PremierLeagueTeam(
                name=team.Name, city=team.City, stadium=team.Stadium)

            db.session.add(new_team)
            db.session.commit()

    def UpdateTeam(self, id, team):
        with self.app.app_context():
            team_update = db.session.get(PremierLeagueTeam, id)
            if team_update:
                team_update.name = team.Name
                team_update.city = team.City
                team_update.stadium = team.Stadium

                db.session.commit()
            else:
                print("Registro com o ID 4 não encontrado.")

    def Delete():
        app = ConnectionDataBase().app
        with app.app_context():

            new_team = PremierLeagueTeam(
                name='New Team', city='City', stadium='Stadium')

            db.session.add(new_team)
            db.session.commit()
