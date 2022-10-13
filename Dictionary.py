my_account = {'name': "Ryan", 'account_num': "123"}
print(my_account['name'])
my_account['name'] = 'John'
print(my_account['name'])

longest = 'Raiders'
afc_east_west_wins = {'Bills': 4,
                      'Jets': 3,
                      'Dolphins': 3,
                      'Patriots': 2,
                      'Chiefs': 3,
                      'Chargers': 3,
                      'Broncos': 2,
                      'Raiders': 1}

for team_name in afc_east_west_wins.keys():
    if afc_east_west_wins[team_name] > afc_east_west_wins[longest]:
        longest = team_name
print(longest)
