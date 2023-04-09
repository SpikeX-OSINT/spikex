#!/usr/share/python3 

from flask import Flask, render_template, request, url_for, redirect, jsonify, abort,json
import json
import os
import re
import random
import string
import requests
from attack_engine import dir_enum, sub_enum, get_robots, get_sitemap, href_spider, form_spider, http_header_data, shodan_scan, random_element

random_string = ''.join(random.choices(string.ascii_letters, k=50))

app = Flask(__name__)
app.secret_key = random_string

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/attack_page', methods=['GET', 'POST'])
def scan_results():
    if request.method == 'POST':

        full_url = request.form['target_url']
        domain_name = re.findall('(?:://)(.*)', str(full_url))
        protocol = re.findall('(.*?)(?:://)', str(full_url))

        try:
            check_get = requests.get(full_url)
        except Exception:
            return render_template('unreachable.html')

        if check_get.status_code == 200:
            pass
        elif check_get.status_code != 200:
            return render_template('unreachable.html')

        shodan_data = shodan_scan(domain_name[0])     # Json data in text format
        shodan_data_dict = json.loads(shodan_data)

        shodan_city = shodan_data_dict['city']
        shodan_region_code = shodan_data_dict['region_code']
        shodan_os = shodan_data_dict['os']
        shodan_tags = shodan_data_dict['tags']
        shodan_ip = shodan_data_dict['ip']
        shodan_isp = shodan_data_dict['isp']
        shodan_area_code = shodan_data_dict['area_code']
        shodan_longitude = shodan_data_dict['longitude']
        shodan_last_update = shodan_data_dict['last_update']
        shodan_ports = shodan_data_dict['ports']                   # list
        shodan_latitude = shodan_data_dict['latitude']
        shodan_hostnames = shodan_data_dict['hostnames']           # list
        shodan_country_code = shodan_data_dict['country_code']
        shodan_country_name = shodan_data_dict['country_name']     # list
        shodan_domains = shodan_data_dict['domains']
        shodan_org = shodan_data_dict['org']
        shodan_Data = shodan_data_dict['data']                     # dictionary
        shodan_asn = shodan_data_dict['asn']
        shodan_ip_str = shodan_data_dict['ip_str']

        allow_robots_list = []
        disallow_robots_list = []

        dir_wordlist_location = "wordlists/directory.txt"
        sub_wordlist_location = "wordlists/subdomain.txt"

        href_list = href_spider(full_url)
        sitemap_list = get_sitemap(full_url)
        http_header_data_dict = http_header_data(full_url)
        get_robots(full_url, allow_robots_list, disallow_robots_list)
        form_int = form_spider(full_url)
        #dir_dict = dir_enum(full_url, dir_wordlist_location)
        #sub_dict = sub_enum(full_url, sub_wordlist_location)
        
        # shodan_Data = shodan_data_dict['data']

        return render_template(
            'attack_page.html',
            # --------- sitemap list ------------ #  
            sitemap_list = sitemap_list,
            sitemap_list_len = len(sitemap_list),
            # ----------------------------------- #
            # ------------ href list ------------ # 
            href_list = href_list, 
            href_list_len = len(href_list),
            # ----------------------------------- #
            # --------- allow robots list ------- #
            allow_robots_list = allow_robots_list,
            allow_robots_list_len = len(allow_robots_list),
            # ----------------------------------- #
            # ------ disallow robots list ------- #
            disallow_robots_list = disallow_robots_list,
            disallow_robots_list_len = len(disallow_robots_list),
            # ----------------------------------- #
            # --- http header data dictionary --- #
            http_header_data_dict = http_header_data_dict,
            http_header_data_dict_key_list = http_header_data_dict.keys(), 
            # ----------------------------------- #
            form_int = form_int, 
            # ------- shodan data iteration ------ #
            # ------------------------------------ # 
            shodan_city_out = shodan_city,
            shodan_region_code_out = shodan_region_code,
            shodan_os_out = shodan_os,
            # ---------- tags list --------------- #
            shodan_tags_list_out = shodan_tags,
            shodan_tags_len_out = len(shodan_tags),
            # ------------------------------------ #
            shodan_ip_out = shodan_ip,
            shodan_isp_out = shodan_isp,
            shodan_area_code_out = shodan_area_code,
            shodan_longitude_out = shodan_longitude,
            shodan_last_update_out = shodan_last_update,
            # --------- ports list ------------ #
            shodan_ports_list_out = shodan_ports,
            shodan_ports_len_out = len(shodan_ports),
            # --------------------------------- #
            shodan_latitude_out = shodan_latitude,
            # -------- hostnames list --------- #
            shodan_hostnames_list_out = shodan_hostnames,
            shodan_hostnames_len_out = len(shodan_hostnames),
            # --------------------------------- #
            shodan_country_code_out = shodan_country_code,
            shodan_country_name_out = shodan_country_name,
            # -------- domains list ----------- # 
            shodan_domains_list_out = shodan_domains,
            shodan_domains_len_out = len(shodan_domains),
            # --------------------------------- # 
            shodan_org_out = shodan_org,
            # ----- Shodan Data List ---------- #
            shodan_Data_out = shodan_Data,
            shodan_Data_len_out = len(shodan_Data),
            # --------------------------------- #
            shodan_asn_out = shodan_asn,
            shodan_ip_str_out = shodan_ip_str
            )

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/api')
def api():
    full_url = request.args.get('url')
    mode = request.args.get('mode')
    domain_name = re.findall('(?:://)(.*)', str(full_url))
    error_list = ['error']

    if not full_url and not mode:
        return render_template('api.html')

    try:
        check_get = requests.get(full_url)
    except Exception:
        return json.dumps(error_list)

    if check_get.status_code == 200:
        pass
    elif check_get.status_code != 200:
        return json.dumps(error_list)
    
    allow_robots_list = []
    disallow_robots_list = []
    dir_wordlist_location = "wordlists/directory.txt"
    sub_wordlist_location = "wordlists/subdomain.txt"

    if not mode or not full_url:
        return jsonify(json.dumps(error_list))
    if mode == 'href_spider':
        href_list = href_spider(full_url)
        return jsonify(json.dumps(href_list))
    if mode == 'sitemap':
        sitemap_list = get_sitemap(full_url)
        return jsonify(json.dumps(sitemap_list))
    if mode == 'http_header_data':
        http_header_data_dict = http_header_data(full_url)
        return jsonify(json.dumps(dict(http_header_data_dict)))
    if mode == 'allow_robots':
        get_robots(full_url, allow_robots_list, disallow_robots_list)
        return jsonify(json.dumps(allow_robots_list))
    if mode == 'disallow_robots':
        get_robots(full_url, allow_robots_list, disallow_robots_list)
        return jsonify(json.dumps(disallow_robots_list))
    if mode == 'form_count':
        form_int = form_spider(full_url)
        return jsonify(json.dumps(form_int))
    if mode == 'dir_enum':
        dir_dict = dir_enum(full_url, dir_wordlist_location)
        return jsonify(json.dumps(dict(dir_dict)))
    if mode == 'sub_enum':
        sub_dict = sub_enum(full_url, sub_wordlist_location)
        return jsonify(json.dumps(dict(sub_dict)))
    else:
        return jsonify(json.dumps(error_list))
    
@app.errorhandler(404)
def error_handler(error):
    return render_template('404_error_page.html'), 404






