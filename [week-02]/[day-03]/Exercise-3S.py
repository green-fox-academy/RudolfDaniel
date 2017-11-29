url = "https//www.reddit.com/r/nevertellmethebots"

url = url[0:4] + str(":") + url[6:]
url = url[:-4]
url = url + str("odds")

print(url)