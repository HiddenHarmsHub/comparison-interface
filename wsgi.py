"""This file contains the WSGI configuration required to serve up the web application.

It works by setting the variable 'application' to a WSGI handler of some description.
"""

import os
import sys

project_home = os.path.dirname(__file__)
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.chdir(project_home)

# This import style will allow the project to be deployed on PythonAnywhere
from app import app as application  # NoQA
