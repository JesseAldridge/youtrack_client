import json, os

def parse_tech_debt():
    with open(os.path.expanduser('~/Desktop/out.json')) as f:
        text = f.read()

    yt_results = json.loads(text)

    return len(yt_results['issue'])

if __name__ == '__main__':
    print parse_tech_debt()
