import json

pytojson = lambda q: list(q.values())
jsontopython = lambda webdata: json.load(webdata)