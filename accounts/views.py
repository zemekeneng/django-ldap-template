from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def login_view(request):
    c = {}
    c.update(csrf(request))
    c['next'] = request.GET.get('next') or '/accounts/home/'
    return render_to_response('accounts/login.html', c)

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        next = request.POST.get('next') or '/accounts/home/'
        return HttpResponseRedirect(next)
    else:
        return HttpResponseRedirect('/accounts/invalid')

def invalid_view(request):
    return render_to_response('accounts/invalid.html')


@login_required(login_url='/accounts/login/')
def loggedin_view(request):
    return render_to_response('accounts/home.html',
                            {'full_name': request.user.first_name})