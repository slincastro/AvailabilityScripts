import requests

def get_request_status_code_security_filters():
    url = ""

    payload = ''
    headers = { }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("secf")
    print(response.status_code)

    return response

def get_response_direct_service():
    url = ""

    payload = ''
    headers = { }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("direct")
    print(response.status_code)

    return response