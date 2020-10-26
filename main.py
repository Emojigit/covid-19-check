from modules import emojiapp_config as ec
from modules import license as el
import os, csv, datetime, sys
import prettytable as pt
if len(sys.argv) == 1:
	op = ""
else:
	op = sys.argv[1]
if op == "license":
	print(el.get())
	exit()

app_name = "covid-19-check"
rdir = ec.get_root(app_name)
os.chdir(rdir)
if not os.path.isdir(rdir+"/COVID-19"):
	status = os.system("git clone https://github.com/CSSEGISandData/COVID-19 --depth 1")
	if not status == 0:
		print("[Error] Can't clone the COVID-19 REPO")
		exit(status)
	os.chdir(rdir+"/COVID-19")
else:
	os.chdir(rdir+"/COVID-19")
	status = os.system("git pull")
	if not status == 0:
		print("[Error] Can't pull the COVID-19 REPO")
		exit(status)
if op == "clone_only":
	exit()
repo = rdir+"/COVID-19"
date = datetime.date.today() + datetime.timedelta(days=-1)
dstr = date.strftime('%m-%d-%Y')
csvdir = repo+"/csse_covid_19_data/csse_covid_19_daily_reports/"+dstr+".csv"
tc,td,tr,ta = 0,0,0,0
with open(csvdir, newline='') as csvfile:
	rows = csv.reader(csvfile)
	tb1 = pt.PrettyTable()

	c = 0
	for row in rows:
		if c == 0:
			tb1.field_names = row
			c = 1
		else:
			if not op == "no_limit":
				row[1] = (row[1][:10] + '..') if len(row[1]) > 10 else row[1]
				row[2] = (row[2][:15] + '..') if len(row[2]) > 15 else row[2]
				row[3] = (row[3][:15] + '..') if len(row[3]) > 15 else row[3]
				row[11] = (row[11][:12] + '..') if len(row[11]) > 12 else row[11]
			tb1.add_row(row)
			tc = tc + int(row[7])
			td = td + int(row[8])
			tr = tr + int(row[9])
			ta = ta + int(row[9])
	tb1.align = "l"
	print(tb1)
print("Total Confirmed: "+str(tc))
print("Total Death: "+str(td))
print("Total Recovered: "+str(tr))
print("Total Active: "+str(ta))
