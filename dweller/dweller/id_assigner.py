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
import re
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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def create_wells(cols, rows):
#	This method is not used in newest iteration
	x = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
	letters = x.split()
	plate = {}
	for row in range(0,rows):
		for col in range(1,cols+1):
			row_letter = letters[row]
			temp_id = well_id + row_letter + str(col)
			plate[temp_id] = {}
	return plate

def read_wells(inp_file, plate):
	with open(inp_file, "r") as inp:
		x = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
		letters = x.split()
		row_index = 0
		for line in inp:
			col_index = 1
			line_cells = line.split('\t')
			for cell in line_cells:
				temp_id = well_id + letters[row_index]+str(col_index)
				if (temp_id not in plate):
					plate[temp_id] = {}
				if ('positive' in cell.lower()):
					plate[temp_id]['control'] = 'positive'
				elif ('negative' in cell.lower()):
					plate[temp_id]['control'] = 'negative'
				elif (is_number(cell)):
					plate[temp_id]['value'] = float(cell)
				col_index += 1
			row_index += 1
	return plate

plate = {}
wells_inp = input("What Plate TSV do you want to load? ")
plate = read_wells(wells_inp, plate)
wells_inp = input("What Assay TSV do you want to load? ")
plate = read_wells(wells_inp, plate)
pprint.pprint (plate)