from urllib.parse import parse_qsl

query = 'name=germey&age=25'
print(parse_qsl(query))
