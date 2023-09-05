import requests
import urllib3
import json
import datetime

# Fix InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def authorization_refresh():
    auth_url = "https://www.strava.com/oauth/token"

    with open('strava_tokens.json', 'r') as json_file:
        refresh_token = json.load(json_file)['refresh_token']

    payload = {
        'client_id': 112918,
        'client_secret': '7adfc48f1ccccc47db0565b73713ef01fa05c8a0',
        'refresh_token': refresh_token,
        'grant_type': "refresh_token",
        'f': 'json'
    }

    # print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    # print("Access Token = {}\n".format(access_token))

    return access_token


def all_activities(access_token, before='', after='', page=1, per_page=30):
    activities_url = "https://www.strava.com/api/v3/athlete/activities"

    hdr = {'Authorization': 'Bearer ' + access_token}
    param = dict()

    if after != '':
        date = datetime.datetime.strptime(after, "%d/%m/%Y")
        param['after'] = datetime.datetime.timestamp(date)
    if before != '':
        date = datetime.datetime.strptime(before, "%d/%m/%Y")
        param['before'] = datetime.datetime.timestamp(date)
    if page != 1:
        param['page'] = page
    if per_page != 30:
        param['per_page'] = per_page

    activities = requests.get(activities_url, headers=hdr, params=param).json()

    return activities


def activity_by_id(access_token, activity_id):
    activity_url = "https://www.strava.com/api/v3/activities/" + activity_id

    hdr = {'Authorization': 'Bearer ' + access_token}
    activity = requests.get(activity_url, headers=hdr).json()

    return activity


def route_by_id(access_token, route_id):
    routes_url = "https://www.strava.com/api/v3/routes/" + route_id

    hdr = {'Authorization': 'Bearer ' + access_token}
    route = requests.get(routes_url, headers=hdr).json()

    return route


if __name__ == '__main__':
    print('Execution strava_api as main...')

    access_token = authorization_refresh()
    activities2022_json = all_activities(access_token, after='16/09/2022', before='18/09/2023', per_page=200)

    with open('activities2023.json', 'w') as f:
        json.dump(activities2022_json, f)

