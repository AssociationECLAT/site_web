#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'me'
SITENAME = u'Site ECLAT'

SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['i18n_subsites']
I18N_SUBSITES = {
'en' :{
	'SITENAME':  'Site ECLAT, en',

	'MENUITEMS': [
	('The association',[
	('Who are we?','/pages/assoc1.html'),
	('Sport','/pages/assoc2.html'),
	('Transversal formation,','/pages/assoc3.html'),
	('Contact us','/pages/assoc4.html'),
	('The website','/pages/assoc5.html'),
	]),
	('Doctoral thesis in short',[
	('What is being a doctorate?','/pages/bref1.html' ),
	('Accounts','/pages/bref2.html' ),
	('Around the PhD','/pages/bref3.html' ),
	]),
	('The Centrale Lyon School',[
	('CRIEC','/pages/ecl1.html'),
	('PhD students everyday','/pages/ecl2.html'),
	('About the campus','/pages/ecl3.html'),
	]),
	('PHD Help',[
	('Latex Templates','/pages/aide1.html'),
	('New Phd student guide','/pages/aide2.html'),
	])]
	}
}

main_lang = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


THEME = './chameleon'
BS3_THEME = 'http://bootswatch.com/simplex/bootstrap.min.css'




MENUITEMS=[
("L\'association",[
('Qui sommes nous?','/pages/assoc1.html'),
('Sport','/pages/assoc2.html'),
('Formation Transversale','/pages/assoc3.html'),
('Nous contacter','/pages/assoc4.html'),
('Le site web','/pages/assoc5.html'),
]),
('La thèse en bref',[
('Qu\'est-ce qu\'être un doctorant?','/pages/bref1.html' ),
('Témoignages','/pages/bref2.html' ),
('Autour de la thèse','/pages/bref3.html' ),
]),
('L\'École Centrale Lyon',[
('CRIEC','/pages/ecl1.html'),
('Les doctorants au quotidien','/pages/ecl2.html'),
('Sur le campus','/pages/ecl3.html'),
]),
('Aide au doctorat',[
('Templates Latex','/pages/aide1.html'),
('Guide du nouveau doctorant','/pages/aide2.html'),
])]

LOAD_CONTENT_CACHE = False
OUTPUT_PATH = 'www/'
