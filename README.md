# reed-switch-rpi

There are a few things you can do with the combo of an rpi + adafruit power boost board + reed switch + magnet. 

1. When a magnet is placed against the reed switch, the raspberry pi remains off. When the magnet is moved away from the reed switch, the raspberry pi turns on. This can be facilitated by connecting the reed swith to the enable and ground pins on the power boost board and connecting power and ground from the power boost board to the rpi. When the magnet is applied it flicks the switch inside the reed switch to closed and it shorts enable and ground together which restricts power to the rpi. When the magnet is removed the reed switch flicks open and the short is not present which allows power flow to the rpi. This method does not require any code!   

2. You run the script (included in the repository as magc.py). You can set this script to run at boot if you like and combine it with the first use specified when the magnet is removed and rpi boots up. If you want it to run at rpi boot, do the following:

        $ chmod +x /magc.py # make executable
        $ sudo nano etc/rc.local 
    
    Just above the “exit 0” line, add a path to magc.py. # place this file wherever you want.
    
    You can also add a delay in there. This may be needed because sometimes the system doesn’t initiate all of the GPIO’s at       once at boot… so your script may be only partially fulfilled. The 10 seconds just gives it a chance to catch up and spin       both at once.
    
    It could look something like this: 
      
        sleep 10
        /home/pi/flipnode.py
        exit 0

Once the script has run, a countdown will begin: e.g. 10 seconds (specified as delay within). Countdown is terminated if magnet is returned to reed switch but script remains active. If countdown is ever achieved, script will activate servos at two specified GPIOs. If this happens, the script will terminate. The script can also be manually terminated.
