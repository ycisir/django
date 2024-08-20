from django.shortcuts import render, HttpResponse


# Create your views here.
# def setcookie(request):
#     resp = render(request, 'student/setcookie.html')
#     resp.set_cookie('name','jack',)
#     return resp

# def getcookie(request):
#     # name = request.COOKIES['name']
#     name = request.COOKIES.get('name', 'guest')
#     return render(request, 'student/getcookie.html', {'name':name})

# def delcookie(request):
#     resp = render(request, 'student/delcookie.html')
#     resp.delete_cookie('name')
#     return resp


# ===============================================================
def setsession(request):
    request.session['name'] = 'jack'
    # request.session['email'] = 'jack@bp.ship'
    # request.session.set_expiry(5)
    return render(request, 'student/setsession.html')


def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name':name})
    # if 'name' in request.session:
    #     name = request.session['name']
    #     request.session.modified = True
    #     return render(request, 'student/getsession.html', {'name':name})
    # else:
    #     return HttpResponse('Your session has expired...')

    # name = request.session.get('name', 'Guest')
    # keys = request.session.keys()
    # items = request.session.items()
    # age = request.session.setdefault('age', '27')

    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_age())
    # print(request.session.get_expiry_date())
    # print(request.session.get_expire_at_browser_close())

    

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    # else:
    #     print('No key availabe!')
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')

# ====================================================================

# def settestcookie(request):
#     request.session.set_test_cookie()
#     return render(request, 'student/settestcookie.html')

# def checktestcookie(request):
#     print(request.session.test_cookie_worked())
#     return render(request, 'student/checktestcookie.html')

# def deltestcookie(request):
#     request.session.delete_test_cookie()
#     return render(request, 'student/deltestcookie.html')