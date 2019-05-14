from globals import *
import urllib3

def main():
    s = list_of_websites[0]
    html = return_html(s)
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
    num_of_char = len(h)
    num_of_char_message = "The program received a html code with {} characters".format(num_of_char)
    print(num_of_char_message)

    section_start = "<section class=\"radar\">"
    section_end = "<div class=\"enquete\">"

    index_char_start = h.index(section_start)
    index_char_end = h.index(section_end)

    print("It starts: {}\nIt ends: {}".format(index_char_start, index_char_end))
    
