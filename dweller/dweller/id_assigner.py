'''
Rule for well ID should be customizable				
Target_Libray_Round_Branch_Subbranch_Plate_Well				
				
Target 	TNF			
Library	Lib1			
Round	3			
Branch	A			
Subbranch	1	subbranch should be optional		
Plate	1 to N			
Well	A1 to H12			
				
Plate format should customizable				
'''
import pprint
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("target", help="Target of plate")
parser.add_argument("library", help="Library of plate")
parser.add_argument("round", help="Round number of plate")
parser.add_argument("branch", help="Branch letter of plate")
parser.add_argument("--subbranch", help="Optional subbranch of plate")
args = parser.parse_args() 

#num_plates = input("How many plates are there? ")
plate_size = input("Is your plate size 96 or 384? ")

if args.subbranch:
	well_id = args.target + "_" + args.library + "_" + args.round + "_" + args.branch + "_" + args.subbranch + "_1_"
else:
	well_id = args.target + "_" + args.library + "_" + args.round + "_" + args.branch + "_1_"

def create_wells(cols, rows):
	x = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z AA BB CC DD EE FF'
	letters = x.split()
	plate = {}
	for row in range(1,rows+1):
		for col in range(1,cols+1):
			row_letter = letters[row - 1]
			temp_id = well_id + row_letter + str(col)
			plate[temp_id] = {}
	return plate


plate_size = eval(plate_size)
if plate_size == 96:
	plate = create_wells(12, 8)
elif plate_size == 384:
	plate = create_wells(12, 32)
else:
	print ("Must choose either 96 or 384, defaulting to 96")
	plate = create_wells(96) 

pos_control = input("Which wells are positive controls (Seperate well numbers with commas)? ")
pos_control_wells = pos_control.split(',')
neg_control = input("Which wells are negative controls (Seperate well numbers with commas)? ")
neg_control_wells = neg_control.split(',')
for pos_well in pos_control_wells:
	temp_id = well_id + pos_well.strip().upper()
	if (temp_id in plate.keys()):
		plate[temp_id]['control'] = 'positive'
	else:
		print (pos_well + " does not exist in plate")
for neg_well in neg_control_wells:
	temp_id = well_id + neg_well.strip().upper()
	if (temp_id in plate.keys()):
		plate[temp_id]['control'] = 'negative'
	else:
		print (neg_well + " does not exist in plate")		

pprint.pprint (plate)



#with open(".txt", "wt") as out_file: