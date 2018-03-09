# coding:utf-8

'''
Created on 2010-9-28

@author: tongjp
'''

from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response
from jxuexi.models import Jword, AdvClass

# 单词速览
@cache_page(60 * 15)
def fastview(request):
    #pageinfo = jwocurpag(request,drict)
    wordlist = Jword.objects.all()[:20]
    return render_to_response('fastview.html', {'jword':wordlist})

def saveclass(request):
    #pageinfo = jwocurpag(request,drict)
    advclass= AdvClass(
                       classid = '93',
                       classname = 'testclass'
                       )
    advclass.save()
    return render_to_response('fastview.html')