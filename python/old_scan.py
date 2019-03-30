import pyinsane2
import datetime

now = datetime.datetime.now()

pyinsane2.init()
try:
	devices = pyinsane2.get_devices()
	assert(len(devices) > 0)
	device = devices[0]
	print("I'm going to use the following scanner: %s" % (str(device)))

	try:
		pyinsane2.set_scanner_opt(device, 'resolution', [1200])
		# [100, 150, 200, 300, 400, 600, 1200, 2400, 4800, 9600]
		# 清晰度太高可能会memory error
		pyinsane2.set_scanner_opt(device, 'source', ['ADF', 'Feeder'])  #Comment this line will not use feeder
	except PyinsaneException:
		print("No document feeder found")
		# return

# Beware: Some scanners have "Lineart" or "Gray" as default mode
# better set the mode everytime
	# device.options["SANE_TYPE_FIXED"]=1
	pyinsane2.set_scanner_opt(device, 'mode', ['Color'])

# Beware: by default, some scanners only scan part of the area
# they could scan.
	pyinsane2.maximize_scan_area(device)
	print("Start!")
	scan_session = device.scan(multiple=True)
	try:
		while True:
			try:
				scan_session.scan.read()
			except EOFError:
				print ("Got a page ! (current number of pages read: %d)"
					% (len(scan_session.images)))
	except StopIteration:
		print("Document feeder is now empty. Got %d pages"
			% len(scan_session.images))
	for idx in range(0, len(scan_session.images)):
		image = scan_session.images[idx]
		image.save("output/"+str(now.date())+str(idx)+".png")
finally:
	pyinsane2.exit()

