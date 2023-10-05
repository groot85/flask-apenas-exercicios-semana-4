from flask import Flask
import urllib.request, json

app = Flask(__name__)

@app.route("/")
# def index(): #faz essa def para que o programa abra a tela de visualização)
#     return '<h1> Olá, WoMakers!</h1>'
def get_list_characters(): #faz essa def para que o programa abra a tela de visualização)
    url = "https://rickandmortyapi.com/api/character" #url do sit rick
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict ["results"]:
        character = {
            "name": character ["name"],
            "status": character ["status"]
        }

        characters.append(character)
    
    return {"characters": characters}

#eagora2235

app.run(host='0.0.0.0', port=81)
