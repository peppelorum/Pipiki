import os

from django.contrib.flatpages.models import FlatPage
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

DEFAULT_TEMPLATE = 'flatpages/default.html'


from django import forms

class HostsForm(forms.Form):
    hosts = forms.CharField(widget=forms.Textarea)

#@login_required
def edit_hosts_file(request):
    context = {}
    user = request.user

#    print 'sadsad', self._known_host_file
    #            path = self._known_host_file.split('/')
    path_split = settings.SFTP_KNOWN_HOST_FILE.split('/')
    path_to_create = '/'.join(path_split[:-1])
#    file_to_create = path_split[-1]

    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'ssh')):
        os.makedirs(os.path.join(settings.MEDIA_ROOT, 'ssh'))
        
    if not os.path.isfile(settings.SFTP_KNOWN_HOST_FILE):
        f = file(settings.SFTP_KNOWN_HOST_FILE, "w")
        f.close()

    if request.method == 'POST':
        form = HostsForm(request.POST)
        if form.is_valid():
#            form.save()
#            print form.cleaned_data['hosts']
            f = file(settings.SFTP_KNOWN_HOST_FILE, "w")
            f.write(form.cleaned_data['hosts'])
            f.close()
            return redirect('/edithosts/')
    else:
        f = file(settings.SFTP_KNOWN_HOST_FILE, "r")
        text = f.read()
        f.close()
        form = HostsForm(initial={'hosts':text})

    context.update({
        'form': form,
#        'tags': Tag.objects.all().order_by('title')
    })
    variables = RequestContext(request, context)

    return render_to_response('hosts_edit.html', variables)

# This view is called from FlatpageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching flatpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.
def flatpage(request, url):
    """
    Public interface to the flat page view.

    Models: `flatpages.flatpages`
    Templates: Uses the template defined by the ``template_name`` field,
        or `flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    f = get_object_or_404(FlatPage, url__exact=url, sites__id__exact=settings.SITE_ID)
    return render_flatpage(request, f)

@csrf_protect
def render_flatpage(request, f):
    """
    Internal interface to the flat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if f.template_name:
        t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    c = RequestContext(request, {
        'flatpage': f,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, FlatPage, f.id)
    return response
