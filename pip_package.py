import sys
import subprocess


try:
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'requests'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'pymongo'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'flask'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'dnspython'])
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'voluptuous'])
except Exception as e:
    print(e)
