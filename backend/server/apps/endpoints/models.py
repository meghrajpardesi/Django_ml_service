from django.db import models

# Create your models here.
class Endpoint(models.Model):
    '''
    The Endpoint represents ML API endpoint.

    Attributes:
        name: The name of the endpoint, it will be used in API url,
        owner : The String contains owner name,
        created_at : the date when endpoint was created.
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model):
    '''
    THE MLAlgorithms represents the ML/DL algorithm object.
    Attributes:
        name : The name of the algorithm.
        description: The short description of how model algorithm works
        code : THe code of the algorithm
        version : the version of the algorithm similar to software versioning.
        owner : the name of the owner
        created_at : THe date when MLAlgorithms gets added
        parent_endpoint : The reference to the end point.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=10000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
    '''
    The MlAlgorithmsStatus represents status of the MLAlgorithms which can change during the time.
    Attributes
    status : The status of algorithm at the endpoint : can be : testing, staging , production, ab_testing.
    active: the boolean flag which point to currently active status.
    created by : the name of the creator.
    parent_mlalgoritm : the reference to corresponding MLAlgorithm.
    '''
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")

class MLRequest(models.Model):
    '''
    The MLRequest will keep information about all requests to ML algorithms
    NOTE: This models need to be modified as per requirements
    Attributes:
        input_data : The input data to ML algoruthm in json format.
        full_response : The response of the mlalgorithm.
        response : The response of the mlalgorithm in json format.
        feedback: The feedback about the response in json format.
        created_at :  The date when request was created.
        parent_mlalgorithm : The refrence to MLAlgorithm used to compute response
    '''
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE )