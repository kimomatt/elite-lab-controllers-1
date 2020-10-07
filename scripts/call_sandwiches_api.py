import json
import requests

ROOT_URL = 'http://127.0.0.1:5000'
headers = {'Content-type': 'application/json'}


def print_formatted_response(response):
    """
    Helper function to pretty print the response object
    """
    print("Response Status Code: " + str(response.status_code))
    print("Response data: " + response.text)


def call_create_sandwich_api():
    print("Calling the CreateSandwich API...")
    url = ROOT_URL + '/sandwiches/'
    response = requests.post(
        url,
        data=json.dumps(request_body),
        headers=headers
    )
    print_formatted_response(response)
    return response.json()


def call_get_sandwich_api(sandwich_id):
    print("Calling the GetSandwich API...")
    url = ROOT_URL + '/sandwiches/' + str(sandwich_id)
    response = requests.get(url)
    print_formatted_response(response)
    return response.json()


def call_get_all_sandwich_api():
    print("Calling the GetAllSandwiches API...")
    url = ROOT_URL + '/sandwiches/'
    response = requests.get(url)
    print_formatted_response(response)
    return response.json()


def call_delete_sandwich_api(sandwich_id):
    print("Calling the DeleteSandwich API...")
    url = ROOT_URL + '/sandwiches/' + str(sandwich_id)
    response = requests.delete(url)
    print_formatted_response(response)


def call_delete_all_sandwich_api():
    print("Deleting all Sandwiches...")
    url = ROOT_URL + '/sandwiches/'
    response = requests.get(url)
    for sandwich in response.json()['sandwiches']:
        call_delete_sandwich_api(sandwich['id'])
        print("Deleted Sandwich ID: " + str(sandwich['id']))


if __name__ == '__main__':
    request_body = {
        "name": "Ham Sandwich",
        "bread": "white",
        "filling": "ham"
    }
    sandwich_id = call_create_sandwich_api()['id']
    call_get_all_sandwich_api()
    call_get_sandwich_api(sandwich_id)
    call_delete_sandwich_api(sandwich_id)
    # call_delete_all_sandwich_api()
