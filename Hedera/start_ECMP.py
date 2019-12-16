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

sum_ele_flow  = 0
sum_mice_flow = 0
ele_reject  = 0
mice_reject = 0
sum_total_time = 0 
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

		
		
		print("use ECMP")
		ECMP_start = time.time()
		path = ECMP.load_path()
		ECMP_finish = time.time()
		ECMP_total = ECMP_finish - ECMP_start
		sum_total_time = sum_total_time + ECMP_total 
		start = time.time()
		ryu.get_databefore(src_ip)
		finish = time.time()
		ryu.get_dataafter(src_ip)
		total = finish - start
		port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12 = ryu.caculate(total)
		path = ECMP_j.caculate(port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12,flow_rate,src_ip,path)
		if(flow_rate<10000000):
			sum_mice_flow = sum_mice_flow +1
			if(path == 'no available path'):
				mice_reject = mice_reject + 1
			flow_load.install_flow(udp_src_port,path,src_ip)
			print('the number of mice_flow is:'+str(sum_mice_flow))
			print('the number of mice_flow_reject is:'+str(mice_reject))	
		if(flow_rate>10000000):
			sum_ele_flow = sum_ele_flow +1
			if(path == 'no available path'):
				ele_reject = ele_reject + 1
			flow_load.install_flow(udp_src_port,path,src_ip)
			print('the number of ele_flow is:'+str(sum_ele_flow))
			print('the number of ele_flow_reject is:'+str(ele_reject))	
		
		print('the current path is:'+str(path))
		print('the current flow_rate is:'+str(flow_rate))
		print('the sum_time is:'+str(sum_total_time))
		f1.write('0')
		f1.close
		f2.close
		f3.close
	else :
		f1.close
		f2.close
		f3.close

