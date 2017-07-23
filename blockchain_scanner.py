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
    print OP_RETURN_retrieve_fromblock(testnet=True, scan_mempool=True)
    """
    [
        {
            "txids": [
                "2e2354862d08be67c7c3fd723b1a8e96357703cda4d17240ca0fef7605a7b46b",
                "33a3dd0953afbadf5d75a9735fc506d1092b158d6753dc8ec5818e68baaaf51b"
            ],
            "data": "{\"a\": \"pl\", \"c\": \"10\", \"cn\": \"Gold - Tichondrius Server\", \"ca\": \"100000\", \"gn\": \"\", \"d\": \"Contact me on keybase, username is emeth\"}",
            "heights": [
                0
            ]
        }
    ]
    """
    time.sleep(10)
