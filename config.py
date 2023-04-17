import json


class config:
    GANACHE_URL = 'HTTP://127.0.0.1:8454'

    ABI_FILE = json.load(open('ABI.json'))

    ABI_ADDRESS = ABI_FILE['ABI_ADDRESS']

    ABI = ABI_FILE['ABI']