#

url = 'https://google.com'

# print(url.strip('https://'))

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()
#this way looks clean.


print(url)


