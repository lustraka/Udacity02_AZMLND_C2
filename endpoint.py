import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://d3e565cc-6c6c-4c93-9571-d1f4d6025dc8.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'LghC0qAsgghQeZbm2HNMT72KDs6VrNUV'

# Two sets of data to score, so we get two results back
data = {"data":[{"age":42,"job":"blue-collar","marital":"single","education":"basic.4y","default":"no","housing":"yes","loan":"no","contact":"cellular","month":"may","day_of_week":"thu","duration":560,"campaign":3,"pdays":999,"previous":0,"poutcome":"nonexistent","emp.var.rate":-1.8,"cons.price.idx":92.893,"cons.conf.idx":-46.2,"euribor3m":1.327,"nr.employed":5099.1},{"age":43,"job":"blue-collar","marital":"single","education":"basic.9y","default":"no","housing":"yes","loan":"no","contact":"cellular","month":"jul","day_of_week":"thu","duration":982,"campaign":1,"pdays":999,"previous":0,"poutcome":"nonexistent","emp.var.rate":1.4,"cons.price.idx":93.918,"cons.conf.idx":-42.7,"euribor3m":4.963,"nr.employed":5228.1}]}

"""
{"data":
        [
          {
            "age": 17,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 971,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },
          {
            "age": 87,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 471,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },
      ]
    }
"""

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
with open("resp.json", "w") as _f:
    _f.write(resp.json())
print(resp.json())


