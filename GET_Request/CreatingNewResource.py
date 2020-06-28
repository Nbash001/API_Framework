import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"


#Read input json file
file = open('/Users/Naveed/Downloads/TestFiles/postreq.json', 'r')
#below will read it, but look like a string
json_input = file.read()
#parse the file into json format
request_json = json.loads(json_input)

print(request_json)

#Make POST request with Json Input Body
response = requests.post(url,request_json)
print(response.content)


#make an assertion to verify
assert response.status_code == 201

#Fetch Header from response
print(response.headers)

print(response.headers.get('Content-Length'))

#Parse response into Json format
response_json = json.loads(response.text)

#Pick ID using Json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])