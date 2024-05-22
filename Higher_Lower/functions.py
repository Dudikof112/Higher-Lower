import game_data
import random

def index():
    def_index = random.randint(0, (len(game_data.data) - 1))

    return def_index


def compare(def_index, def_i):

    print(f"Compare {def_i}: {game_data.data[def_index]['name']}, a {game_data.data[def_index]['description']}, from "
          f"{game_data.data[def_index]['country']}.")


def compare_followers(def_a, def_b):

    if game_data.data[def_a]['follower_count'] > game_data.data[def_b]['follower_count']:
        return True

    else:
        return False
