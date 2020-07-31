import requests

url = "https://vipkingston1000.amocrm.ru/api/v2/account"

# payload = {'add': [{'name':'товары'}]}
payload = {'with': 'pipelines,groups,note_types,task_types'}
print("payload ",type(payload))




files = [

]




response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.json())
