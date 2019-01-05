import json
import random
'''
get one video to watch
'''

db = 'db.json'
template = """
Video genre : {} \n
Video name : {} \n
Video detail : {} \n
video watching address : {} \n
short description : {}
"""


def load(db):
    with open(db) as f:
        return json.load(f)


def load_test():
    print(load(db))


def random_watch(genre='documentary'):
    movies_db = load(db)
    if genre:
        results = movies_db[genre]
        item = random.choice(results)
        name = item.get("name", None)
        detail = item.get("detail", None)
        address = item.get("address", None)
        desc = item.get("description", None)
        s = template.format(genre, name, detail, address, desc)

        print("Good Luck and enjoy the juerney of next")
        print("=" * 20)
        print(s)
        print("=" * 20)
        return 0
    else:
        pass


random_watch()
