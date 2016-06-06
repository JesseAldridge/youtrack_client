import json

import requests

import secrets

client = requests.session()

payload = {'login': secrets.username, 'password': secrets.password}
headers = {'Accept': 'application/json'}
resp = client.post(
    r'https://gigwalk.myjetbrains.com/youtrack/rest/user/login', data=payload,
    headers=headers)

# dashboard:  http://gigwalk.myjetbrains.com/youtrack/issues/?q=%23%7BTECH+DEBT%7D+team%3A+%7BBack+End%7D+state%3A+Submitted+state%3A+Blocked+

url = 'https://gigwalk.myjetbrains.com/youtrack/rest/issue?max=100&filter=%23%7BTECH+DEBT%7D+State%3A+Submitted+State%3A+Blocked++Team%3A+%7BBack+End%7D'
resp = client.get(url, headers=headers)
print json.dumps(json.loads(resp.content), indent=2)
