#from datetime import date
import json

'''
x = raw_input("Enter birthdate:")

def finddob_name(x):
    dict1={"chitra":"18/03/1991","jhon":"20/05/1989","raj":"22/07/2001"}
    for i,j in dict1.items():
        if (j == x):
            print i
            break
        else:
            dict1["newperson"]=x
    print dict1
    
finddob_name(x) 
'''
####################################################################################################


x = raw_input("Enter serach name:")
#x = raw_input("Enter serach name:")

def json_name(x):

	inputs={
		"chitra": "18/03/1991",
		"jhon": "20/05/1989",
		"raj": "22/07/2001"
	          	      
               }	

	old_inputs=json.dumps(inputs)
	jsoninputs = json.loads(old_inputs) 
	#print jsoninputs

	for i in jsoninputs:
        	if (i == x):
			val = jsoninputs[i]
            		print val
            		break
        	else:
            		inputs[x]= "22/07/2019"

    	print inputs


json_name(x)
