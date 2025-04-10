#!/usr/bin/python3

#Instructions :
#
#Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete 
# response to a request).
#Test your code with multiple sites such as google, ynet, imdb, etc.

import requests, time

def time_to_load(url):
    

    start = time.time()
    response = requests.get(url)
    end = time.time()
    code = response.status_code
    if code == 200:
        print(f"Page: {url} Execution time: {end - start:.4f} seconds")
    else:
        print("Error")
time_to_load("https://google.com")
time_to_load("https://ynet.co.il")
time_to_load("https://imdb.com")




