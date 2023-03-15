birds = [{'name':'mus','key':'m','count':0},
          {'name':'duif','key':'d','count':0},
          {'name':'koolmees','key':'k','count':0},
          {'name':'kraai','key':'i','count':0},
          ]

print('Bird counter until dot')
# TO DO:

# 1) print all birds with key and name
for bird in birds:
    print(f"{bird['key']}. {bird['name']}")


# 2) define function get_bird_by_key(birds: list, key:str) returns bird or None


def get_bird_by_key(birds: list, key:str):
    for bird in birds:
        if bird['key'] == key:
            return bird
    return None

bird = get_bird_by_key(birds, "x")
print(bird)
# 3) repeat until given '.'
#       input key of bird 
#    find bird with get_bird_by_key
#    if bird found: 
#       increment bird count
#       show bird name and count
while True:
    key = input("Type (.) to stop")
    if key == ".":
        break

    bird = get_bird_by_key(birds, key)
    if bird in birds:
        bird['count'] +=1
        print(f"Incremented count for {bird['name']}: {bird['count']}")
    else:
        print("Bird not found")


# 4) print all birds with name and count
for bird in birds:
    print(f"{bird['name']}: {bird['count']}")


# 5) print per bird also the percentage of the total count