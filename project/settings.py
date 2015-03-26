"""
Django settings for generic project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
from project.get_secrets import get_secrets

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j49-9wfm9*=k36i8+qu3-mtt9lgvkttujd-g(nhya^o=)_6sow'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition 

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'generic_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'project/templates/'),
                os.path.join(BASE_DIR, 'accounts/templates/'),
                os.path.join(BASE_DIR, 'generic_app/templates/'),)

#######################################################################
## LDAP Config
#######################################################################

secrets = get_secrets(os.path.join(BASE_DIR, 'ldap.secret'))
# Baseline configuration.
AUTH_LDAP_SERVER_URI = secrets['uri']
AUTH_LDAP_BIND_DN = secrets['dn']
AUTH_LDAP_BIND_PASSWORD = secrets['password']

AUTH_LDAP_USER_SEARCH = LDAPSearch("",
    ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

# or perhaps:
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"

# Set up the basic group parameters.
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=django,ou=groups,dc=example,dc=com",
#     ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
# )
# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# # Simple group restrictions
# AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=django,ou=groups,dc=example,dc=com"
# AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=django,ou=groups,dc=example,dc=com"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

# AUTH_LDAP_PROFILE_ATTR_MAP = {
#     "employee_number": "employeeNumber"
# }

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "cn=active,ou=django,ou=groups,dc=example,dc=com",
#     "is_staff": "cn=staff,ou=django,ou=groups,dc=example,dc=com",
#     "is_superuser": "cn=superuser,ou=django,ou=groups,dc=example,dc=com"
# }

# AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
#     "is_awesome": "cn=awesome,ou=django,ou=groups,dc=example,dc=com",
# }

# This is the default, but I like to be explicit.
# AUTH_LDAP_ALWAYS_UPDATE_USER = True

# # Use LDAP group membership to calculate group permissions.
# AUTH_LDAP_FIND_GROUP_PERMS = True

# # Cache group memberships for an hour to minimize LDAP traffic
# AUTH_LDAP_CACHE_GROUPS = True
# AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
