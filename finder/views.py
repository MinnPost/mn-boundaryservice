import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

# @todo Shouldn't really be here.
def settings_processor(request):
    return {'settings': settings}

def index(request):
    context = RequestContext(request)
    
    # Serialize JSON settings to context
    json_settings = {
      'EXAMPLE_SCOPE': settings.EXAMPLE_SCOPE,
      'EXAMPLE_PLACE': settings.EXAMPLE_PLACE,
      'EXAMPLE_PLACE_LAT_LNG': settings.EXAMPLE_PLACE_LAT_LNG,
      'EXAMPLE_UNIT': settings.EXAMPLE_UNIT,
      'EXAMPLE_UNIT_CODE': settings.EXAMPLE_UNIT_CODE,
      'EXAMPLE_PLACE_BBOX': settings.EXAMPLE_PLACE_BBOX
    }
    json_settings = json.dumps(json_settings)

    try:
        address = request.REQUEST.get('address')
        context['address'] = address
    except KeyError:
        pass

    return render_to_response('index.html', { 'json_settings': json_settings }, context)
