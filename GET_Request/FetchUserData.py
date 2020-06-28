import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

# Send GET request
response = requests.get(url)

#Display Status Code
print(response.status_code)

#Validate Status Code
assert response.status_code == 200

# Display Response with .Content (body)
print(response.content)

# Display .headers
print(response.headers)

#Display specific headers
print(response.headers.get('Server'))
print(response.headers.get('Date'))

#Fetch Cookies
print(response.cookies)

#Fetch Encoding
print(response.encoding)

#Fetch Elapsed Time
print(response.elapsed)

#########################################################################

#Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

#Fetch specific value (totalpages) using Json Path
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

#make an validation
assert pages[0] == 2

########################################################################

#Fetch specific value (firstname) using Json Path
first_name = jsonpath.jsonpath(json_response,'data[0].first_name')
print(first_name[0])

#Fetch all first names using Json Path (loop will execute 0 to 2 becuase last value is ignored)
for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])