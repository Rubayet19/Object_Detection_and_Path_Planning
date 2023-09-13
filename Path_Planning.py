import requests

url = "https://graphhopper.com/api/1/route"

query = {
  "profile": "car",
  "point": ["23.810059, 90.413589", "23.781070,90.407170"],
  "locale": "en",
  "elevation": "false",
  "optimize": "false",
  "instructions": "true",
  "calc_points": "true",
  "debug": "false",
  "points_encoded": "true",
  "ch.disable": "false",
  "pass_through": "false",
  "algorithm": "alternative_route",
  "alternative_route.max_paths": "2",
  "alternative_route.max_weight_factor": "1.4",
  "alternative_route.max_share_factor": "0.6",
  "key": "a5ba8cae-bfea-4ff2-92a0-ec654bb16f4e"
}

response = requests.get(url, params=query)
data = response.json()

route=data["paths"][0]["instructions"]
keys_to_keep = ['distance', 'heading', 'text']
new_list = [{k: d[k] for k in keys_to_keep if k in d} for d in route]
for d in new_list:
    for k, v in d.items():
        print(k, v)
    print("")
