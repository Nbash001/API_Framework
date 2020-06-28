import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users/2"


#Read input json file
file = open('/Users/Naveed/Downloads/TestFiles/postreq.json', 'r')
#below will read it, but look like a string
json_input = file.read()
#parse the file into json format
request_json = json.loads(json_input)

print(request_json)

#Making PUT request
response = requests.put(url, request_json)

#Validate response code
assert response.status_code == 200

#Parse response Content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])

##Put is similar to Post, just diff method and response status code