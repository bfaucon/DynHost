#!/bin/bash

#=========================================================================
#              CheckWan.py
#-------------------------------------------------------------------------
# by Bfaucon - 2022, April
# version 0.1 2022-04-20
# Modifications by Bruno Faucon - 2022
# version 0.2 2022-04-20
# Documentation
#-------------------------------------------------------------------------
# Checking internet connection.
# If issue, restart wlan0
#=========================================================================

# keep LAN alive
echo "................................................"
date "+%Y.%m.%d %H:%M:%S"
echo " "
ping -c2 google.com 

 
if [ $? != 0 ] 
then 
  echo " "
  echo "No network connection, restarting wlan0"
  
# put your router reboot code here
   echo "Stop Wlan0"
   #sudo ifdown wlan0
   sudo ip link set wlan0 down
   echo "Start Wlan0"
   #sudo ifup wlan0
   sudo ip link set wlan0 up
   echo "Wait 30 Sec"
   sleep 30s
   echo "send Email"
   python ./Send_Email.py rpi@one2care.be bruno.faucon@one2care.be 'Alerte Raspberry' 'Problème de connexion internet sur le nouveau Raspberry. Je redémarre wlan0'
fi
echo "................................................"
echo " "
