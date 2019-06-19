# reed-switch-rpi

There are a few things you can do with the combo of an rpi + adafruit power boost board + reed switch + magnet. 

One thing is that when a magnet is placed against the reed switch, the raspberry pi remains off. When the magnet is moved away from the reed switch, the raspberry pi turns on. This can be facilitated by connecting the reed swith to the enable and ground pins on the power boost board and connecting power and ground from the power boost board to the rpi. When the magnet is applied it flicks the switch inside the reed switch to closed and it shorts enable and ground together which restricts power to the rpi. When the magnet is removed the reed switch flicks open and the short is not present which allows power to the rpi. This method does not require any code.   

A potential second use of the system is that a script is set to run at rpi boot (following the removal of the magnet's presence at the reed switch). Once the script has run, a countdown will begin: e.g. 10 seconds (specified as delay). Script is terminated if magnet is returned to reed switch.
