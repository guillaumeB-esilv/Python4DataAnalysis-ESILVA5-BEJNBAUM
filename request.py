import requests
import json

url = 'http://127.0.0.1:5000/api/'

data = [[634995,0,463,1,0.0,806.0,11.291044776119403,1.0,70.49513846124168,0.0,806.0,7.574626865671642,0.0,69.435826365571,0.0,76.0,2.6044776119402986,0.0,8.50550186882253,0.0,806.0,10.649253731343284,1.0,70.25478763764251,-69.0,806.0,4.970149253731344,0.0,69.85058043098057,0,0,0,0,0,10,132,1,0,24,0,0,0,0,1,0,0,0,0,0,0,0,1,0]]
print(len(data[0]))
j_data = json.dumps(data, separators=(',',':'))
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)





