from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)


@app.route("/")  #pagina inicial/home
def get_list_characters_page():
  url = "https://rickandmortyapi.com/api/character"
  response = urllib.request.urlopen(url)
  data = response.read()
  dict = json.loads(data)

  return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
  url = "https://rickandmortyapi.com/api/character/" + id
  response = urllib.request.urlopen(url)
  data = response.read()
  dict = json.loads(data)

  return render_template("profile.html", profile=dict)


# def index(): #faz essa def para que o programa abra a tela de visualização)
#     return '<h1> Olá, WoMakers!</h1>'
@app.route("/lista")
def get_list_characters(
):  #faz essa def para que o programa abra a tela de visualização)
  url = "https://rickandmortyapi.com/api/character"  #url do sit rick
  response = urllib.request.urlopen(url)
  characters = response.read()
  dict = json.loads(characters)

  characters = []

  for character in dict["results"]:
    character = {"name": character["name"], "status": character["status"]}

    characters.append(character)

  return {"characters": characters}


@app.route("/locations")
def get_list_locations():
  url = "https://rickandmortyapi.com/api/location"
  response = urllib.request.urlopen(url)
  locations = response.read()
  dict = json.loads(locations)

  locations = []

  for location in dict["results"]:
    location = {
      "id": location["id"],
      "name": location["name"],
      "type": location["type"],
      "dimension": location["dimension"],
    }

    locations.append(location)

  return render_template("locations.html", locations=locations)


@app.route("/location/<id>")
def get_location(id):
  url = "https://rickandmortyapi.com/api/location/" + id  #na correção do exercicio foi utilizado o + logo após o sinal de igual e o id entre {}" o que causou um erro. ao fazer nesse padrão que eu fiz, deu certo. como estava no exemplo/correção url = +"https://rickandmortyapi.com/api/location/{id}"
  response = urllib.request.urlopen(url)
  data = response.read()
  location = json.loads(data)

  characters = []
  for char_url in location['residents']:
    char_response = urllib.request.urlopen(char_url)
    char_data = char_response.read()
    char_dict = json.loads(char_data)
    characters.append(char_dict)
  location['characters'] = characters

  return render_template("location.html", location=location)


@app.route("/episodes")
def get_list_episodes():
  url = "https://rickandmortyapi.com/api/episode/"
  response = urllib.request.urlopen(url)
  episodes = response.read()
  dict = json.loads(episodes)

  episodes = []

  for episode in dict["results"]:
    episode = {
      "id": episode["id"],
      "name": episode["name"],
      "air_date": episode["air_date"],
      "episode": episode["episode"],
    }

    episodes.append(episode)

  return render_template("episodes.html", episodes=episodes)


# @app.route("/episode/<id>")
# def get_episode(id):
#   url = "https://rickandmortyapi.com/api/episode/"+id
#   response = urllib.request.urlopen(url)
#   data = response.read()
#   episode = json.loads(data)

app.run(host='0.0.0.0', port=81)
