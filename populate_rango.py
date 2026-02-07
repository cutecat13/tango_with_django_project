import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url)[0]
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


def populate():
    python_cat = add_cat('Python', 128, 64)
    add_page(python_cat, 'Official Python Tutorial',
             'https://docs.python.org/3/tutorial/')
    add_page(python_cat, 'How to Think like a Computer Scientist',
             'http://www.greenteapress.com/thinkpython/')
    add_page(python_cat, 'Learn Python in 10 Minutes',
             'http://www.korokithakis.net/tutorials/python/')

    django_cat = add_cat('Django', 64, 32)
    add_page(django_cat, 'Official Django Tutorial',
             'https://docs.djangoproject.com/en/2.1/intro/tutorial01/')
    add_page(django_cat, 'Django Rocks',
             'http://www.djangorocks.com/')
    add_page(django_cat, 'How to Tango with Django',
             'http://www.tangowithdjango.com/')

    frame_cat = add_cat('Other Frameworks', 32, 16)
    add_page(frame_cat, 'Bottle',
             'http://bottlepy.org/docs/dev/')
    add_page(frame_cat, 'Flask',
             'http://flask.pocoo.org')


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
