from uclcoin import Block
import requests
import json
from collections import namedtuple

r = requests.get('http://piv.azurewebsites.net/block/minable/030137f26e33548c265b60046ac9444fdba8187f7af89ac42bff9b850b75662794')
last_block = json.loads(r.text)
block = Block.from_dict(last_block["block"])
difficulty = last_block["difficulty"]

while block.current_hash[:difficulty].count('0') < difficulty:
    block.nonce += 1
    block.recalculate_hash()

data = json.dumps(block, default=lambda x: x.__dict__)

requests.post('http://piv.azurewebsites.net/block',data,json=True)
