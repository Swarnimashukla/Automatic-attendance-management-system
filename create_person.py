import sys
import cognitive_face as CF
import global_variables as global_var
import sqlite3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


Key = global_var.key

CF.Key.set(Key)

BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

print("personGroupId = %s" %(global_var.personGroupId))

if len(sys.argv) is not 1:
    res = CF.person.create(global_var.personGroupId, str(sys.argv[1]))
    #print("res = {}".format(res)) 
    print(res)
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res['personId'], extractId))
    connect.commit()                                                            # commiting into the database
    connect.close()
    print("Person ID successfully added to the database")
else:
    print("please specify parameters ie userId of person to add from database directory")
