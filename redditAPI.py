import requests
import environment

auth = requests.auth.HTTPBasicAuth(environment.redditClient, environment.redditSecret)
data = {'grant_type': 'password',
        'username': environment.redditUser,
        'password': environment.redditPass}
headers = {'User-Agent': 'PCDEALSBOTv1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

def getTopPost(): 
    res = requests.get("https://oauth.reddit.com/r/bapcsalescanada/top/?t=day",
                    headers=headers)
    return [res.json()['data']['children'][0]['data']['title'], res.json()['data']['children'][0]['data']['url_overridden_by_dest']]