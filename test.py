from requests import post

url = "http://localhost:8000"
data = '{"A":1,"B":2,"C":0,"D":0,"E":6,"F":0,"G":0,"H":0,"I":2}'
r = post(url=url, data=data)
print(r.content)