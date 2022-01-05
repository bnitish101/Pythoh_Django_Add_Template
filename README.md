Django installation
Configuration using cmd
Check python version in the project directory : python
pip install virtualenv
virtualenv env
env\scripts\activate OR env\scripts\deactivate
pip install django
django-admin (to see all commands)
django-admin startproject studybubd
cd studybubd
python manage.py runserver
Move env folder into the project folder studybubd
Open project folder studybubd in VS Code editor
(env) C:\PythonPojects\Pythoh_Django_Add_Template>python manage.py startapp baseApp
Understand Directory structure 
Projects
App
Routing
views 
Template 
Rendering templates
HTML CSS
Template inhritance
{% include ‘navbar.html’ %}
{% extends ‘main.html’ %}
{% block contents %} html code {% endblock %}
