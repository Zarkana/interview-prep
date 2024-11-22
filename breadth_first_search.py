from collections import deque

class Person:
    def __init__(self, name, is_mango_seller=False):
        self.name = name
        self.is_mango_seller = is_mango_seller

def mango_bfs(start_person, graph):
    search_queue = deque(graph[start_person])
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person.name not in searched:
            if person.is_mango_seller:
                return person.name
            search_queue.extend(graph[person.name])
            searched.add(person.name)
    return "N/A"

you = Person("you")
alice = Person("alice")
bob = Person("bob")
claire = Person("claire")
peggy = Person("peggy")
anuj = Person("anuj")
thom = Person("thom")
jonny = Person("jonny", True)

graph = {
    "you": [alice, bob, claire],
    "alice": [you, peggy],
    "bob": [you, anuj, peggy],
    "claire": [you, thom, jonny],
    "peggy": [alice, bob],
    "anuj": [bob],
    "thom": [claire],
    "jonny": [claire]
}

print(mango_bfs("you", graph))

