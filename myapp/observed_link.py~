import httplib2
import time
import json
from time import clock


class ryu_bandwidth_monitor:
    url = ''
    data_before   =  [0 for i in range(13)] 	# 0 ~ 13 are S7-PORT2 S5-PORT1 S1-PORT2 S9-PORT4 S11-PORT3 S5-PORT2 S2-PORT4 S7-PORT1 S6-PORT1 S3-PORT1 S10-PORT3 S6-PORT2 S4-PORT2 flow_rate
    data_after    =  [0 for i in range(13)]	#so the link1 is 0 1 2 3 4, link2 is 0 5 6 3 4, link3 is 7 8 9 10 4, link4 is 7 11 12 10 4 flow_rate is 13

    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + str(port) + '/index.html'

    def get_flow_rate_before(self,src_ip):
	http              = httplib2.Http()
	headers           = {'Accept': 'application/json'}
	if(src_ip == '10.0.0.1'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/7', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
					
		while(data['7'][k]['cookie'] != 10):
			k = k+1
		self.data_before[12]    = data['7'][k]['byte_count']			#need revise
					
	if(src_ip == '10.0.0.2'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/7', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['7'][k]['cookie'] != 11):
			k = k+1
		self.data_before[12]    = data['7'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.3'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/8', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['8'][k]['cookie'] != 11):
			k = k+1
		self.data_before[12]    = data['8'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.4'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/8', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['8'][k]['cookie'] != 10):
			k = k+1
		self.data_before[12]    = data['8'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.5'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/11', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['11'][k]['cookie'] != 11):
			k = k+1
		self.data_before[12]    = data['11'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.6'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/11', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['11'][k]['cookie'] != 10):
			k = k+1
		self.data_before[12]    = data['11'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.7'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/12', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['12'][k]['cookie'] != 10):
			k = k+1
		self.data_before[12]    = data['12'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.8'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/12', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['12'][k]['cookie'] != 11):
			k = k+1
		self.data_before[12]    = data['12'][k]['byte_count']			#need revise
	#print(self.data_before[12])

    def get_flow_rate_after(self,src_ip):
	http              = httplib2.Http()
	headers           = {'Accept': 'application/json'}
	if(src_ip == '10.0.0.1'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/7', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
					
		while(data['7'][k]['cookie'] != 10):
			k = k+1
		self.data_after[12]    = data['7'][k]['byte_count']			#need revise
					
	if(src_ip == '10.0.0.2'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/7', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['7'][k]['cookie'] != 11):
			k = k+1
		self.data_after[12]    = data['7'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.3'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/8', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['8'][k]['cookie'] != 11):
			k = k+1
		self.data_after[12]    = data['8'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.4'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/8', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['8'][k]['cookie'] != 10):
			k = k+1
		self.data_after[12]    = data['8'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.5'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/11', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['11'][k]['cookie'] != 11):
			k = k+1
		self.data_after[12]    = data['11'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.6'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/11', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['11'][k]['cookie'] != 10):
			k = k+1
		self.data_after[12]    = data['11'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.7'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/12', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['12'][k]['cookie'] != 10):
			k = k+1
		self.data_after[12]    = data['12'][k]['byte_count']			#need revise

	if(src_ip == '10.0.0.8'):
		response, content = http.request(uri='http://192.168.93.137:8080/stats/flow/12', headers=headers)    #observed the flow_rate,this code need revise
		json_data         = content.decode()
		data              = json.loads(json_data)
		k = 0
		while(data['12'][k]['cookie'] != 11):
			k = k+1
		self.data_after[12]    = data['12'][k]['byte_count']			#need revise
	#print(self.data_after[12])
    def caculate_flow_rate(self,time):
	flow_rate = float((self.data_after[12]-self.data_before[12])*8/time)
	return flow_rate


    def get_databefore(self,src_ip):
	http              = httplib2.Http()
	headers           = {'Accept': 'application/json'}
	if(src_ip == '10.0.0.1' or src_ip == '10.0.0.2' or src_ip == '10.0.0.3' or src_ip == '10.0.0.4'):
		if(src_ip == '10.0.0.1' or src_ip == '10.0.0.2'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/7/1', headers=headers)    #S7_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[0]    = data['7'][0]['tx_bytes'] 			

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/7/2', headers=headers)    #S7_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[1]    = data['7'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/13/4', headers=headers)    #S13_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[10]    = data['13'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/14/3', headers=headers)    #S14_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[11]    = data['14'][0]['tx_bytes']
				
		if(src_ip == '10.0.0.3' or src_ip == '10.0.0.4'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/8/1', headers=headers)    #S8_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[0]    = data['8'][0]['tx_bytes'] 			
	
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/8/2', headers=headers)    #S8_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[1]    = data['8'][0]['tx_bytes'] 
			
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/13/3', headers=headers)    #S13_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[10]    = data['13'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/14/4', headers=headers)    #S14_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[11]    = data['14'][0]['tx_bytes']
				
				
						
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/5/1', headers=headers)    #S5_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[2]    = data['5'][0]['tx_bytes'] 	

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/5/2', headers=headers)    #S5_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[3]    = data['5'][0]['tx_bytes'] 			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/6/1', headers=headers)    #S6_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[4]    = data['6'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/6/2', headers=headers)    #S6_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[5]    = data['6'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/3', headers=headers)    #S1_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[6]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/2', headers=headers)    #S2_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[7]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/3', headers=headers)    #S3_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[8]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/3', headers=headers)    #S4_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[9]    = data['4'][0]['tx_bytes']

	if(src_ip == '10.0.0.5' or src_ip == '10.0.0.6' or src_ip == '10.0.0.7' or src_ip == '10.0.0.8'):
		if(src_ip == '10.0.0.5' or src_ip == '10.0.0.6'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/11/1', headers=headers)    #S11_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[0]    = data['11'][0]['tx_bytes'] 			

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/11/2', headers=headers)    #S11_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[1]    = data['11'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/17/4', headers=headers)    #S17_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[10]    = data['17'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/18/3', headers=headers)    #S18_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[11]    = data['18'][0]['tx_bytes']
				


		if(src_ip == '10.0.0.7' or src_ip == '10.0.0.8'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/12/1', headers=headers)    #S12_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[0]    = data['12'][0]['tx_bytes'] 			
	
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/12/2', headers=headers)    #S12_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[1]    = data['12'][0]['tx_bytes'] 
			
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/17/3', headers=headers)    #S17_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[10]    = data['17'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/18/4', headers=headers)    #S18_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_before[11]    = data['18'][0]['tx_bytes']
				
						
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/9/1', headers=headers)    #S9_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[2]    = data['9'][0]['tx_bytes'] 	

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/9/2', headers=headers)    #S9_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[3]    = data['9'][0]['tx_bytes'] 			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/10/1', headers=headers)    #S10_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[4]    = data['10'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/10/2', headers=headers)    #S10_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[5]    = data['10'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/4', headers=headers)    #S1_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[6]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/3', headers=headers)    #S2_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[7]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/4', headers=headers)    #S3_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[8]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/4', headers=headers)    #S4_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_before[9]    = data['4'][0]['tx_bytes']	




    def get_dataafter(self,src_ip):
	http              = httplib2.Http()
	headers           = {'Accept': 'application/json'}

	if(src_ip == '10.0.0.1' or src_ip == '10.0.0.2' or src_ip == '10.0.0.3' or src_ip == '10.0.0.4'):
		if(src_ip == '10.0.0.1' or src_ip == '10.0.0.2'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/7/1', headers=headers)    #S7_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[0]    = data['7'][0]['tx_bytes'] 			

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/7/2', headers=headers)    #S7_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[1]    = data['7'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/13/4', headers=headers)    #S13_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[10]    = data['13'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/14/3', headers=headers)    #S14_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[11]    = data['14'][0]['tx_bytes']

		if(src_ip == '10.0.0.3' or src_ip == '10.0.0.4'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/8/1', headers=headers)    #S8_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[0]    = data['8'][0]['tx_bytes'] 			
	
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/8/2', headers=headers)    #S8_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[1]    = data['8'][0]['tx_bytes'] 
			
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/13/3', headers=headers)    #S13_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[10]    = data['13'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/14/4', headers=headers)    #S14_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[11]    = data['14'][0]['tx_bytes']
						
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/5/1', headers=headers)    #S5_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[2]    = data['5'][0]['tx_bytes'] 	

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/5/2', headers=headers)    #S5_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[3]    = data['5'][0]['tx_bytes'] 			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/6/1', headers=headers)    #S6_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[4]    = data['6'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/6/2', headers=headers)    #S6_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[5]    = data['6'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/3', headers=headers)    #S1_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[6]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/2', headers=headers)    #S2_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[7]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/3', headers=headers)    #S3_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[8]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/3', headers=headers)    #S4_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[9]    = data['4'][0]['tx_bytes']

	if(src_ip == '10.0.0.5' or src_ip == '10.0.0.6' or src_ip == '10.0.0.7' or src_ip == '10.0.0.8'):
		if(src_ip == '10.0.0.5' or src_ip == '10.0.0.6'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/11/1', headers=headers)    #S11_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[0]    = data['11'][0]['tx_bytes'] 			

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/11/2', headers=headers)    #S11_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[1]    = data['11'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/17/4', headers=headers)    #S17_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[10]    = data['17'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/18/3', headers=headers)    #S18_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[11]    = data['18'][0]['tx_bytes']

		if(src_ip == '10.0.0.7' or src_ip == '10.0.0.8'):
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/12/1', headers=headers)    #S12_Port1
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[0]    = data['12'][0]['tx_bytes'] 			
	
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/12/2', headers=headers)    #S12_Port2
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[1]    = data['12'][0]['tx_bytes'] 
			
				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/17/3', headers=headers)    #S17_Port3
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[10]    = data['17'][0]['tx_bytes']

				response, content = http.request(uri='http://192.168.93.137:8080/stats/port/18/4', headers=headers)    #S18_Port4
				json_data         = content.decode()
				data              = json.loads(json_data)
				self.data_after[11]    = data['18'][0]['tx_bytes']
				

						
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/9/1', headers=headers)    #S9_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[2]    = data['9'][0]['tx_bytes'] 	

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/9/2', headers=headers)    #S9_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[3]    = data['9'][0]['tx_bytes'] 			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/10/1', headers=headers)    #S10_Port1
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[4]    = data['10'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/10/2', headers=headers)    #S10_Port2
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[5]    = data['10'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/1/4', headers=headers)    #S1_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[6]    = data['1'][0]['tx_bytes'] 

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/2/3', headers=headers)    #S2_Port3
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[7]    = data['2'][0]['tx_bytes']	
					
		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/3/4', headers=headers)    #S3_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[8]    = data['3'][0]['tx_bytes']			

		response, content = http.request(uri='http://192.168.93.137:8080/stats/port/4/4', headers=headers)    #S4_Port4
		json_data         = content.decode()
		data              = json.loads(json_data)
		self.data_after[9]    = data['4'][0]['tx_bytes']	




    def caculate(self,time):
	#file = open('/home/ryu/myapp/observed_state.txt','w')
	port_rate_1 = float((self.data_after[0]-self.data_before[0])*8/time)    # 0 ~ 12 are S7-PORT2 S5-PORT1 S1-PORT2 S9-PORT4 S11-PORT3 S5-PORT2 S2-PORT4 S7-PORT1 S6-PORT1 S3-PORT1 S10-PORT3 S6-PORT2 S4-PORT2
	port_rate_2 = float((self.data_after[1]-self.data_before[1])*8/time)
	port_rate_3 = float((self.data_after[2]-self.data_before[2])*8/time)
	port_rate_4 = float((self.data_after[3]-self.data_before[3])*8/time)
	port_rate_5 = float((self.data_after[4]-self.data_before[4])*8/time)
	port_rate_6 = float((self.data_after[5]-self.data_before[5])*8/time)
	port_rate_7 = float((self.data_after[6]-self.data_before[6])*8/time)
	port_rate_8 = float((self.data_after[7]-self.data_before[7])*8/time)
	port_rate_9 = float((self.data_after[8]-self.data_before[8])*8/time)
	port_rate_10 = float((self.data_after[9]-self.data_before[9])*8/time)
	port_rate_11 = float((self.data_after[10]-self.data_before[10])*8/time)
	port_rate_12 = float((self.data_after[11]-self.data_before[11])*8/time)

	#file.write(str(S7_PORT1)+'\n'+str(S4_PORT2)+'\n'+str(S5_PORT2)+'\n'+str(S6_PORT2)+'\n'+'1'+'\n'+'1'+'\n')
	#file.close		
	#print(S11_PORT3/(1000*1000))
	return port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12

#ryu=ryu_bandwidth_monitor('192.168.93.137', '8080')
#start = time.time()
#ryu.get_databefore('10.0.0.1')
#finish = time.time()
#ryu.get_dataafter('10.0.0.1')

#time = finish-start
#print(time)
#ryu.caculate(time)


