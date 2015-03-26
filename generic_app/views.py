from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

@login_required(login_url='/accounts/login/')
def generic_app_view(request):
    return render_to_response('generic_app/generic_app.html',
                            {'full_name': request.user.first_name})
