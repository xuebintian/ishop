# -*- coding: utf-8 -*-
import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

logger = logging.getLogger('django')


@login_required
def index(request):
    template = u'index.html'
    contexts = {u'title': u'ishop'}
    return render(request, template, contexts)


@login_required
def api(request):
    success = False
    message = ''
    if request.method == 'GET':
        try:
            user = request.user
            success = True
        except Exception as e:
            logger.error(e)
            message = e
    else:
        message = 'request method must be GET!'

    data = {'success': success, 'message': message, 'data': None}
    # python的json.dumps方法默认会输出成这种格式"\u2535a\u35a2\u89bd"，要输出中文需要指定ensure_ascii参数为False
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')
