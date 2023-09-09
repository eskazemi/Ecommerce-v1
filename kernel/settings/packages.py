from .base import INSTALLED_APPS

# ###########
# Third-party apps #
#############

INSTALLED_APPS.append("django_celery_beat")
INSTALLED_APPS.append("storages")


# ##########
# local apps
# ##########
INSTALLED_APPS.append("accounts")
INSTALLED_APPS.append("home")
INSTALLED_APPS.append("product")
INSTALLED_APPS.append("orders")
