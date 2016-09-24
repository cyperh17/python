from http import client
import json #https://pythonworld.ru/moduli/modul-json.html

#import datetime as dt #other import statement type

#https://docs.python.org/3/library/http.client.html
#http://lecturesnet.readthedocs.io/net/requests.html
#https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP#302

conn = client.HTTPConnection('jsonplaceholder.typicode.com')

try:    
    conn.request('GET', '/users') #request(method, url, body=None, headers={})
    web_response = conn.getresponse() #Returns an HTTPResponse
    r_data = web_response.read().decode('utf-8')
except Exception as ex:
    print('Error occured: ', ex)
else:    
    result = json.loads(r_data) #decoding json

    for user in result:
        print('id: {id}, email: {email}, username: {username}, name: {name}'.format(**user))
finally:
    conn.close()