from django.shortcuts import render, HttpResponse
from django.core.cache import cache
from blog import signals
# from django.views.decorators.cache import cache_page


# @cache_page(30)
def home(request):
    # custom signal =============
    # signals.notification.send(sender=None, request=request, user=['Mohammad', 'Yasir'])

    # cache low level api ==============
    # fees = cache.get_or_set('fees', 11000, 20, version=2)
    # data = {'name':'abc', 'roll':101}
    # cache.set_many(data, 30)
    # sv = cache.get_many(data)
    # print(sv)

    # cache.delete('fees', version=2)

    # cache.set('roll', 101, 60)
    # roll = cache.get('roll')
    # cache.decr('roll', delta=1)
    # cache.incr('roll', delta=1)
    # print(roll)

    # session count===============
    # cnt = request.session.get('count',0)
    # new_cnt = cnt+1
    # request.session['count'] = new_cnt

    # cache=================
    # name = 'yasir'

    # cache.clear()
    return render(request, 'core/index.html')
