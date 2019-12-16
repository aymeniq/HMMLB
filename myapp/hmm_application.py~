import linecache
import random

"""
bandwidth 1 means the load rate =<20%
bandwidth 2 means the load rate 20%<load rate<50%
bandwidth 3 means the load rate >=50%
direction 1 means forward
direction 2 means backward
flowsize  1 means the flowsize =<500Mbits
flowsize  2 means the flowsize 500Mbits<flowsize<1Gbits
flowsize  3 means the flowsize >=1Gbits

observed_matrix's column is defined as 0~53(S7_port1 S4_port2 direction flowsize) 54~71(S5_port2 direction flowsize) 72~89(S6_port2 direction flowsize)

"""


#this is the Hmm Application
class HmmApplication():
	def __init__(self):
	    self.bandwidth_read  = [0 for i in range(4)]
	    self.direction_read  = 1
	    self.flowsize_read   = 1
	
	    self.bandwidth  	 = [0 for i in range(4)]
	    self.direction	 = 1
	    self.flowsize        = 1	

	    self.observed_matrix = []  					       #self.observed_matrix = [[0 for i in range(90)] for i in range(6)]
	    self.transfer_matrix = []                                          #self.transfer_matrix = [[0 for i in range(6)] for i in range(6)]
	    self.initial_vector  = 0		       			       #self.initial_vector  = [0 for i in range(6)]
	    self.default_path_number = 0

	def get_parameter(self,S7_port1,S4_port2,S5_port2,S6_port2,direction,flowsize):
	    self.bandwidth_read[0]    = str(S7_port1)	#S7_port1
	    self.bandwidth_read[1]    = str(S4_port2)	#S4_port2
	    self.bandwidth_read[2]    = str(S5_port2)	#S5_port2
	    self.bandwidth_read[3]    = str(S6_port2)	#S6_port2
	    self.direction_read       = str(direction)
	    self.flowsize_read        = str(flowsize)

	    self.bandwidth[0]	      = int(self.bandwidth_read[0])
	    self.bandwidth[1]	      = int(self.bandwidth_read[1])
	    self.bandwidth[2]	      = int(self.bandwidth_read[2])
	    self.bandwidth[3]	      = int(self.bandwidth_read[3])
	    self.direction 	      = int(self.direction_read)
	    self.flowsize 	      = int(self.flowsize_read)

	    with open('/home/ryu/myapp/observed_matrix.txt','r') as f:
	       for line in f:
		  self.observed_matrix.append(list(map(float,line.split(','))))
	   
	    with open('/home/ryu/myapp/transfer_matrix.txt','r') as f:
	       for line in f:
		  self.transfer_matrix.append(list(map(float,line.split(','))))

	    with open('/home/ryu/myapp/initial_vector.txt','r') as f:
	       for line in f:
		  self.initial_vector = (list(map(float,line.split(','))))


	def caculation(self):
	    #This is the first hiden_state caculation, we need find the position of the observed state in *observed_matrix, the formula "row_number_firststate = (w-1)*18+(x-1)*6+(y-1)*3+(z-1)" is being 		     used. 
	    #w means the value of S7_port1, x means the value of S4_port2, y means the value of direction, z means the value of flowsize.
	    default_path_number = 0
	    row_number_firststate = (self.bandwidth[0]-1)*18+(self.bandwidth[1]-1)*6+(self.direction-1)*3+(self.flowsize-1)

	    S5_probability = self.initial_vector[4]*self.observed_matrix[4][row_number_firststate]      #the first hiden_state probability of Switch 5
	    S6_probability = self.initial_vector[5]*self.observed_matrix[5][row_number_firststate]	#the first hiden_state probability of Switch 6
	    

	    #This is the second hiden_state caculation, the same we need finde the observed state's position, the formulas "row_number_second_S1S2 = 54+(x-1)*6+(y-1)*3+(z-1)" and "row_number_second_S3S4 		     = 72+(x-1)*6+(y-1)*3+(z-1)"are being used.
	    #x means the value of S5_port2 or S6_port2, y means the value of direction, z means the value of flowsize.

	    row_number_secondstate_S1S2 = 54+(self.bandwidth[2]-1)*6+(self.direction-1)*3+(self.flowsize-1)		# the DATA of S5_port2 is being used cause the network topology
	    row_number_secondstate_S3S4 = 72+(self.bandwidth[3]-1)*6+(self.direction-1)*3+(self.flowsize-1)		# the DATA of S6_port2 is being used

	    S1_probability = max(S5_probability*self.transfer_matrix[4][0],S6_probability*self.transfer_matrix[5][0])*self.observed_matrix[0][row_number_secondstate_S1S2]
	    S2_probability = max(S5_probability*self.transfer_matrix[4][1],S6_probability*self.transfer_matrix[5][1])*self.observed_matrix[1][row_number_secondstate_S1S2]
	    S3_probability = max(S5_probability*self.transfer_matrix[4][2],S6_probability*self.transfer_matrix[5][2])*self.observed_matrix[2][row_number_secondstate_S3S4]
	    S4_probability = max(S5_probability*self.transfer_matrix[4][3],S6_probability*self.transfer_matrix[5][3])*self.observed_matrix[3][row_number_secondstate_S3S4]
	    """
	    #according to the probability, we caculate the routing pace of this flow.this is for the certain pace.
	    result = max(S1_probability,S2_probability,S3_probability,S4_probability)
	    if(result == S1_probability):
		print("the first line")
	    if(result == S2_probability):
		print("the second line")
	    if(result == S3_probability):
		print("the third line")
	    if(result == S2_probability):
		print("the forth line")
	    """
	    #this is for the probably pace
	    print(S1_probability,S2_probability,S3_probability,S4_probability)
	    if(S1_probability + S2_probability + S3_probability + S4_probability == 0):

		self.default_path_number = self.default_path_number + 1

		default_path = 'S4'
	     	return default_path #default_path is S4
	    print('the default_path_number is:'+str(self.default_path_number))
	    
	    s1=S1_probability / (S1_probability + S2_probability + S3_probability + S4_probability)   #Calculate the percentage of s1 s2 s3 s4
	    s2=S2_probability / (S1_probability + S2_probability + S3_probability + S4_probability)
	    s3=S3_probability / (S1_probability + S2_probability + S3_probability + S4_probability)
	    s4=S4_probability / (S1_probability + S2_probability + S3_probability + S4_probability)
	    print(s1,s2,s3,s4)

	    some_list = ['S1','S2','S3','S4'] 
	    probabilities = [s1,s2,s3,s4]

	    x = random.uniform(0,1)  
	    cumulative_probability = 0.0
	    for item, item_probability in zip(some_list, probabilities):  
		cumulative_probability += item_probability  
		if x < cumulative_probability:break  
	    return item


		
		
		
#hmm = HmmApplication()
#hmm.get_parameter()
#hmm.caculation()	    

	    
	    
		
