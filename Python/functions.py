import requests, re
from globals import *


def main(request):
    try:
        html = return_html(source)
        local_and_speed_limit = get_localization_and_speed(html)
        has_data = bool(local_and_speed_limit)

        if has_data:
            data_captured_msg = f"The program reach the data\nConsider drive carefully anyway."
            pretty_print(data_captured_msg, True)
            print(local_and_speed_limit)
            return local_and_speed_limit

    except:
        exception_msg = f"Something Went Wrong.\nDrive Slowly."
        pretty_print(exception_msg, False)
        return exception_msg


def return_html(source):
    accessing_msg = f"Trying to Access {source}"
    pretty_print(accessing_msg, True)

    data_request = requests.get(source)
    source_status = data_request.status_code

    if source_status == 200:
        success_message = f"Status Code: {source_status}\n{source} was accessed successfully.\nGetting Speed Gun Data."
        pretty_print(success_message, True)
        html_file = data_request.text
        return html_file
    else:
        failure_message = f"Error.\nThe status code of the site {source} is: {source_status}\nExiting program."
        pretty_print(failure_message, False)
        exit()


def get_localization_and_speed(html):
    regex_localization_and_speed = re.findall(regex, html)
    localization_and_speed = {}
    radar_number = 0
    
    for tuple_value in regex_localization_and_speed:
        for index, value in enumerate(tuple_value):
            is_even = (index % 2) == 0

            if is_even:
                current_radar = {}
                
                speed_limit = int(tuple_value[index].strip())
                road = tuple_value[index + 1].strip().lower()

                msg = f"Road: {road} | Speed Limit:{speed_limit}"

                current_radar = {
                    "localization" : road,
                    "speed_limit" : speed_limit
                }

                radar_number += 1
                localization_and_speed[radar_number] = current_radar

    return localization_and_speed


def pretty_print(msg, status):
    if status == True:
        format_msg = f"{colors['success']}{msg}{colors['end']}"
    else :
        format_msg = f"{colors['err']}{msg}{colors['end']}"

    print(format_msg, end="\n\n")
