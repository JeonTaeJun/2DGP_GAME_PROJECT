# layer 0: Background
# layer 1: at
# layer 2: player
# layer 3: monster
# layer 4: font

objects = [[], [], [], [],[]]
def add_object(o, layer):
    objects[layer].append(o)

def add_objects(l, layer):
    objects[layer] += l

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break
def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o
