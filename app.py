from Models.Teams import Teams
from Services.TeamService import TeamService
from config.config import ConnectionDataBase

query = TeamService()
team = Teams()
id = 6
team.Name = "Leicester City"
team.City = "Leicester"
team.Stadium = "King Power Stadium"


try:
    # query.creatTeam(team)
    query.UpdateTeam(id, team)
except Exception as e:
    print(f"Error: {e}")
