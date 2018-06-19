
try : 
	from setuptools import setup 
	
except ImportError: 
	
	from disutils.core import setup 

config = {
	
	'description' : 'My Project',
	'author' : 'Thura Aung',
	'url' : 'URL to get it at',
	'download_url' : 'Where to download it.',
	'author_email' : 'thuraaung.ppt@gmail.com',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packeges' : ['NAME'], 
	'scripts' : [], 
	'name' : 'My Project',
}	

setup(**config)	