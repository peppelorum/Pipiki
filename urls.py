# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings

from articles import views
from articles.models import *
# print articles, dir(articles)



# def display_article_no_year(request, slug, template='articles/article_detail.html'):
#     """Displays a single article."""

#     try:
#         article = Article.objects.live(user=request.user).get(slug=slug)
#     except Article.DoesNotExist:
#         raise Http404

#     # make sure the user is logged in if the article requires it
#     if article.login_required and not request.user.is_authenticated():
#         return HttpResponseRedirect(reverse('auth_login') + '?next=' + request.path)

#     variables = RequestContext(request, {
#         'article': article,
#         'disqus_forum': getattr(settings, 'DISQUS_FORUM_SHORTNAME', None),
#     })
#     response = render_to_response(template, variables)

#     return response



urlpatterns = patterns('',
    
       # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'admin/(.*)', admin.site.root),
    url(r'^', include('articles.urls')),
    (r'^treenav/', include('treenav.urls.admin')),
    # url(r'^(?P<slug>.*)/$', display_article_no_year, name='articles_display_article_no_year'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


# from django.db import models

