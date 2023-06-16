# Create a function that adds a new country to the trave_log list

def add_new_country(country:str,visits:int,cities:list,log:list):
    dit = {}
    dit["country"] = country
    dit["visits"] = visits
    dit["cities"] = cities
    log.append(dit)

travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities": ["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities": ["Berlin","Hamburg","Stuttgart"]    
    }
]

add_new_country("Russia",2,["Moscow","Saint Petersburg"],travel_log)

print(travel_log)