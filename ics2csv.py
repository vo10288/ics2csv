import csv
from ics import Calendar
## argparse
import argparse
import os
from datetime import datetime

#Create Necessary Folders
if not os.path.exists("CSV"):
	os.makedirs("CSV")
if not os.path.exists("ICS"):
	os.makedirs("ICS")
	
datatimestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

	
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True, default=
ap.add_argument("-i", "--input", required=True,
	help="input file ICS Google Calendar ")
	
args = vars(ap.parse_args())


# Read ICS Calendar file
with open(str(args["input"]), 'r') as f:
    c = Calendar(f.read())

# Create CSV file
with open('CSV/'+datatimestamp+'.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Subject', 'Start Date', 'End Date'])
    for event in c.events:
        writer.writerow([event.name, event.begin.isoformat(), event.end.isoformat()])
