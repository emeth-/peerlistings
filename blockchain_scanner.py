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
            try:
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
            except KeyError:

                if (listing_data['game_name'] and
                    listing_data['currency_name'] and
                    listing_data['currency_amount'] and
                    listing_data['cost'] and
                    listing_data['details']):
                    print "listing_data", listing_data
                    try:
                        new_l = Listing(**listing_data)
                        new_l.save()
                    except:
                        print "Error (type error?) while trying to save: ", listing_data

    time.sleep(10)
