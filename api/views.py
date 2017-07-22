from django.http import HttpResponse
import datetime
import json
from api.models import Listing
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

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


def dtables_example(request):
    return TemplateResponse(request, 'datatables.html', context={
        "users": []
    })

def sell(request):
    return TemplateResponse(request, 'sell.html', context={})

def autocomplete(request, obj):
    data = []
    if obj == "game_name":
        for l in Listing.objects.filter(game_name__icontains=request.POST['query']).order_by('name'):
            data.append({
                "id": l.game_name,
                "name": l.game_name
            })

    #elif...

    return HttpResponse(json.dumps(data, default=json_custom_parser), content_type='application/json', status=200)
