import os
os.system('cls||clear')


auction = {}

end_auction = False
while not end_auction:
    name = input("What is the name of the bider? ")
    bid_price = int(input("What is the bid price? $"))
    auction[name] =bid_price

    anyone = input('Is there anyone else bidding? yes or no? ')
    if anyone == 'no':
        highest = 0
        bidder = ''
        for key in auction:
            if auction[key] >= highest:
                highest = auction[key]
                bidder = key
        print(f"{bidder} won with a bid of ${highest}!")
        end_auction = True
    elif anyone == 'yes':
        os.system('cls||clear')
    


