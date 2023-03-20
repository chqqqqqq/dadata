import requests


#Получение результата запросf по API
def get_data(settings, query, count=10):
    try:
        url = settings[0]
        api_key = settings[1]
        language = settings[2]
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + api_key
        }
        params = {
            "query": query,
            "language": language,
            "count": count
        }
        response = requests.post(url, headers=headers, json=params)
        data = response.json()["suggestions"]
        if response.status_code == 200:
            return data
        else:
            return None
    except:
        return None