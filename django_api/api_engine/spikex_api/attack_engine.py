import requests
import urllib.parse as urlparse
import re
from pythonping import ping
import socket

# The shodan API Key is stored im a hidden file called .SHODAN_API_KEY
with open(".SHODAN_API_KEY", "r") as api_key:
    shodan_api = str(api_key.read())

def get_ip(url):

    response_dict = {}
    ping_response = ping(url, count=1)                                                       
    server_ip = re.findall('(?:Reply from )(\d*.\d*.\d*.\d*)', str(ping_response))          
    response_time = re.findall('(?:bytes in )(.*)(:?ms)', str(ping_response))               
    round_trip_time = str(response_time[0][0])
    time_unit = str(response_time[0][1])  

    response_dict['server_ip'] = server_ip[0]
    response_dict['round_trip_time'] = round_trip_time
    response_dict['time_unit'] = time_unit

    return response_dict

def dir_enum(full_url, wordlist):

    response_dict = {}
    with open(wordlist, 'r') as file:
        read_file = file.read()
        for dir in read_file.split():
            try:
                target_url = full_url +"/" + dir
                get_request = requests.get(target_url)
                status_code = get_request.status_code               # Status code is a integer value
                response_dict[target_url] = status_code             # dictionary that contains URL as key and Status Code as value
            except Exception:
                continue
    return response_dict

def sub_enum(url, protocol, wordlist):

    response_dict = {}
    with open(wordlist, 'r') as file:
        read_file = file.read()
        for sub in read_file.split():
            try:
                target_url = protocol + "://" + sub + "." + url
                get_request = requests.get(target_url)
                status_code = get_request.status_code               # Status code is a integer value
                response_dict[target_url] = status_code             # dictionary that contains URL as key and Status Code as integer value
            except Exception:
                continue
    return response_dict


def get_robots(full_url, allow_robots_list, disallow_robots_list):

    robots_url = full_url + "/robots.txt"
    try:
        get_request = requests.get(robots_url)

        response_code = get_request.status_code
        if response_code == 200:
            robots_existence = True
        else:
            robots_existence = False

        if robots_existence == True:
            robots_content = get_request.text

            allow_content = re.findall('(?:Allow: )(.*)', robots_content)

            for dir in allow_content:
                dir = urlparse.urljoin(full_url, dir)
                allow_robots_list.append(dir)

            disallow_content = re.findall('(?:Disallow: )(.*)', robots_content)

            for dir in disallow_content:
                dir = urlparse.urljoin(full_url, dir)
                disallow_robots_list.append(dir)
        else:
            pass
    except Exception:
        pass

def get_sitemap(full_url):

    try:
        sitemap_url = full_url + "/sitemap.xml"
        get_request = requests.get(sitemap_url)

        response_code = get_request.status_code
        if response_code == 200:
            sitemap_existence = True
        else:
            sitemap_existence = False
        
        if sitemap_existence == True:
            sitemap_content = get_request.text
            sitemap_urls = re.findall('(?:<loc>)(.*)(?:</loc>)', str(sitemap_content))
            return sitemap_urls
    except Exception:
        pass

def href_spider(full_url):

    url_list = []
    get_request = requests.get(full_url)
    response_content = get_request.content
    href_links = re.findall('(?:href=")(.*?)"', response_content.decode(errors="ignore"))
    for link in href_links:
        link = urlparse.urljoin(full_url, link)
        
        if "#" in link:
            link = link.split("#")[0]
        
        if full_url in link and link not in url_list:
            url_list.append(link)

    return url_list

def form_spider(full_url):

    count = 0
    get_request = requests.get(full_url)
    response_content = get_request.content
    form_tags = re.findall('</form>', str(response_content))
    count = len(form_tags)
    return count                                # Returning the number of form tags in the site as integer

def http_header_data(full_url):

    get_request = requests.get(full_url)
    headers = get_request.headers
    return headers                              # Dictionary of header files is returned

def http_response(code):

    response = ""
    if code == "200":
        response = "OK"
    elif code == "301":
        response = "Move Permenantly"
    elif code == "400":
        response = "Bad Request"
    elif code == "403":
        response = "Forbidden"
    elif code == "404":
        response = "Not Found"
    elif code == "500":
        response = "Internal Server Error"
    else:
        pass
    return response                              # String value is returned

def shodan_scan(domain_name):

    ip_address = socket.gethostbyname(domain_name)
    shodan_data = requests.get('https://api.shodan.io/shodan/host/' + ip_address + '?key=' + shodan_api)
    return shodan_data.text                      # Returns text data in json format

def random_element(element):

    element_type = str(type(element))

    if element_type == "<class 'str'>":
        return element

    if element_type == "<class 'int'>":
        return element

    if element_type == "<class 'list'>":
        element_list = element
        element_list_len = len(element_list)

        for value in range(0, element_list_len):
            random_element(element_list[value])

    