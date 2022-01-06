Day one:
45 minutes completed 

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


Day Two:
1:06:02 minutes completed 

Day Three:

Pass the data from view to templates
Aother way to do templating by creating html in appliaction instead of projects
rule to create directory in application for html files
creat templates directory and inside the direcoty must have dictory with the same name as appliction
Passing values through URL in the routing, with data type
Explore name key words in routing, name key word value will not change even the url change that is why we should use name while calling urls