"""
File to start the application with WSGI.

Copy the example to wsgi.py.
"""
import os
import sys
import site
from distutils.sysconfig import get_python_lib

# Path is the parent directory of this script
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add this path to the system path collection
if path not in sys.path:
  sys.path.append(path)
  
# Add where get_python_lib thinks site packaes are
if os.path.exists(get_python_lib()):
  site.addsitedir(get_python_lib())
else:
  # Check for places where we might find libraries.  This is
  # assuming that there is a virtualenv called bondaryservice
  # and using Python 2.6 or 2.7 in our local directory.
  local6 = path + '/boundaryservice/lib/python2.6/site-packages'
  local7 = path + '/boundaryservice/lib/python2.7/site-packages'
  if os.path.exists(local):
    site.addsitedir(local)
  elif os.path.exists(local7):
    site.addsitedir(local7)


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
