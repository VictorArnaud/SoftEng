# File Name: Makefile
# Purpose  : Symplify project commands
# Author   : Victor Arnaud
# Date     : 01/06/2018

SERVER = 0.0.0.0:8000

run:
	# Run the development server
	python3 softeng/manage.py runserver ${SERVER}

migrations:
	# Create all migrations from models
	python3 softeng/manage.py makemigrations

migrate:
	# Migrate all migrations on database
	python3 softeng/manage.py migrate

superuser:
	# Create a superuser on system
	python3 softeng/manage.py createsuperuser

shell:
	# Run interactive shell of project
	python3 softeng/manage.py shell_plus

staticfiles:
	# Generate the staticfiles
	python3 softeng/manage.py collectstatic

populate:
	# Populate the sesame triplestore with RDF file
	python3 ontology/populate.py

rdf:
	# Create RDF file
	python3 ontology/RDF/ontology.py

query:
	# Query to triplify the rdf protege to rdf triplestore
	python3 ontology/query.py

sesame:
	# Run the sesame triplestore container
	sudo docker-compose up -d

clean:
	# Remove all __pycache__
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
