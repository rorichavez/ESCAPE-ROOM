# define rooms and items
# GAMME ROOM

import src.functions as fn 

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

mirror = {
    "name": "mirror",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}


# BEDROOM ONE

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

big_dresser = {
    "name": "big dresser",
    "type": "furniture",
}

lamp = {
    "name": "lamp",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

bedroom_one = {
    "name": "bedroom one",
    "type": "room",
}

# BEDROOM TWO

doble_bed = {
    "name": "doble bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

carpet = {
    "name": "carpet",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

bedroom_two = {
    "name": "bedroom two",
    "type": "room",
}

# LIVING ROOM

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

big_couch = {
    "name": "big couch",
    "type": "furniture",
}

tv = {
    "name": "tv",
    "type": "furniture",
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [game_room, bedroom_one, bedroom_two, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, mirror, door_a],
    "piano": [key_a],
    "door a": [game_room, bedroom_one],
    "bedroom one":[queen_bed, big_dresser, lamp, door_b, door_a, door_c],
    "queen bed":[key_b],
    "door b":[bedroom_one, bedroom_two],
    "bedroom two":[doble_bed, dresser, carpet, door_b],
    "doble bed":[key_c],
    "dresser":[key_d],
    "door c":[bedroom_one, living_room],
    "living room":[dining_table, big_couch, tv, door_c, door_d],
    "door d":[outside],
    "outside": [door_d]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

game_state = INIT_GAME_STATE.copy()

fn.start_game(game_state,object_relations)