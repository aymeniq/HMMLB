class ECMP_judge:

	def caculate(self,port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12,flow_rate,src_ip,path):

		#print('flow_rate:'+str(flow_rate))
		#if(flow_rate>10000000):
			if(src_ip == '10.0.0.1' or src_ip == '10.0.0.2' or src_ip == '10.0.0.5' or src_ip == '10.0.0.6'):
				'''
				link1's bandwidth
				'''
				if(src_ip == '10.0.0.1' or src_ip == '10.0.0.5'):

					link1_bandwidth_remain = 100000000 - max(port_rate_2,port_rate_3,port_rate_7,port_rate_11)+flow_rate

				else :
					link1_bandwidth_remain = 100000000 - max(port_rate_2,port_rate_3,port_rate_7,port_rate_11)
				#print(link1_bandwidth_remain)
				

				'''
				link2's bandwidth
				'''
		
				link2_bandwidth_remain = 100000000 - max(port_rate_2,port_rate_4,port_rate_8,port_rate_11)
				#print(link1_bandwidth_remain)		
				'''
				link3's bandwidth

				'''
				if(src_ip == '10.0.0.2' or src_ip == '10.0.0.6'):

					link3_bandwidth_remain = 100000000 - max(port_rate_1,port_rate_5,port_rate_9,port_rate_12)+flow_rate
				else:
					link3_bandwidth_remain = 100000000 - max(port_rate_1,port_rate_5,port_rate_9,port_rate_12)
				#print(link1_bandwidth_remain)
				'''
				link4's bandwidth
				'''
		
				link4_bandwidth_remain = 100000000 - max(port_rate_1,port_rate_6,port_rate_10,port_rate_12)
				#print(link1_bandwidth_remain)

			else :

				'''
				link1's bandwidth
				'''
				link1_bandwidth_remain = 100000000 - max(port_rate_1,port_rate_3,port_rate_7,port_rate_11)
				#print('link1_bandwidth_remain:'+str(link1_bandwidth_remain))
				'''
				link2's bandwidth
				'''
				if(src_ip == '10.0.0.3' or src_ip == '10.0.0.7'):
					link2_bandwidth_remain = 100000000 - max(port_rate_1,port_rate_4,port_rate_8,port_rate_11)+flow_rate
				else:
					link2_bandwidth_remain = 100000000 - max(port_rate_1,port_rate_4,port_rate_8,port_rate_11)
		
				'''
				link3's bandwidth
				'''
		
				link3_bandwidth_remain = 100000000 - max(port_rate_2,port_rate_5,port_rate_9,port_rate_12)
		
				'''
				link4's bandwidth
				'''
				if(src_ip == '10.0.0.4' or src_ip == '10.0.0.8'):
					link4_bandwidth_remain = 100000000 - max(port_rate_2,port_rate_6,port_rate_10,port_rate_12)+flow_rate
				else:
					link4_bandwidth_remain = 100000000 - max(port_rate_2,port_rate_6,port_rate_10,port_rate_12)
			print('link1_bandwidth_remain:'+str(link1_bandwidth_remain))
			print('link2_bandwidth_remain:'+str(link2_bandwidth_remain))
			print('link3_bandwidth_remain:'+str(link3_bandwidth_remain))
			print('link4_bandwidth_remain:'+str(link4_bandwidth_remain))

			if(path == 'S1'):
				if(flow_rate>link1_bandwidth_remain):
					path = 'no available path'
					return path
			if(path == 'S2'):
				if(flow_rate>link2_bandwidth_remain):
					path = 'no available path'
					return path
			if(path == 'S3'):
				if(flow_rate>link3_bandwidth_remain):
					path = 'no available path'
					return path
			if(path == 'S4'):
				if(flow_rate>link4_bandwidth_remain):
					path = 'no available path'
					return path
			return path


