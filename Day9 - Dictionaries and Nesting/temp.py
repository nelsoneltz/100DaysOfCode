# dit = {"Bug":"Insert text here"}

# try:
#     print(dit['Bog']) 
#     # print(0/0)
# except Exception as error:
#     print('An exception ocurred:', type(error).__name__)


dit = {"Bug":"Insert text here",
       "Text":"Anything"
}

for key in dit:
    print(dit[key])
    print(dit)


# travel_log = {
#     "France": ["Paris","Lille","Dijon"],
#     "Berlin":{
#         "City": 1,
#         "Capital":123
#     }
# }

# print(travel_log['France'][0])
# print(travel_log['Berlin']['City'])