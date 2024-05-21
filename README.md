# BITNI KOMANDI

- creating environment: 

- starting environment: [env-name]\Scripts\activate   

- deactivate environment: deactivate

- starting project: django-admin startproject restaurant

- running the server/starting the app: python manage.py runserver

- openning the app: python manage.py startapp rest_app (za modelite)

- migracii: python manage.py makemigrations
	  python manage.py migrate

# Cekori za kreiranje project
	1.django-admin startproject [projectName]  -> kreiranje na obicen proekt
	2.biranje na enivronment (ako ne ti e namesten kako so treba)
	3.python manage.py [projectName so views]
	4.python manage.py runserver
	5.python manage.py migrate -> prven ova da napravi user model i views za admin panel
	6.python manage.py createsuperuser
	7.dodaj go noviot [projectName so views] vo settings -> INSTALLED_APPS
	8.python manage.py makemigrations 
	9.python manage.py migrate
	10.GG <3 !
