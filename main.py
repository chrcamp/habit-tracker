import requests
import project_auth
from datetime import datetime

TOKEN = project_auth.pixela_token
USERNAME = project_auth.pixela_username
graph_id = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': graph_id,
    'name': 'Reading Graph',
    'unit': 'Pages',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

add_pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.now().strftime('%Y%m%d')

pixel_config = {
    'date': today,
    'quantity': '20'
}

# pixel_response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)

update_pixel_endpoint = f"{add_pixel_endpoint}/{today}"
pixel_update = {
    'quantity': '18'
}
# update_response = requests.put(url=update_pixel_endpoint, json=pixel_update, headers=headers)
# print(update_response.text)

delete_pixel_response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(delete_pixel_response.text)
