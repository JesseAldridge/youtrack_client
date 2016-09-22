import json, os
from datetime import date

import requests

import secrets

def pull_and_post_daily_tickets():
    client = requests.session()

    payload = {'login': secrets.username, 'password': secrets.password}
    headers = {'Accept': 'application/json'}
    resp = client.post(
        r'https://gigwalk.myjetbrains.com/youtrack/rest/user/login', data=payload,
        headers=headers)

    # dashboard:
    #                       http://gigwalk.myjetbrains.com/youtrack/issues?q=Board%3A+To-Do+State%3A+%7BIn+Progress%7D+%23Jesse+

    url = 'https://gigwalk.myjetbrains.com/youtrack/rest/issue?max=100&filter=Board%3A+To-Do+State%3A+%7BIn+Progress%7D+%23Jesse+'
    resp = client.get(url, headers=headers)
    content_dict = json.loads(resp.content)
    ticket_ids = [issue['id'] for issue in content_dict['issue']]

    today = date.today()
    today_str = ' '.join(str(x) for x in (today.year, today.month - 1, today.day))
    url = ('https://taskranger.firebaseio.com/user_trees/'
           'github:191903/days/{}/youtrack.json?auth={}').format(
           today_str, secrets.task_ranger_secret)
    requests.put(url, data=json.dumps(ticket_ids))

if __name__ == '__main__':
    pull_and_post_daily_tickets()
