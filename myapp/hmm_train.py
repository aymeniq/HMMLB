import linecache

"""
the train_data.txt structure is :
	  hiden_state	|         observed_state     
		   	|
	   route_path 	|   S7-port1   S4-port2   S5-port2   S6-port2   direction   flowsize
example:	1	|     2           2          3          1           1           3
		   	|
		   	|

"""	



def train_function():
	myfile = open("train_data.txt") 
	lines = len(myfile.readlines())		       #caculate the lines of data.

	data_read = [[0 for i in range(7)] for i in range(lines)]
	data_int  = [[0 for i in range(7)] for i in range(lines)]

	i = 0
	while(i<lines):
		data_read[i] = linecache.getline('train_data.txt',i+1)      #read the data to an array

		j = 0
		while(j<7):						    #change the "string" to "int"
			data_int[i][j] = int(data_read[i][j])
			j += 1


		i += 1

	
	"""
	summarize the data
	"""

	 
	route_path_summary      = [0 for i in range(7)]	           #summarize route_path, total number is 4

	observed_matrix_data_S5 = [0 for i in range(54)]           #summarize the observed_matrix of S5, total number is 54
	observed_matrix_data_S6 = [0 for i in range(54)]           #summarize the observed_matrix of S6, total number is 54
	observed_matrix_data_S1 = [0 for i in range(18)]	   #summarize the observed_matrix of S1, total number is 18
	observed_matrix_data_S2 = [0 for i in range(18)]	   #summarize the observed_matrix of S2, total number is 18
	observed_matrix_data_S3 = [0 for i in range(18)]  	   #summarize the observed_matrix of S3, total number is 18
	observed_matrix_data_S4 = [0 for i in range(18)]  	   #summarize the observed_matrix of S4, total number is 18

	transfer_matrix_data_S5 = [0 for i in range(2)]            #total number is 2
	transfer_matrix_data_S6 = [0 for i in range(2)]		   #total number is 2

	initial_matrix_data 	= [0 for i in range(2)]		   #means the initial_probability	

	total_S5 = 0				                   #remember the number of states
	total_S6 = 0
	total_S1 = 0
  	total_S2 = 0
	total_S3 = 0
	total_S4 = 0

	i = 0 
	while(i < lines):
		
		if(data_int[i][0] == 1):
			
			route_path_summary[0] += 1

			column_S5 = (data_int[i][1]-1)*18+(data_int[i][2]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)			#"column_S5 = (w-1)*18+(x-1)*6+(y-1)*3+(z-1)" is being used. 
			observed_matrix_data_S5[column_S5] += 1										#summarize the observed_matrix of S5
			total_S5 += 1
			

			column_S1 = (data_int[i][3]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)					#the formulas "column_S1 = (x-1)*6+(y-1)*3+(z-1)" is being used.
			observed_matrix_data_S1[column_S1] += 1										#summarize the observed_matrix of S1
			total_S1 += 1

		if(data_int[i][0] == 2):

			route_path_summary[1] += 1

			column_S5 = (data_int[i][1]-1)*18+(data_int[i][2]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)			
			observed_matrix_data_S5[column_S5] += 1	
			total_S5 += 1

			column_S2 = (data_int[i][3]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)
			observed_matrix_data_S2[column_S2] += 1										#summarize the observed_matrix of S2
			total_S2 += 1

		if(data_int[i][0] == 3):

			route_path_summary[2] += 1

			column_S6 = (data_int[i][1]-1)*18+(data_int[i][2]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)			
			observed_matrix_data_S6[column_S6] += 1										#summarize the observed_matrix of S6
			total_S6 += 1
		
			column_S3 = (data_int[i][4]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)
			observed_matrix_data_S3[column_S3] += 1										#summarize the observed_matrix of S3
			total_S3 += 1

		if(data_int[i][0] == 4):

			route_path_summary[3] += 1

			column_S6 = (data_int[i][1]-1)*18+(data_int[i][2]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)			#summarize the observed_matrix of S6
			observed_matrix_data_S6[column_S6] += 1		
			total_S6 += 1
				
			column_S4 = (data_int[i][4]-1)*6+(data_int[i][5]-1)*3+(data_int[i][6]-1)
			observed_matrix_data_S4[column_S4] += 1										#summarize the observed_matrix of S4
			total_S4 += 1

		i += 1
		
	

	"""

	caculate the observed_probability of switch

	"""
	i = 0
	while(i<54):
		

		observed_matrix_data_S5[i] = observed_matrix_data_S5[i]/float(total_S5)
		observed_matrix_data_S6[i] = observed_matrix_data_S6[i]/float(total_S6)
		i += 1

	i = 0
	while(i<18):
	
		observed_matrix_data_S1[i] = observed_matrix_data_S1[i]/float(total_S1)
		observed_matrix_data_S2[i] = observed_matrix_data_S2[i]/float(total_S2)
		observed_matrix_data_S3[i] = observed_matrix_data_S3[i]/float(total_S3)
		observed_matrix_data_S4[i] = observed_matrix_data_S4[i]/float(total_S4)	
		i+= 1

	"""
	
	caculate the transfer_probability of switch

	"""
	transfer_matrix_data_S5[0] = total_S1/float((total_S1+total_S2)) 							#means the probability of S5->S1
	transfer_matrix_data_S5[1] = total_S2/float((total_S1+total_S2))							#means the probability of S5->S2
	transfer_matrix_data_S6[0] = total_S3/float((total_S3+total_S4)) 							#means the probability of S6->S3
	transfer_matrix_data_S6[1] = total_S4/float((total_S3+total_S4))							#means the probability of S6->S4


	"""
	
	caculate the initial_probability of switch

	"""
	initial_matrix_data[0] = total_S5/float((total_S5+total_S6))								#the initial probability of S5
	initial_matrix_data[1] = total_S6/float((total_S5+total_S6))								#the initial probability of S6


	"""
	merge the observed_data and put it out to observed_matrix.txt

	"""

	observed_matrix_data = [[0 for i in range(90)] for i in range(6)]							

	i=0
	while(i<54):
		observed_matrix_data[4][i] = observed_matrix_data_S5[i] 
		observed_matrix_data[5][i] = observed_matrix_data_S6[i] 	
		i += 1

	j = 0
	while(i<72):
		observed_matrix_data[0][i] = observed_matrix_data_S1[j]
		observed_matrix_data[1][i] = observed_matrix_data_S2[j]
		i += 1
		j += 1


	j = 0
	while(i<90):
		observed_matrix_data[2][i] = observed_matrix_data_S3[j]
		observed_matrix_data[3][i] = observed_matrix_data_S4[j]
		i += 1
		j += 1
	
	
	
	file = open('observed_matrix.txt','w') 
	for k in observed_matrix_data:
		k = str(k).strip('[').strip(']').replace("'","").replace('','')
		file.write(k+'\n')
	file.close()


	"""

	merge the transfer_data and put it out to transfer_matrix.txt
	
	"""
	transfer_matrix_data = [[0 for i in range(6)] for i in range(6)]

	transfer_matrix_data[4][0] = transfer_matrix_data_S5[0]
	transfer_matrix_data[4][1] = transfer_matrix_data_S5[1]	
	transfer_matrix_data[5][2] = transfer_matrix_data_S6[0]
	transfer_matrix_data[5][3] = transfer_matrix_data_S6[1]
	
	file = open('transfer_matrix.txt','w') 
	for k in transfer_matrix_data:
		k = str(k).strip('[').strip(']').replace("'","").replace('','')
		file.write(k+'\n')
	file.close()


	"""
	
	put initial_matrix_data out to the initial_vector.txt

	"""
	initial_vector = [0 for i in range(6)]

	initial_vector[4] = initial_matrix_data[0]
	initial_vector[5] = initial_matrix_data[1]

	file = open('initial_vector.txt','w') 
	i = 0
	for k in initial_vector:
		k = str(k)
		if(i < 5):
			file.write(k+',')
		if(i == 5):
			file.write(k+'\n')
		i += 1
	file.close()





	
"""
Do the train_function
"""
train_function()









	
