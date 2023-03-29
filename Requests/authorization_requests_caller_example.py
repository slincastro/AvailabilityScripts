import requests

def get_request_with_sf():
    #----------- Replace From here -----------------
    url = ""

    payload = ''
    headers = { }

    response = requests.request("POST", url, headers=headers, data=payload)
    # ----------- to here -----------------

    return response

def get_request_direct_service():
    # ----------- Replace From here -----------------
    url = ""

    payload = ''
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    print("direct")
    print(response.status_code)
    # ----------- to here -----------------

    return response