import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import json
import time
import django
django.setup()

from api.models import Listing
from OP_RETURN import *

current_block_number = get_block_height(testnet=True)

while True:
    #latest_block_number = get_block_height(testnet=True)
    #if latest_block_number != current_block_number:
    #    print OP_RETURN_retrieve_fromblock(block_number=latest_block_number, testnet=True)
    found_db_transactions = OP_RETURN_retrieve_fromblock(testnet=True, scan_mempool=True)
    for t in found_db_transactions:
        try:
            data = json.loads(t['data'])
        except ValueError:
            data = {'error': 'Invalid JSON'}

        if data.get('a') == "pl":
            listing_data = {
                "tx_id": t['txids'][0],
                "game_name": data['gn'],
                "currency_name": data['cn'],
                "currency_amount": data['ca'],
                "cost": data['c'],
                "details": data['d'],
                "seller_address": t['from_address'],
                "block_number": t['heights'][0]
            }
            if listing_data['game_name']:
                print "listing_data", listing_data
                new_l = Listing(**listing_data)
                new_l.save()

    time.sleep(10)
