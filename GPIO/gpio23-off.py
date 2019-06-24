#!/usr/bin/python

# Toggle GPIO pin 23.
# Output pulse frequency is about 18 kHz (varies due to other activity).


pin_path = '/sys/class/gpio/gpio23'

def write_once(path, value):
    f = open(path, 'w')
    f.write(value)
    f.close()
    return


# Set pin for output, with initial value low. 
write_once(pin_path + '/direction', 'out\n')

f = open(pin_path + '/value', 'w')

# Blink as fast as possible...

f.write('0')
f.flush()
    
f.close()
