import json
import sys


filepath = "/home/chitra/Python-code/input_file.json"


x = raw_input("Enter serach name:")

def json_read(x):
	with open(filepath,'r') as filejson:
		jsoninputs = json.load(filejson) 
		for i in jsoninputs:
        		if (i == x):
				val = jsoninputs[i]
            			print val
            			break
			else:
				y = raw_input("Enter birthdate:")
				jsoninputs[x]= y
				with open(filepath,'w') as filejson2:
					json.dump(jsoninputs,filejson2)
					jsoninputs = json.dumps(jsoninputs)
					print jsoninputs
					break
 	

json_read(x)
      		





