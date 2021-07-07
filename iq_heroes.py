from pprint import pprint

import requests


def data_request(name):
    url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
    params = {}
    headers = {}
    return requests.get(url, params=params, headers=headers)


def get_intelligence(name):
    data = data_request(name).json()['results'][0]['powerstats']
    intelligence = data['intelligence']
    return intelligence

if __name__ == '__main__':
    Hulk_iq = get_intelligence('Hulk')
    Captain_iq = get_intelligence('Captain America')
    Thanos_iq = get_intelligence('Thanos')

dict_iq = {'Hulk': Hulk_iq,'Captain America':Captain_iq, 'Thanos':Thanos_iq}

sorted_values = sorted(dict_iq.values())
sorted_dict = {}

for i in sorted_values:
    for k in dict_iq.keys():
        if dict_iq[k] == i:
            sorted_dict[k] = dict_iq[k]
            break
print(list(sorted_dict)[0])
