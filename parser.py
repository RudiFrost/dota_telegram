import json

import requests


def get_heroes_name():
    heroes_dict = {}
    result = requests.get('https://api.opendota.com/api/heroes')

    for i in range(len(result.json())):
        id = result.json()[i]["id"]
        name = result.json()[i]["name"]
        primary_attr = result.json()[i]["primary_attr"]
        attack_type = result.json()[i]["attack_type"]
        roles = result.json()[i]["roles"]
        heroes_dict[result.json()[i]['localized_name']] = {'id': id, 'name': name, 'primary_attr': primary_attr,
                                                           'attack_type': attack_type, 'roles': roles}

    with open("data/heroes_name.json", "w", encoding='utf-8') as f:
        json.dump(heroes_dict, f, indent=4, ensure_ascii=False)


def get_heroes_id():
    heroes_dict = {}
    result = requests.get('https://api.opendota.com/api/heroes')

    for i in range(len(result.json())):
        localized_name = result.json()[i]["localized_name"]
        name = result.json()[i]["name"]
        primary_attr = result.json()[i]["primary_attr"]
        attack_type = result.json()[i]["attack_type"]
        roles = result.json()[i]["roles"]
        heroes_dict[result.json()[i]['id']] = {'localized_name': localized_name, 'name': name, 'primary_attr': primary_attr,
                                                           'attack_type': attack_type, 'roles': roles}

    with open("data/heroes_id.json", "w", encoding='utf-8') as f:
        json.dump(heroes_dict, f, indent=4, ensure_ascii=False)


def get_match(match_id):
    try:
        result = requests.get('https://api.opendota.com/api/matches/' + str(match_id))
    except:
        return "пиво"
    match_result = result.json()
    for i in range(10):
        if match_result['picks_bans'][i]["team"] == 1:
            match_result['picks_bans'][i]["team"] = "Dire"
        else:
            match_result['picks_bans'][i]["team"] = "Radiant"
        with open('data/heroes_id.json') as f4:
            templates = json.load(f4)
        match_result['picks_bans'][i]["hero_id"] = templates[str(match_result['picks_bans'][i]["hero_id"])]['localized_name']
    if match_result["radiant_win"]:
        match_result["radiant_win"] = "Radiant"
    else:
        match_result["radiant_win"] = "Dire"
    match_result.pop('players')
    with open("data/match.json", "w", encoding='utf-8') as f:
        json.dump(match_result, f, indent=4, ensure_ascii=False)

