from urllib.parse import parse_qs

query = 'name=germey&age=25'
print(parse_qs(query))
