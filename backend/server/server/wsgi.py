"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()


# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.test_classifier.random_forest import RandomForestClassifier

try:
    registry = MLRegistry()  #creating ML registry
    # random Forest Classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="test_classifier",
                           algorithm_object=rf,
                           algorithm_status="production",
                           algorithm_version='0.0.1',
                           owner='MRJ',
                           algorithm_description="Random Forest with simple pre- and post-processing")

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
