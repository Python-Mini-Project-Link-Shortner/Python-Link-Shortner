import sys
import subprocess


try:
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'requests'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'pymongo'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'flask'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'dnspython'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'voluptuous'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'short_url'])
except Exception as e:
    print(e)
