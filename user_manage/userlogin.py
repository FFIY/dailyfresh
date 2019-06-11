from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def login(func):

    def login_func(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            r = HttpResponseRedirect('/user/login/')
            r.set_cookie('url', request.get_full_path())
            return r
    return login_func

