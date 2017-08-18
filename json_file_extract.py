import json
#import sys


filepath = "/home/chitra/Python-code/input_file.json"


def json_read():
	x = raw_input("Enter serach name:")
	x=str(x)
	with open(filepath,'r+') as filejson:
		jsonData=filejson.read()
		jsoninputs = json.loads(jsonData)
		print jsoninputs     
		for i,j in jsoninputs.items():
        		if x==i:
				val = j
            			print 'Birthdate is :',val
            			break

		else:
			y = raw_input("Enter birthdate:")
			jsoninputs[x]= y
			with open(filepath,'w+') as filejson:   
				json.dump(jsoninputs,filejson,indent=4)
				print jsoninputs
				

json_read()
      		





