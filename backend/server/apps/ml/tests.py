from django.test import TestCase
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.test_classifier.random_forest import RandomForestClassifier

from apps.ml.registry import MLRegistry


class MLTests(TestCase):
    def test_rf_algorithms(self):
        input_data = {
            "age" : 24,
            'workclass':"private",
            'fnlwgt':34146,
            'education':"HS-grad",
            "education-num":9,
            "marital-status":"Married-civ-spouse",
            "occupation":"Software-Engineer",
            "relationship":"Husband",
            "race":'Asian',
            "sex":'Male',
            "capital-gain":0,
            "capital-loss":0,
            "hours-per-week":68,
            "native-country":"India"

        }

        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)

        self.assertEqual('OK', response['status'])
        self.assertEqual('label' in response)
        self.assertEqual('<=50K', response['label'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "test_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = 'random forest'
        algorithm_status = 'production'
        algorithm_version = '0.0.1'
        algorithm_owner = 'MRJ'
        algorithm_description = "Rnadom Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)

        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                               algorithm_status, algorithm_version, algorithm_owner,
                               algorithm_description, algorithm_code)

        # there should be one endpoint available
        self.assertequal(len(registry.endpoint), 1)

