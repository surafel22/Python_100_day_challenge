travel_log = [
    {
        "country":"germany",
        "cities_visited" : ["berlin","munich","frankfurt"]},
    {
        "country":"france",
        "cities_visited":["paris","lille","monaco"]},
]
def add_new(a,b):
    new = {}
    new["country"] = a
    new["country_cisited"] = b
    travel_log.append(new)
add_new("russia",["moscow","st pettersburg"])
print(travel_log)