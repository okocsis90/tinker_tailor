def tinker_tailor_basic(end_num, step):
    list_of_players, killed_players, index = list(range(1, end_num + 1)), [], 0
    while list_of_players:
        index = (index + (step-1)) % len(list_of_players)
        killed_players.append(list_of_players.pop(index))
    return killed_players

print(tinker_tailor_basic(5, 3))
