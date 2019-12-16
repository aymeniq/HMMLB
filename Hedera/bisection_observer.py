import httplib2
import time
import json
from time import clock


class ryu_bisection_monitor:
    url = ''
    data_before   =  [0 for i in range(13)] 	# 0 ~ 13 are S7-PORT2 S5-PORT1 S1-PORT2 S9-PORT4 S11-PORT3 S5-PORT2 S2-PORT4 S7-PORT1 S6-PORT1 S3-PORT1 S10-PORT3 S6-PORT2 S4-PORT2 flow_rate
    data_after    =  [0 for i in range(13)]	#so the link1 is 0 1 2 3 4, link2 is 0 5 6 3 4, link3 is 7 8 9 10 4, link4 is 7 11 12 10 4 flow_rate is 13
	
    def get_bisection_before(self):
		http              = httplib2.Http()
		headers           = {'Accept': 'application/json'}

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/3', headers=headers)    #S1_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[1]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/2', headers=headers)    #S2_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[2]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/3', headers=headers)    #S3_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[3]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/3', headers=headers)    #S4_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[4]    = data['4'][0]['tx_bytes']

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/4', headers=headers)    #S1_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[5]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/3', headers=headers)    #S2_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[6]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/4', headers=headers)    #S3_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[7]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/4', headers=headers)    #S4_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[8]    = data['4'][0]['tx_bytes']	
    def get_bisection_after(self):
		http              = httplib2.Http()
		headers           = {'Accept': 'application/json'}

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/3', headers=headers)    #S1_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[1]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/2', headers=headers)    #S2_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[2]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/3', headers=headers)    #S3_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[3]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/3', headers=headers)    #S4_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[4]    = data['4'][0]['tx_bytes']

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/4', headers=headers)    #S1_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[5]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/3', headers=headers)    #S2_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[6]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/4', headers=headers)    #S3_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[7]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/4', headers=headers)    #S4_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[8]    = data['4'][0]['tx_bytes']
    def caculate(self,time):
	S1_2 = float((self.data_after[1]-self.data_before[1])*8/time)
	S2_2 = float((self.data_after[2]-self.data_before[2])*8/time)
	S3_3 = float((self.data_after[3]-self.data_before[3])*8/time)
	S4_3 = float((self.data_after[4]-self.data_before[4])*8/time)
	S1_4 = float((self.data_after[5]-self.data_before[5])*8/time)
	S2_3 = float((self.data_after[6]-self.data_before[6])*8/time)
	S3_4 = float((self.data_after[7]-self.data_before[7])*8/time)
	S4_4 = float((self.data_after[8]-self.data_before[8])*8/time)
	print(S1_2,S2_2,S3_3,S4_3,S1_4,S2_3,S3_4,S4_4)

ryu = ryu_bisection_monitor()
ryu.get_bisection_before()
time.sleep(10)
ryu.get_bisection_after()
ryu.caculate(10)



