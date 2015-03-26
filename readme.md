Django LDAP Template
=====

This is a generic setup to connect to an ldap server from a Django project.

## Instalation
* Set up virtualenv [condaenv]
```
pip install -r pip.txt
``` 
* Create ldap.secret file [in outer-most dir for default settings]. I included this and the `get_secret(filepath)` function so that I wouldn't have to keep any ldap info in this repo. The file should look like this:
```
uri=#####
dn=#####
password=#####
```
* Set up the database
```
python manage.py syncdb
```
