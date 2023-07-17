# import json
import requests
# import shutil

pokename = input('Bir pokemon giriniz : ')
result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokename.lower()}")

if result.status_code == 200:
    json_data = result.json()
    print(f'Pokemon : {pokename.lower()}\nid : {json_data["id"]}\nname : {json_data["name"]}\nweight : {json_data["weight"]}\nheight : {json_data["height"]}')
    # sprites = json_data['sprites']['front_default']
    # files = f"{pokename.lower()}_sprites.png"
    # result = req.get(sprites, stream=True)
    # with open(files, 'wb') as file:
    #     shutil.copyfileobj(result.raw, file)
    