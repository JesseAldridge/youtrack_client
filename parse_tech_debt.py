import json, os

with open(os.path.expanduser('~/Desktop/out2.json')) as f:
    text = f.read()

yt_results = json.loads(text)

print len(yt_results['issue'])
