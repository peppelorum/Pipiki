

from django.core.urlresolvers import reverse, resolve
from articles import models

# @models.permalink
def get_absolute_url_no_year(self):
    return reverse('articles_display_article_no_year', (self.slug))

# print models, dir(models)

models.Article.get_absolute_url_no_year = get_absolute_url_no_year
