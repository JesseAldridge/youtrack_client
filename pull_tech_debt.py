import json, os

import requests

import secrets

def pull_tech_debt():
    client = requests.session()

    payload = {'login': secrets.username, 'password': secrets.password}
    headers = {'Accept': 'application/json'}
    resp = client.post(
        r'https://gigwalk.myjetbrains.com/youtrack/rest/user/login', data=payload,
        headers=headers)

    # dashboard:
    #                       http://gigwalk.myjetbrains.com/youtrack/issues/?q=%23%7BTECH+DEBT%7D+State%3A+Submitted+state%3A+Blocked++team%3A+%7BBack+End%7D

    url = 'https://gigwalk.myjetbrains.com/youtrack/rest/issue?max=100&filter=%23%7BTECH+DEBT%7D+State%3A+Submitted+State%3A+Blocked++Team%3A+%7BBack+End%7D'
    resp = client.get(url, headers=headers)
    json_str = json.dumps(json.loads(resp.content), indent=2)
    with open(os.path.expanduser('~/Desktop/out.json'), 'w') as f:
        f.write(json_str)

if __name__ == '__main__':
    pull_tech_debt()
