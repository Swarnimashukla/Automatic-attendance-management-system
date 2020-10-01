import sys
import os, time
import cognitive_face as CF
import global_variables as global_var
import urllib
import sqlite3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


Key = global_var.key

CF.Key.set(Key)

BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

def get_person_id():
	person_id = ''
	extractId = str(sys.argv[1])[-2:]
	connect = sqlite3.connect("Face-DataBase")
	c = connect.cursor()
	cmd = "SELECT * FROM Students WHERE ID = " + extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	connect.close()
	return person_id

if len(sys.argv) is not 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1]))
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
        	print(filename)
        	imgurl = urllib.request.pathname2url(os.path.join(imageFolder, filename))
        	#imgurl = imgurl[3:]
        	print("imageurl = {}".format(imgurl))
        	res = CF.face.detect(imgurl)
        	if len(res) != 1:
        		print("No face detected in image")
        	else:
        		res = CF.person.add_face(imgurl, global_var.personGroupId, person_id)
        		print(res)	
        	time.sleep(6)
else:
	print("supply attributes please from dataset folder")
