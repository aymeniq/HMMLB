import httplib2
import time

class RyuUtil:
    url = ''


    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + str(port)
    def install_flow(self, container_name='default'):
        http = httplib2.Http()
        headers = {'Accept': 'application/json'}
	#switch of type 1

        initial_s7_body1 ='{"dpid": 7,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'
        initial_s7_body2 ='{"dpid": 7,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s7_body3 ='{"dpid": 7,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s7_body4 ='{"dpid": 7,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'
        #initial_s7_body3 ='{"dpid": 7,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42317},"actions":[{ "type": "OUTPUT","port": 2}]}' #Line 1/s7
        #initial_s7_body4 ='{"dpid": 7,"cookie": 4,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42302},"actions":[{ "type": "OUTPUT","port": 2}]}' #Line 2/s7
        #initial_s7_body5 ='{"dpid": 7,"cookie": 5,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":36763},"actions":[{ "type": "OUTPUT","port": 1}]}' #Line 3/s7
        #initial_s7_body6 ='{"dpid": 7,"cookie": 6,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":37855},"actions":[{ "type": "OUTPUT","port": 1}]}' #Line 4/s7

        initial_s8_body1 ='{"dpid": 8,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s8_body2 ='{"dpid": 8,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s8_body3 ='{"dpid": 8,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s8_body4 ='{"dpid": 8,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'

        initial_s11_body1 ='{"dpid": 11,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'
        initial_s11_body2 ='{"dpid": 11,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s11_body3 ='{"dpid": 11,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s11_body4 ='{"dpid": 11,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'

        initial_s12_body1 ='{"dpid": 12,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s12_body2 ='{"dpid": 12,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s12_body3 ='{"dpid": 12,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s12_body4 ='{"dpid": 12,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'

        initial_s16_body1 ='{"dpid": 16,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s16_body2 ='{"dpid": 16,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s16_body3 ='{"dpid": 16,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s16_body4 ='{"dpid": 16,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'

        initial_s19_body1 ='{"dpid": 19,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s19_body2 ='{"dpid": 19,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'
        initial_s19_body3 ='{"dpid": 19,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s19_body4 ='{"dpid": 19,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'

        initial_s20_body1 ='{"dpid": 20,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s20_body2 ='{"dpid": 20,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s20_body3 ='{"dpid": 20,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s20_body4 ='{"dpid": 20,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'

        initial_s15_body1 ='{"dpid": 15,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'
        initial_s15_body2 ='{"dpid": 15,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s15_body3 ='{"dpid": 15,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s15_body4 ='{"dpid": 15,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'
        #initial_s11_body3 ='{"dpid": 11,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42317},"actions":[{ "type": "OUTPUT","port": 3}]}' #Line 1/s11
        #initial_s11_body4 ='{"dpid": 11,"cookie": 4,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42302},"actions":[{ "type": "OUTPUT","port": 3}]}' #Line 2/s11
        #initial_s11_body5 ='{"dpid": 11,"cookie": 5,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":36763},"actions":[{ "type": "OUTPUT","port": 3}]}' #Line 3/s11
        #initial_s11_body6 ='{"dpid": 11,"cookie": 6,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":37855},"actions":[{ "type": "OUTPUT","port": 3}]}' #Line 4/s11


	#switch of type 2
        initial_s5_body1 ='{"dpid": 5,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s5_body2 ='{"dpid": 5,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s5_body3 ='{"dpid": 5,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s5_body4 ='{"dpid": 5,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'
        #initial_s5_body3 ='{"dpid": 5,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42317},"actions":[{ "type": "OUTPUT","port": 1}]}' #Line 1/s5
        #initial_s5_body4 ='{"dpid": 5,"cookie": 4,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42302},"actions":[{ "type": "OUTPUT","port": 2}]}' #Line 2/s5

        initial_s9_body1 ='{"dpid": 9,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s9_body2 ='{"dpid": 9,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s9_body3 ='{"dpid": 9,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s9_body4 ='{"dpid": 9,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'

        initial_s10_body1 ='{"dpid": 10,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s10_body2 ='{"dpid": 10,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s10_body3 ='{"dpid": 10,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s10_body4 ='{"dpid": 10,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'

        initial_s6_body1 ='{"dpid": 6,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s6_body2 ='{"dpid": 6,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s6_body3 ='{"dpid": 6,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'
        initial_s6_body4 ='{"dpid": 6,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        #initial_s6_body3 ='{"dpid": 6,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":36763},"actions":[{ "type": "OUTPUT","port": 1}]}' #Line 3/s6
        #initial_s6_body4 ='{"dpid": 6,"cookie": 4,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":37855},"actions":[{ "type": "OUTPUT","port": 2}]}' #Line 4/s6

        initial_s13_body1 ='{"dpid": 13,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s13_body2 ='{"dpid": 13,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s13_body3 ='{"dpid": 13,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s13_body4 ='{"dpid": 13,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'
        #initial_s9_body3 ='{"dpid": 9,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42317},"actions":[{ "type": "OUTPUT","port": 4}]}' #Line 1/s9
        #initial_s9_body4 ='{"dpid": 9,"cookie": 4,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42302},"actions":[{ "type": "OUTPUT","port": 4}]}' #Line 2/s9

        initial_s14_body1 ='{"dpid": 14,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s14_body2 ='{"dpid": 14,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s14_body3 ='{"dpid": 14,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s14_body4 ='{"dpid": 14,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'
        #initial_s10_body3 ='{"dpid": 10,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":36763},"actions":[{ "type": "OUTPUT","port": 3}]}' #Line 3/s10
        #initial_s10_body4 ='{"dpid": 10,"cookie": 4,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":37855},"actions":[{ "type": "OUTPUT","port": 3}]}' #Line 4/s10

        initial_s17_body1 ='{"dpid": 17,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s17_body2 ='{"dpid": 17,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s17_body3 ='{"dpid": 17,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s17_body4 ='{"dpid": 17,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'

        initial_s18_body1 ='{"dpid": 18,"cookie": 1,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s18_body2 ='{"dpid": 18,"cookie": 2,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s18_body3 ='{"dpid": 18,"cookie": 3,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s18_body4 ='{"dpid": 18,"cookie": 4,"table_id": 0,"priority":3,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'



	#switch of type 3
        initial_s1_body1 ='{"dpid": 1,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s1_body2 ='{"dpid": 1,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s1_body3 ='{"dpid": 1,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s1_body4 ='{"dpid": 1,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'
        #initial_s1_body3 ='{"dpid": 1,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42317},"actions":[{ "type": "OUTPUT","port": 2}]}' #Line 1/s1

        initial_s2_body1 ='{"dpid": 2,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 2}]}'
        initial_s2_body2 ='{"dpid": 2,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s2_body3 ='{"dpid": 2,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s2_body4 ='{"dpid": 2,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 3}]}'
        #initial_s2_body3 ='{"dpid": 2,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":42302},"actions":[{ "type": "OUTPUT","port": 4}]}' #Line 2/s2

        initial_s3_body1 ='{"dpid": 3,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s3_body2 ='{"dpid": 3,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 2}]}'
        initial_s3_body3 ='{"dpid": 3,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s3_body4 ='{"dpid": 3,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 1}]}'
        #initial_s3_body3 ='{"dpid": 3,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":36763},"actions":[{ "type": "OUTPUT","port": 1}]}' #Line 3/s3

        initial_s4_body1 ='{"dpid": 4,"cookie": 1,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 1},"actions":[{ "type": "OUTPUT","port": 3}]}'
        initial_s4_body2 ='{"dpid": 4,"cookie": 2,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 3},"actions":[{ "type": "OUTPUT","port": 1}]}'
        initial_s4_body3 ='{"dpid": 4,"cookie": 3,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 2},"actions":[{ "type": "OUTPUT","port": 4}]}'
        initial_s4_body4 ='{"dpid": 4,"cookie": 4,"table_id": 0,"priority":2,"flags": 1,"match":{"in_port": 4},"actions":[{ "type": "OUTPUT","port": 2}]}'
        #initial_s4_body3 ='{"dpid": 4,"cookie": 3,"table_id": 0,"priority":100,"flags": 1,"match":{"dl_type":2048,"nw_src":"10.0.0.1","nw_dst":"10.0.0.3","nw_proto":17,"udp_dst":5001,"udp_src":37855},"actions":[{ "type": "OUTPUT","port": 2}]}' #Line 4/s4



	#send request 
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s7_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s7_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s7_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s7_body4, method='POST',headers=headers)
        #response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s7_body5, method='POST',headers=headers)
        #response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s7_body6, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s8_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s8_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s8_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s8_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s11_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s11_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s11_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s11_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s12_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s12_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s12_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s12_body4, method='POST',headers=headers)
        #response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s11_body5, method='POST',headers=headers)
        #response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s11_body6, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s16_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s16_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s16_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s16_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s19_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s19_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s19_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s19_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s20_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s20_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s20_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s20_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s15_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s15_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s15_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s15_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s5_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s5_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s5_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s5_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s6_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s6_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s6_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s6_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s9_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s9_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s9_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s9_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s10_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s10_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s10_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s10_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s14_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s14_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s14_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s14_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s17_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s17_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s17_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s17_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s18_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s18_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s18_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s18_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s13_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s13_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s13_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s13_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s1_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s1_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s1_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s1_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s2_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s2_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s2_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s2_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s3_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s3_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s3_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s3_body4, method='POST',headers=headers)

        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s4_body1, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s4_body2, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s4_body3, method='POST',headers=headers)
        response, content = http.request(uri='http://192.168.93.137:8080/stats/flowentry/add', body=initial_s4_body4, method='POST',headers=headers)




ryu = RyuUtil('192.168.93.137', '8080')
ryu.install_flow()
