playercards_discard_temp=[]
PlayerCards_Discard=[]
playercards_discard_file = open("./../../data/pandemic/PlayerCards_Deck.txt", "r")
for x in playercards_discard_file:
    playercards_discard_temp.extend(x.split(";"))
# for i in playercards_discard_temp:
#     PlayerCards_Discard.append(i.split(":"))
playercards_discard_file.close()

# del PlayerCards_Discard[-1]



cities_discard_temp=[]
Cities_Discard=[]
cities_discard_file = open("./../../data/pandemic/Cities.txt", "r")
for x in cities_discard_file:
    cities_discard_temp.extend(x.split(";"))
# for i in cities_discard_temp:
#     Cities_Discard.append(i.split(":"))
cities_discard_file.close()

# del Cities_Discard[-1]

events_discard_temp=[]
Events_Discard=[]
events_discard_file = open("./../../data/pandemic/Events.txt", "r")
for x in events_discard_file:
    events_discard_temp.extend(x.split(";"))
# for i in events_discard_temp:
#     Events_Discard.append(i.split(":"))
events_discard_file.close()

# del Events_Discard[-1]

a=list((set(events_discard_temp)- set(playercards_discard_temp)))
b=list((set(cities_discard_temp) - set(playercards_discard_temp))) 

print(a)
print(b)