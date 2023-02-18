import sys
from sys import argv
import poke_api
import pastebin_api


def main():
    poke_name = get_poke_name()
    try:
        poke_dict = poke_api.get_pokemon_info(poke_name)
    except:
        sys.exit()
    title = paste_title_maker(poke_name)
    body_text = paste_body_maker(poke_dict)
    print(body_text)
    pastebin_api.post_new_paste(title, body_text, '1M', False, True)
    return

def get_poke_name():
    try:
        poke_name = argv[1]
    except:
        print("Error: Please provide a Pokemon name")
        sys.exit()
    return poke_name

def paste_title_maker(poke_name):
    poke_name = poke_name.capitalize()
    paste_title = f"{poke_name}'s Abilities" 
    return paste_title

def paste_body_maker(poke_dict):
    count = 0
    abilities = poke_dict["abilities"]
    print(abilities)
    ability_string = ''
    for ability in abilities:
        count +=1
        ability_name = ability['ability']['name']
        if count != len(abilities):
            ability_string += f"- {ability_name}\n"
        else:
            ability_string += f"- {ability_name}"
    return ability_string
    #
    #for i in range(0, len(abilities)):
       # ability = poke_dict["abilities"][i]
        #ability_name = ability["name"]
        
        
        
        #if i != len(abilities):
           # print(f"- {ability_name}\n", end='')
        #else:
            #print(f"- {ability_name}", end='')
        
    
    

if __name__ == '__main__':
    main()