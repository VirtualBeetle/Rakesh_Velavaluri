from urllib.parse import urlencode
from urllib.request import urlopen
import json

url = "http://localhost:8090/primes&url=http://localhost:8090/fibo&url=http://localhost:8090/odd"
stp=url.split("&url=")
print(stp)

for i in range(0,len(stp)):
    response = urlopen(stp)
    data_json = json.loads(response.read())
    print(data_json)