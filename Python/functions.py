from globals import *
import urllib3
import re

def main():
    html = return_html(source)
    get_localization(html)

def return_html(site):
    http = urllib3.PoolManager()
    data_request = http.request('GET', site)
    site_status = data_request.status

    if site_status == 200:
        html_file = data_request.data.decode("utf-8")
        return html_file
    else:
        failure_message = "The status code of the site {} is: {}".format(site, site_status)
        print(failure_message)
        exit()

def get_localization(h):
    regex_date = re.compile(r"Radar \| (.*)<\/h2>")
    regex_speed_limits = re.compile(r"<big>(.{2}) <small>")
    regex_section_radar = re.compile(r"<\/big><div><h4>(.*?)<\/h4>")

    date_match = regex_date.search(h)
    speed_limits_matches = regex_speed_limits.finditer(h)
    section_radar_matches = regex_section_radar.finditer(h)

    print("Data: {}".format(date_match.group(1)))

    for i in section_radar_matches:
        for j in speed_limits_matches:
            print("Localização: {}, Limite de Velocidade: {} km/h".format(i.group(1), j.group(1)))
            
