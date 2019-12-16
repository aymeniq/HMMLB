import time
import sys
from time import clock
sys.path.append("/home/ryu/Hedera/")
from observed_link import ryu_bandwidth_monitor
from caculate_FFalgorithm_for_path import FFalgorithm
from flow_entry import RyuUtil
from ECMP import ECMPalgorithm
from ECMP_judge import ECMP_judge

ryu=ryu_bandwidth_monitor('192.168.93.137', '8080')
ffalgorithm = FFalgorithm()
flow_load = RyuUtil('192.168.93.137', '8080')
ECMP = ECMPalgorithm()
ECMP_j = ECMP_judge()

sum_ele_flow = 0
sum_mice_flow = 0
ele_reject = 0
mice_reject = 0
sum_time = 0
route = 0
while(1):

	time.sleep(0.5)
	f3=open('/home/ryu/myapp/flow_src_ip.txt','r')
	f1=open('/home/ryu/myapp/flow_entry_signal.txt','r+')
	f2=open('/home/ryu/myapp/flow_information.txt','r')

	if(f1.read() == '1'):
		udp_src_port = f2.read()
		src_ip = f3.read()
		#start = time.time()
		ryu.get_flow_rate_before(src_ip)
		#finish = time.time()
		#total = finish - start
		time.sleep(0.5)
		ryu.get_flow_rate_after(src_ip)
		flow_rate = ryu.caculate_flow_rate(0.5)

		if(flow_rate > 10000000):
			print("use FFalgorithm")
			FF_start = time.time() 

			sum_ele_flow = sum_ele_flow + 1

			start = time.time()
			ryu.get_databefore(src_ip)
			finish = time.time()
			ryu.get_dataafter(src_ip)
			total = finish - start
			port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12 = ryu.caculate(total)
			
			path = ffalgorithm.caculate_bandwidth(port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12,flow_rate,src_ip)
			if(path == 'no available path'):
				ele_reject = ele_reject + 1
			flow_load.install_flow(udp_src_port,path,src_ip)
			FF_finish = time.time() 
			FF_total = FF_finish - FF_start
			sum_time = sum_time + FF_total
			print('the number of ele_flow is:'+str(sum_ele_flow))
			print('the number of ele_flow_reject is:'+str(ele_reject))
			print('total process time is:'+str(sum_time))
			if(path != 'no available path'):
				f4=open('/home/ryu/myapp/train_data.txt','a')
				if(path == 'S1'):
					route = 1
				if(path == 'S2'):
					route = 2
				if(path == 'S3'):
					route = 3
				if(path == 'S4'):
					route = 4
				if((port_rate_1/100000000) <= 0.2):
					p1 = 1
				if(0.2<(port_rate_1/100000000) <0.5):
					p1 = 2
				if((port_rate_1/100000000) >=0.5):
					p1 = 3		
				if((port_rate_10/100000000) <= 0.2):
					p10 = 1
				if(0.2<(port_rate_10/100000000) <0.5):
					p10 = 2
				if((port_rate_10/100000000) >=0.5):
					p10 = 3	
				if((port_rate_4/100000000) <= 0.2):
					p4 = 1
				if(0.2<(port_rate_4/100000000) <0.5):
					p4 = 2
				if((port_rate_4/100000000) >=0.5):
					p4 = 3	
				if((port_rate_6/100000000) <= 0.2):
					p6 = 1
				if(0.2<(port_rate_6/100000000) <0.5):
					p6 = 2
				if((port_rate_6/100000000) >=0.5):
					p6 = 3	
						
				f4.write(str(route))
				f4.write(str(p1))
				f4.write(str(p10))
				f4.write(str(p4))
				f4.write(str(p6))
				f4.write('1')
				f4.write('1')
				f4.write('\n')
				f4.close

		else:
			print("use ECMP")
			sum_mice_flow = sum_mice_flow +1
			path = ECMP.load_path()
			start = time.time()
			ryu.get_databefore(src_ip)
			finish = time.time()
			ryu.get_dataafter(src_ip)
			total = finish - start
			port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12 = ryu.caculate(total)
			path = ECMP_j.caculate(port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12,flow_rate,src_ip,path)
			if(path == 'no available path'):
				mice_reject = mice_reject + 1
			flow_load.install_flow(udp_src_port,path,src_ip)
			print('the number of mice_flow is:'+str(sum_mice_flow))
			print('the number of mice_flow_reject is:'+str(mice_reject))		
		
		print('the current path is:'+str(path))
		print('the current flow_rate is:'+str(flow_rate))
		f1.write('0')
		f1.close
		f2.close
		f3.close
	else :
		f1.close
		f2.close
		f3.close

