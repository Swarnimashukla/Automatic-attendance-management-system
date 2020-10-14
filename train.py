import cognitive_face as CF
import global_variables as global_var
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

Key = global_var.key

CF.Key.set(Key)

BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


res = CF.person_group.train(global_var.personGroupId)
print(res)
