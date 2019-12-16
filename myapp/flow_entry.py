import httplib2
import time
import linecache

class RyuUtil:
    url = ''


    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + str(port)
    def install_flow(self, udp,path_load,src_ip):
        http = httplib2.Http()
        headers    = {'Accept': 'application/json'}
	udp_number = str(udp)
	path       = str(path_load)
	src_ip     = str(src_ip)
	#f3=open('/home/ryu/myapp/flow_src_ip.txt','r')
	#src_ip = f3.read()
	if(src_ip == '10.0.0.1'):
		dst_ip = '10.0.0.9'			
		if(path == 'S1'):
			first_switch  = '7'
			second_switch = '5'
			third_switch  = '1'
			forth_switch  = '13'
			fifth_switch  = '15'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '3'

		if(path == 'S2'):
			first_switch  = '7'
			second_switch = '5'
			third_switch  = '2'
			forth_switch  = '13'
			fifth_switch  = '15'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '2'
			port_4	      = '4'
			port_5	      = '3'
		if(path == 'S3'):
			first_switch  = '7'
			second_switch = '6'
			third_switch  = '3'
			forth_switch  = '14'
			fifth_switch  = '15'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '3'
		if(path == 'S4'):
			first_switch  = '7'
			second_switch = '6'
			third_switch  = '4'
			forth_switch  = '14'
			fifth_switch  = '15'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '3'	
		if(path == 'no available path'):
			first_switch  = '7'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path

	if(src_ip == '10.0.0.2'):
		dst_ip = '10.0.0.10'			
		if(path == 'S1'):
			first_switch  = '7'
			second_switch = '5'
			third_switch  = '1'
			forth_switch  = '13'
			fifth_switch  = '15'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '4'

		if(path == 'S2'):
			first_switch  = '7'
			second_switch = '5'
			third_switch  = '2'
			forth_switch  = '13'
			fifth_switch  = '15'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '2'
			port_4	      = '4'
			port_5	      = '4'
		if(path == 'S3'):
			first_switch  = '7'
			second_switch = '6'
			third_switch  = '3'
			forth_switch  = '14'
			fifth_switch  = '15'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '4'
		if(path == 'S4'):
			first_switch  = '7'
			second_switch = '6'
			third_switch  = '4'
			forth_switch  = '14'
			fifth_switch  = '15'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '4'	
		if(path == 'no available path'):
			first_switch  = '7'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path

	if(src_ip == '10.0.0.3'):	
		dst_ip = '10.0.0.11'		
		if(path == 'S1'):
			first_switch  = '8'
			second_switch = '5'
			third_switch  = '1'
			forth_switch  = '13'
			fifth_switch  = '16'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '3'

		if(path == 'S2'):
			first_switch  = '8'
			second_switch = '5'
			third_switch  = '2'
			forth_switch  = '13'
			fifth_switch  = '16'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '2'
			port_4	      = '3'
			port_5	      = '3'
		if(path == 'S3'):
			first_switch  = '8'
			second_switch = '6'
			third_switch  = '3'
			forth_switch  = '14'
			fifth_switch  = '16'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '3'
		if(path == 'S4'):
			first_switch  = '8'
			second_switch = '6'
			third_switch  = '4'
			forth_switch  = '14'
			fifth_switch  = '16'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '3'	
		if(path == 'no available path'):
			first_switch  = '8'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path

	if(src_ip == '10.0.0.4'):
		dst_ip = '10.0.0.12'			
		if(path == 'S1'):
			first_switch  = '8'
			second_switch = '5'
			third_switch  = '1'
			forth_switch  = '13'
			fifth_switch  = '16'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '4'

		if(path == 'S2'):
			first_switch  = '8'
			second_switch = '5'
			third_switch  = '2'
			forth_switch  = '13'
			fifth_switch  = '16'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '2'
			port_4	      = '3'
			port_5	      = '4'
		if(path == 'S3'):
			first_switch  = '8'
			second_switch = '6'
			third_switch  = '3'
			forth_switch  = '14'
			fifth_switch  = '16'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '4'
		if(path == 'S4'):
			first_switch  = '8'
			second_switch = '6'
			third_switch  = '4'
			forth_switch  = '14'
			fifth_switch  = '16'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '4'	
		if(path == 'no available path'):
			first_switch  = '8'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path

	if(src_ip == '10.0.0.5'):
		dst_ip = '10.0.0.13'			
		if(path == 'S1'):
			first_switch  = '11'
			second_switch = '9'
			third_switch  = '1'
			forth_switch  = '17'
			fifth_switch  = '19'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '4'
			port_5	      = '3'

		if(path == 'S2'):
			first_switch  = '11'
			second_switch = '9'
			third_switch  = '2'
			forth_switch  = '17'
			fifth_switch  = '19'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '3'
		if(path == 'S3'):
			first_switch  = '11'
			second_switch = '10'
			third_switch  = '3'
			forth_switch  = '18'
			fifth_switch  = '19'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '3'
			port_5	      = '3'
		if(path == 'S4'):
			first_switch  = '11'
			second_switch = '10'
			third_switch  = '4'
			forth_switch  = '18'
			fifth_switch  = '19'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '4'
			port_4	      = '3'
			port_5	      = '3'	
		if(path == 'no available path'):
			first_switch  = '11'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path

	if(src_ip == '10.0.0.6'):
		dst_ip = '10.0.0.14'			
		if(path == 'S1'):
			first_switch  = '11'
			second_switch = '9'
			third_switch  = '1'
			forth_switch  = '17'
			fifth_switch  = '19'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '4'
			port_5	      = '4'

		if(path == 'S2'):
			first_switch  = '11'
			second_switch = '9'
			third_switch  = '2'
			forth_switch  = '17'
			fifth_switch  = '19'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '4'
			port_5	      = '4'
		if(path == 'S3'):
			first_switch  = '11'
			second_switch = '10'
			third_switch  = '3'
			forth_switch  = '18'
			fifth_switch  = '19'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '3'
			port_5	      = '4'
		if(path == 'S4'):
			first_switch  = '11'
			second_switch = '10'
			third_switch  = '4'
			forth_switch  = '18'
			fifth_switch  = '19'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '4'
			port_4	      = '3'
			port_5	      = '4'	
		if(path == 'no available path'):
			first_switch  = '11'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path

	if(src_ip == '10.0.0.7'):
		dst_ip = '10.0.0.15'			
		if(path == 'S1'):
			first_switch  = '12'
			second_switch = '9'
			third_switch  = '1'
			forth_switch  = '17'
			fifth_switch  = '20'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '3'
			port_5	      = '3'

		if(path == 'S2'):
			first_switch  = '12'
			second_switch = '9'
			third_switch  = '2'
			forth_switch  = '17'
			fifth_switch  = '20'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '3'
		if(path == 'S3'):
			first_switch  = '12'
			second_switch = '10'
			third_switch  = '3'
			forth_switch  = '18'
			fifth_switch  = '20'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '4'
			port_5	      = '3'
		if(path == 'S4'):
			first_switch  = '12'
			second_switch = '10'
			third_switch  = '4'
			forth_switch  = '18'
			fifth_switch  = '20'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '4'
			port_4	      = '4'
			port_5	      = '3'	
		if(path == 'no available path'):
			first_switch  = '12'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path

	if(src_ip == '10.0.0.8'):
		dst_ip = '10.0.0.16'			
		if(path == 'S1'):
			first_switch  = '12'
			second_switch = '9'
			third_switch  = '1'
			forth_switch  = '17'
			fifth_switch  = '20'
			port_1        = '1'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '3'
			port_5	      = '4'

		if(path == 'S2'):
			first_switch  = '12'
			second_switch = '9'
			third_switch  = '2'
			forth_switch  = '17'
			fifth_switch  = '20'
			port_1        = '1'
			port_2	      = '2'
			port_3	      = '3'
			port_4	      = '3'
			port_5	      = '4'
		if(path == 'S3'):
			first_switch  = '12'
			second_switch = '10'
			third_switch  = '3'
			forth_switch  = '18'
			fifth_switch  = '20'
			port_1        = '2'
			port_2	      = '1'
			port_3	      = '4'
			port_4	      = '4'
			port_5	      = '4'
		if(path == 'S4'):
			first_switch  = '12'
			second_switch = '10'
			third_switch  = '4'
			forth_switch  = '18'
			fifth_switch  = '20'
			port_1        = '2'
			port_2	      = '2'
			port_3	      = '4'
			port_4	      = '4'
			port_5	      = '4'	
		if(path == 'no available path'):
			first_switch  = '12'
			switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "DROP"}]}'
			response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
			return path
	#print(first_switch)
        switch_1 ='{"dpid": '+first_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "OUTPUT","port": '+port_1+'}]}'

	
        switch_2 ='{"dpid": '+second_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "OUTPUT","port": '+port_2+'}]}'

        switch_3 ='{"dpid": '+third_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "OUTPUT","port": '+port_3+'}]}'

        switch_4 ='{"dpid": '+forth_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "OUTPUT","port": '+port_4+'}]}'

        switch_5 ='{"dpid": '+fifth_switch+',"cookie": 100,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"'+src_ip+'","nw_dst":"'+dst_ip+'","nw_proto":17,"udp_dst":5001,"udp_src":'+udp_number+'},"actions":[{ "type": "OUTPUT","port": '+port_5+'}]}'

	response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_4, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=switch_5, method='POST',headers=headers)
	
#ryu = RyuUtil('192.168.93.137', '8080')
#ryu.install_flow('11111','S4','10.0.0.1')
