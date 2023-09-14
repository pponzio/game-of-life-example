# From: https://flask.palletsprojects.com/en/2.3.x/tutorial/tests/
coverage run --branch --source='life/' -m pytest
coverage run --append --branch --source='life/' -m behave
coverage html
