#!/bin/bash -e
coverage run manage.py test
coverage html
open htmlcov/index.html