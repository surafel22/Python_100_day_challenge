import requests
from datetime import datetime

USERNAME = "sure22"
TOKEN = "alk3894hjkaklj"
GRAPH_ID = "graph1"
QUANTITY = input("How many minutes did you code today?")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_configs = {
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"minutes",
    "type":"int",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_configs, headers=headers)

POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
print(formatted_date)
post_configs = {
    "date":formatted_date,
    "quantity":QUANTITY
}

post_response = requests.post(url=POST_ENDPOINT, json=post_configs, headers=headers)
print(post_response.text)
PUT_ENDPOINT = F"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
put_configs = {
    "date":formatted_date,
    "quantity":QUANTITY
}

# put_response = requests.put(url=PUT_ENDPOINT, json=put_configs, headers=headers)
# print(put_response.text)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
delete_configs = {
    "date":formatted_date,

}
# delete_response = requests.delete(DELETE_ENDPOINT, headers=headers)
# print(delete_response.text)