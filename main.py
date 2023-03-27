
import time
import csv
from datetime import datetime
from Requests import authorization_Requests

def write_requests(service_name):
    sf_response = authorization_Requests.get_request_status_code_security_filters()
    now = datetime.now()
    auth_response = authorization_Requests.get_response_direct_service()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    date_name = now.strftime("%d_%m_%Y")

    with open(service_name +"_"+ date_name +'.csv', mode='a') as employee_date_file:

        employee_writer_date = csv.writer(employee_date_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if sf_response.status_code == 200 and auth_response.status_code == 200 :
            employee_writer_date.writerow([sf_response.status_code, auth_response.status_code, date ])
        else :
            employee_writer_date.writerow([sf_response.status_code, auth_response.status_code, date ])#, sf_response.text,auth_response.text])


def in_minutes(minutes):
    return minutes * 60

def get_range_time(hours_to_monitor, sleep_time):
    return (hours_to_monitor * 60 )/ sleep_time

def monitor(hours_to_monitor, service_name):
    count = 0
    sleep_time = in_minutes(0.5)
    range_time = get_range_time(hours_to_monitor, sleep_time)

    for i in range(int(range_time)):
        count = count + 1
        time.sleep(sleep_time)
        write_requests(service_name)
        print("-------------------------------- " + str(count) + " request")

service_name_to_monitor = "Authorization_Servicelocal"
monitor(9,service_name_to_monitor)