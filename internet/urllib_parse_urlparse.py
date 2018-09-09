import urllib
from urllib.parse import urlparse, urlsplit, urldefrag, \
    urlunparse, urljoin, urlencode, parse_qs, parse_qsl, \
    quote, quote_plus, unquote, unquote_plus

from urllib.request import urlopen

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
parsed_split = urlsplit(url)
parsed_defarag = urldefrag(url)
url_unparsed = urlunparse(parsed)
print(parsed)
print(parsed.username)
print(parsed.password)
print(parsed.hostname)
print(parsed.port)

print(parsed_split)

print(parsed_defarag.url)
print(parsed_defarag.fragment)
url_unparsed = url_unparsed[:]
print("URL UNPARSED: ", url_unparsed)

print(urljoin("http://www.example.com/path/file.html", "anotherfile.html"))
print(urljoin("http://www.example.com/path/file.html", "../anotherfile.html"))

query_args = {"q": "query string", "foo": "bar"}
query_args_seq = {"foo": ["foo1", "foo2"]}
encoded_args = urlencode(query_args)
print("Encoded: ", encoded_args)
print("Single: ", urlencode(query_args_seq))
print("Sequence: ", urlencode(query_args_seq, doseq=True))

encoded = "foo=foo1&foo=foo2"
print("parse_qs: ", parse_qs(encoded))
print("parse_qsl: ", parse_qsl(encoded))

url_spec = "http://localhost:8080/~hellmann/"

print("urlencode(): ", urlencode({"url": url_spec}))
print("quote(): ", quote(url_spec))
print("quote_plus(): ", quote_plus(url_spec))

print(unquote('http%3A//localhost%3A8080/%7Ehellmann/'))
print(unquote_plus('http%3A%2F%2Flocalhost%3A8080%2F%7Ehellmann%2F'))
