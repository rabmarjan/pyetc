from kivy.network.urlrequest import UrlRequest

req = UrlRequest("http://localhost:8000/api/v1/contact/")

print(req.req_body)


def got_json(req, result):
    for key, value in result['headers'].items():
        print('{}: {}'.format(key, value))


req = UrlRequest('http://localhost:8000/api/v1/contact/', got_json)
print(req)

import urllib


def bug_posted(req, result):
    print('Our bug is posted!')
    print(result)


params = urllib({
    "contact_id": 10,
    "first_name": "Abdur",
    "last_name": "Rab",
    "middle_name": "Marjan",
    "email": "rab.marjan@gmail.com",
    "country": "Bangladesh",
    "phone": "8801727309106",
    "address": "Dhaka",
    "image": "/media/Images/Screenshot.png"

})
headers = {'Content-type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json'}
req = UrlRequest('http://localhost:8000/api/v1/contact/', on_success=bug_posted, req_body=params,
                 req_headers=headers)
