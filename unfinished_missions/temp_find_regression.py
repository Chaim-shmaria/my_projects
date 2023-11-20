import requests

API_URL = "https://api.github.com/search/repositories?q=language:python&sort=stars&per_page=10&page=3"

temp = requests.get(API_URL)
if temp.status_code == 200:
    dict = temp.json()
    # dict2 = [dict['fork':]]
    # print(dict['fork', ])
    # for key, value in dict.items():
    # Print the key and value on a separate row
    # print(f"{key}: {value}")
    print(dict)
