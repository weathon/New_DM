import pyinsane2
import datetime
import pickle
import os
import eel

def get_devices_function():
	pyinsane2.init()
	devices = pyinsane2.get_devices()
	assert(len(devices) > 0)
	return devices
	
def feeder(resolution,mode):
	with open("usedid.txt",'r') as myfile:
		myid=myfile.read()
	with open("usedid.txt",'w') as myfile:
		myfile.write(str(int(myid)+1))
	now = datetime.datetime.now()

	pyinsane2.init()
	try:
		devices = pyinsane2.get_devices()
		assert(len(devices) > 0)
		device = devices[0]
		eel.PageConsole("I'm going to use the following scanner: %s" % (str(device)))

		try:
			pyinsane2.set_scanner_opt(device, 'resolution', [int(resolution)])
			# [100, 150, 200, 300, 400, 600, 1200, 2400, 4800, 9600]
			# 清晰度太高可能会memory error
			pyinsane2.set_scanner_opt(device, 'source', ['ADF', 'Feeder'])  #Comment this line will not use feeder
		except PyinsaneException:
			eel.PageConsole("No document feeder found")
			# return

	# Beware: Some scanners have "Lineart" or "Gray" as default mode
	# better set the mode everytime
		# device.options["SANE_TYPE_FIXED"]=1
		pyinsane2.set_scanner_opt(device, 'mode', [mode])

	# Beware: by default, some scanners only scan part of the area
	# they could scan.
		pyinsane2.maximize_scan_area(device)
		eel.PageConsole("Start!")
		scan_session = device.scan(multiple=True)
		try:
			while True:
				try:
					scan_session.scan.read()
				except EOFError:
					print ("Got a page ! (current number of pages read: %d)"
						% (len(scan_session.images)))
		except StopIteration:
			eel.PageConsole("Document feeder is now empty. Got %d pages"
				% len(scan_session.images))
		for idx in range(0, len(scan_session.images)):
			image = scan_session.images[idx]
			os.mkdir("./html/output/"+str(myid))
			image.save("./html/output/"+str(myid)+"/"+str(now.date())+"-"+str(idx)+".png")
	finally:
		pyinsane2.exit()
		return "./html/output/"+str(myid)+"/"+str(now.date())+"-"+str(idx)+".png",myid

def start(resolution,mode):
	with open("usedid.txt") as myfile:
		myid=myfile.read()
	with open("usedid.txt",'w') as myfile:
		myfile.write(str(int(myid)+1))

	now = datetime.datetime.now()
	pyinsane2.init()
	try:
		devices = pyinsane2.get_devices()
		assert(len(devices) > 0)
		device = devices[0]
		eel.PageConsole("I'm going to use the following scanner: %s" % (str(device)))

		pyinsane2.set_scanner_opt(device, 'resolution', [int(resolution)])

	# Beware: Some scanners have "Lineart" or "Gray" as default mode
	# better set the mode everytime
		pyinsane2.set_scanner_opt(device, 'mode', [mode])

	# Beware: by default, some scanners only scan part of the area
	# they could scan.
		pyinsane2.maximize_scan_area(device)

		scan_session = device.scan(multiple=False)
		try:
			while True:
				scan_session.scan.read()
		except EOFError:
			pass
		image = scan_session.images[-1]
		os.mkdir("./html/output/"+str(myid))
		image.save("./html/output/"+str(myid)+"/"+str(now.date())+str(0)+".png")
	finally:
		pyinsane2.exit()
		return "./html/output/"+str(myid)+"/"+str(now.date())+str(0)+".png",myid
		#以idngyaofangzai finily 

if __name__=="__main__":
    feeder(300,"color")
