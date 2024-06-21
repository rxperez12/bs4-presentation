from bs4 import BeautifulSoup
import requests
import re

url = f"https://sports.yahoo.com/soccer/scoreboard/?confId=soccer.l.fbeuef&dateRange=current&schedState=7"
results = requests.get(url).text

document = BeautifulSoup(results, "html.parser")

answers = []

# get all games that have already been played
game_elems = document.find_all( "li", class_='final')


for game in game_elems:
    game_score_teams = game.find(class_="score").find_all(class_='team')
    game = []

    # Get teams and respective scores
    for team in game_score_teams:
        name = [ team.text for team in team.select('span[data-tst="first-name"]')]
        score = re.findall(r'\d+', team.text)
        game.append([name[0], score[0]])

    answers.append(game)
    print(game)

with open("output.txt", "w") as txt_file:
    for line in answers:
        txt_file.write(str(line) + "\n")