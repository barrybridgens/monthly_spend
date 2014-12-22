try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Monthly Spend',
    'author': 'Barry Bridgens',
    'url': 'https://github.com/barrybridgens/monthly_spend',
    'download_url': 'https://github.com/barrybridgens/monthly_spend',
    'author_email': 'barry@bridgens.me.uk',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'monthly_spend'
}

setup(**config)
