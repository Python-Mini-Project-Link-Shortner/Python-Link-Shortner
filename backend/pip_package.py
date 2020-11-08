import sys
import subprocess


try:
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'requests'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'pymongo'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'flask'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'dnspython'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'voluptuous'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'short_url'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'flask-cors'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'whitenoise'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'gunicorn'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'geoip2'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'google-api-python-client'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'google-auth'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'google-auth-httplib2'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'google-auth-oauthlib'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'oauth2client'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'lxml'])
except Exception as e:
    print(e)
