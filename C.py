import http.client

conn = http.client.HTTPSConnection("forecast9.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "forecast9.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

conn.request("GET", "/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))