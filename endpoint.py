import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://d1828af7-0fb5-486d-841c-35c5fca55847.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "DxnlfpGm3Kaa58RVTic9eE6c9XLczhJe"
# Two sets of data to score, so we get two results back
data = {
    "data": [
    
        {
        "age":75.0,
"anaemia":0,
"creatinine_phosphokinase": 582,
"diabetes":0,
"ejection_fraction":20,
"high_blood_pressure":1,
"platelets":265000.00,
"serum_creatinine":1.9,
"serum_sodium":130,
"sex":1,
"smoking":0,
"time":4                       
            },
        {
        "age":55.0,
"anaemia":0,
"creatinine_phosphokinase": 7861,
"diabetes":0,
"ejection_fraction":38,
"high_blood_pressure":0,
"platelets":263358.03,
"serum_creatinine":1.1,
"serum_sodium":136,
"sex":1,
"smoking":0,
"time":6   
        
            },
        ]
    }

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
