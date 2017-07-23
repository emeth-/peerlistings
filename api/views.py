from django.http import HttpResponse
import datetime
import json
from api.models import Listing
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from OP_RETURN import *

def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)

def get_datatable_data(request):

    offset = int(request.GET['start'])
    limit = int(request.GET['length'])

    sort_by = request.GET["columns["+request.GET['order[0][column]']+"][name]"]
    if request.GET["order[0][dir]"] == "desc":
        sort_by = "-"+sort_by

    c_data = Listing.objects.all().order_by(sort_by, 'block_number')
    recordsTotal = c_data.count()
    if request.GET.get('gamename_filter'):
        c_data = c_data.filter(game_name__icontains=request.GET['gamename_filter'])
    recordsFiltered = c_data.count()

    return HttpResponse(json.dumps({
        "data": list(c_data[offset:offset+limit].values()),
        "draw": request.GET['draw'],
        "recordsFiltered": recordsFiltered,
        "recordsTotal": recordsTotal,
    }, default=json_custom_parser), content_type='application/json', status=200)


def calc_fee(request):
    data = {
        "a": "pl", #App = Peerlistings
        "gn": request.POST['game_name'],
        "cn": request.POST['currency_name'],
        "ca": request.POST['currency_amount'],
        "c": request.POST['cost'],
        "d": request.POST['details'],
    }

    fee = OP_RETURN_calc_fee(json.dumps(data))

    return HttpResponse(json.dumps({
        "fee": fee,
    }, default=json_custom_parser), content_type='application/json', status=200)

def create_signature(request):
    pieces = request.POST['verification_string'].split('|')
    tx_id = pieces[0]
    seller_address = pieces[1]

    # Verify listing exists, this throws error if not found
    found_listing = Listing.objects.get(tx_id=tx_id, seller_address=seller_address)

    sign_this = tx_id + "|" + seller_address
    signature = OP_RETURN_sign(seller_address, sign_this, testnet=True)

    return HttpResponse(json.dumps({
        "signature": signature,
    }, default=json_custom_parser), content_type='application/json', status=200)


def verify_signature(request):
    """
    "verification_string": jQuery(t).parent().find(".buyer_string").val(),
    "signature": jQuery(t).parent().find(".seller_signature").val()
    """
    pieces = request.POST['verification_string'].split('|')
    tx_id = pieces[0]
    seller_address = pieces[1]

    # Verify listing exists, this throws error if not found
    found_listing = Listing.objects.get(tx_id=tx_id, seller_address=seller_address)

    sign_this = tx_id + "|" + seller_address
    verified_signature = OP_RETURN_verify_signature(seller_address, request.POST['signature'], sign_this, testnet=True)
    print "*~~***", verified_signature

    return HttpResponse(json.dumps({
        "verified_signature": verified_signature,
    }, default=json_custom_parser), content_type='application/json', status=200)


def submit_sell(request):
    data = {
        "a": "pl", #App = Peerlistings
        "gn": request.POST['game_name'],
        "cn": request.POST['currency_name'],
        "ca": request.POST['currency_amount'],
        "c": request.POST['cost'],
        "d": request.POST['details'],
    }

    results = OP_RETURN_store(json.dumps(data), testnet=True)
    print "Stored in blockchain, results: ", results

    return HttpResponse(json.dumps({
        "results": results,
    }, default=json_custom_parser), content_type='application/json', status=200)

def buy(request):
    return TemplateResponse(request, 'buy.html', context={})

def howitworks(request):
    return TemplateResponse(request, 'howitworks.html', context={})

def sell(request):
    return TemplateResponse(request, 'sell.html', context={})

def autocomplete(request, obj):
    data = []
    if obj == "gamename":
        for l in Listing.objects.filter(game_name__icontains=request.POST['query']).order_by('game_name'):
            data.append({
                "id": l.game_name,
                "name": l.game_name
            })

    #elif...

    return HttpResponse(json.dumps(data, default=json_custom_parser), content_type='application/json', status=200)
