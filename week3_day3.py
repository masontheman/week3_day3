import requests as req 
class PokeStats:
    def __init__(self,name,at_json = {}):
        self.name = name
        pokemon=req.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')
        self.at_json = at_json
        at_json = pokemon.json()
        print(f"{name.capitalize()} weighs {at_json['weight']} poop units and is {at_json['height']} poopies tall")
    def get_Moves(self,move):
        self.at_json = req.get(f'https://pokeapi.co/api/v2/move/{move}/').json()
        print(f"{move.capitalize()} with an accuracy of  {self.at_json['accuracy']}")
        pass
    def try_twnty(self):
        pokemon=req.get(f'https://pokeapi.co/api/v2/move/?limit=1000&offset=20')
        at_json = pokemon.json()
        print(*(y for x in at_json['results'] for z,y in x.items() if z == 'name'),sep=',')
    def get_pokemon_name_lol(self):
        pokemon=req.get(f'https://pokeapi.co/api/v2/pokemon/?limit=1000&offset=20')
        at_json = pokemon.json()
        print(*(y for x in at_json['results'] for z,y in x.items() if z == 'name'),sep=',')
        #print(*(y for x in at_json['results'] for z,y in x.items() if z == 'name'),sep=',')
charizard = PokeStats('charizard')
#clefairy = PokeStats('clefairy')
#charizard.get_Moves('double-slap')
#charizard.try_twnty()
#charizard.get_pokemon_name_lol()
charizard.who_can_learn()

