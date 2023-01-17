import requests


def max_value(stats):
    max_val = 0
    max_name = None
    for key, val in stats.items():
        if max_val < val:
            max_val = val
            max_name = key
    return max_name


def set_list(params):
    val_list = []
    for val in params.values():
        val_list += val
    return list(set(val_list))


def filter_country(params):
    return list(filter(lambda log: 'Россия' in list(log.values())[0], params))


def create_folder_ya_disk(token, path, name_folder):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': f'OAuth {token}'}
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    requests.delete(url, params={'path': name_folder, 'permanently': True}, headers=headers)
    req_0 = requests.put(url, params={'path': name_folder}, headers=headers)
    dict_requests = {'status_code': req_0.status_code, 'list_requests': []}
    req = requests.get(url, params={'path': path}, headers=headers).json()
    for i in req['_embedded']['items']:
        dict_requests['list_requests'].append(i['name'])
    return dict_requests
