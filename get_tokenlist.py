import json

import requests


URL = 'https://raw.githubusercontent.com/viaprotocol/tokenlists/' \
      '9104291b392a740080393cc2272a0792b895f114/tokenlists/all.json'


def get_tokenlist():
    response = requests.get(url=URL)
    tokenlist = response.json()

    with open('all.json', mode='w') as file:
        file.write(json.dumps(tokenlist, indent=4))
