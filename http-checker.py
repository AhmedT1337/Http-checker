import requests
from sys import argv
from art import tprint

tprint("Http-Checker")
print("           Coded by: Ahmed Tareq\n\n")

domains = open(argv[1], "r").read().splitlines()

for domain in domains :
    if "http://" or "https://" not in domain :
        domain_1 = "http://" + domain
        domain_2 = "https://" + domain
    try :
        status_1 = requests.get(domain_1, timeout = 1)
        status_2 = requests.get(domain_2, timeout = 1)
        print(f"{domain}, http: {status_1.status_code}, https: {status_2.status_code}\n")
    except :
        print(f"{domain} doesn't work\n")