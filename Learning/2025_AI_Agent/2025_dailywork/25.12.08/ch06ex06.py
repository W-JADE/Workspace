phonebook ={
    "p_list" : [
        {"no": 1, "name":"장이연", "phone":"010-1111-1111"},
        {"no": 2, "name":"감보람", "phone":"010-1111-2222"},
        {"no": 3, "name":"나한별", "phone":"010-1111-3333"},
        {"no": 4, "name":"박서우", "phone":"010-1111-4444"}
    ],
    "nextNO" : 5
}

import json

with open("phonebook.json", "w", encoding="utf-8") as f:
    json.dump(phonebook, f, ensure_ascii=False, indent=2)


with open("phonebook.json", "r", encoding="utf-8") as f:
    loaded_phonebook = json.load(f)


print(loaded_phonebook["p_list"], ":", loaded_phonebook["nextNo"])