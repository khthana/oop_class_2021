import requests
import json

url = 'https://covid19.ddc.moph.go.th/api/Cases/today-cases-all'

req = requests.get(url)
data = req.json()

print("ผู้ป่วยรายวัน:",data[0]['new_case'])
print("ผู้ป่วยสะสม:",data[0]['total_case'])
print("ผู้เสียชีวิต:",data[0]['new_death'])
print("หายป่วย:",data[0]['new_recovered'])









