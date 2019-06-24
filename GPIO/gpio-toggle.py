#!/usr/bin/python

# Toggle GPIO pin 23.
# Output pulse frequency is about 18 kHz (varies due to other activity).

import sys
cmdargs = str(sys.argv)
total = len(sys.argv)

print ("Total: %s" % total)

if total == 1:
    print("Usage: %s <pin number> <pin status>" % sys.argv[0])
    sys.exit(2)


pin = str(sys.argv[1])
status = str(sys.argv[2])

pin_path = '/sys/class/gpio/gpio' + pin

print("Turning pin %s %s" % (pin,status))

def write_once(path, value):
    f = open(path, 'w')
    f.write(value)
    f.close()
    return


# Set pin for output, with initial value low. 
write_once(pin_path + '/direction', 'out\n')

f = open(pin_path + '/value', 'w')

if status == 'on':
	f.write('1')
	f.flush()
elif status == 'off':
	f.write('0')
	f.flush()
else:
	print("Incorrect status, please use either on or off")
	sys.exit(2)

f.close()
