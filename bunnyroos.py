from __future__ import print_function
import sys
import time

sleeping = '''     
   ^ ^                                                                                                                                                                       
   _ _
 {  *  }                                                                                                                                                                     
{  \ /  }
{       }                                                                                                                                                                     
   " "
'''

awake = ''' 
   ^ ^  !!!                                                                                                                                                                  
   . .
 {  *  }                                                                                                                                                                     
{  \ /  }
{       }
   " "  
'''

string = sys.argv[1]

if "bunnyroo" in string.lower():
    print (sleeping)

if "two" in string.lower():
    print (sleeping)
    print (sleeping)

if "wake up" in string:
    print (sleeping)

if "WAKE UP" in string:
    print (awake)

    seconds_remaining = 3
    while seconds_remaining > 0:
        print (" ")
        time.sleep(3)
        seconds_remaining -= 1
        
    seconds_remaining = 1
    while seconds_remaining > 0:
        print ("so sleepy ...")
        time.sleep(1)
        seconds_remaining -= 1

    seconds_remaining = 3
    while seconds_remaining >0:
        print (" ")
        time.sleep(1)
        seconds_remaining -=1
    print (sleeping)
