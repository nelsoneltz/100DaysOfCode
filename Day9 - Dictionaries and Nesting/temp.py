# dit = {"Bug":"Insert text here"}

# try:
#     print(dit['Bog']) 
#     # print(0/0)
# except Exception as error:
#     print('An exception ocurred:', type(error).__name__)


# dit = {"Bug":"Insert text here",
#        "Text":"Anything"
# }

# for key in dit:
#     print(dit[key])


# travel_log = {
#     "France": ["Paris","Lille","Dijon"],
#     "Berlin":{
#         "City": 1,
#         "Capital":123
#     }
# }

# print(travel_log['France'][0])
# print(travel_log['Berlin']['City'])

# import json

# with open("teste.json",'r') as file:
#     data = file.read()

# result = json.loads(data)

# print(result['results']['teste2'])

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

formated = format_name("neSleons",'testdD')
print(formated)

