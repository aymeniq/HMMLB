import time
import sys
sys.path.append("/home/ryu/myapp/")
from observed_state import ryu_bandwidth_monitor
from observed_link import judge_ryu_bandwidth_monitor
from hmm_application import HmmApplication
from flow_entry import RyuUtil
from HMM_judge import HMM_judge
from ECMP import ECMPalgorithm

ECMP = ECMPalgorithm()
judge = judge_ryu_bandwidth_monitor('192.168.93.137', '8080')
judge_for_HMM = HMM_judge()
ryu = ryu_bandwidth_monitor('192.168.93.137', '8080')
hmm = HmmApplication()
flow_load = RyuUtil('192.168.93.137', '8080')

sum_ele_flow = 0
sum_mice_flow = 2
ele_reject = 0
mice_reject = 0
sum_time = 0
while(1):
	time.sleep(0.5)
	f3=open('/home/ryu/myapp/flow_src_ip.txt','r')
	f1=open('/home/ryu/myapp/flow_entry_signal.txt','r+')
	f2=open('/home/ryu/myapp/flow_information.txt','r')
	if(f1.read() == '1'):
		udp_src_port = f2.read()
		src_ip = f3.read()

		ryu.get_flow_rate_before(src_ip)
		time.sleep(0.5)
		ryu.get_flow_rate_after(src_ip)
		flow_rate = ryu.caculate_flow_rate(0.5)
		if(flow_rate > 10000000):
			print("use Binjie_method")

			Binjie_start = time.time() 

			sum_ele_flow = sum_ele_flow + 1
			
			a = time.time()
			ryu.get_databefore(src_ip)
			b = time.time()
			time.sleep(0.1)
			total = b - a + 0.1
			ryu.get_dataafter(src_ip)
			p1,p10,p4,p6 = ryu.caculate(total)
			hmm.get_parameter(p1,p10,p4,p6,1,1)
			path = hmm.caculation()

			Binjie_finish = time.time() 
			Binjie_total = Binjie_finish - Binjie_start
			sum_time = sum_time + Binjie_total



			start = time.time()
			judge.get_databefore(src_ip)
			finish = time.time()
			judge.get_dataafter(src_ip)
			total = finish - start
			port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12 = judge.caculate(total)
			path = judge_for_HMM.caculate(port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12,flow_rate,src_ip,path)
			if(path == 'no available path'):
				ele_reject = ele_reject + 1

			Binjie_start = time.time() 
			flow_load.install_flow(udp_src_port,path,src_ip)
			Binjie_finish = time.time() 
			Binjie_total = Binjie_finish - Binjie_start
			sum_time = sum_time + Binjie_total
			print('the number of ele_flow is:'+str(sum_ele_flow))
			print('the number of ele_flow_reject is:'+str(ele_reject))
			print('total process time is:'+str(sum_time))

		else:
			print("use ECMP")
			sum_mice_flow = sum_mice_flow +1
			path = ECMP.load_path()
			start = time.time()
			judge.get_databefore(src_ip)
			finish = time.time()
			judge.get_dataafter(src_ip)
			total = finish - start
			port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12 = judge.caculate(total)
			path = judge_for_HMM.caculate(port_rate_1,port_rate_2,port_rate_3,port_rate_4,port_rate_5,port_rate_6,port_rate_7,port_rate_8,port_rate_9,port_rate_10,port_rate_11,port_rate_12,flow_rate,src_ip,path)
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

