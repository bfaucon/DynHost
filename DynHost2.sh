#/bin/sh
 
#
# CONFIG GOES HERE
#
 
HOST=myhost.mydomain.net
LOGIN=mylogin
PASSWORD=mypassword
 
PATH_APP=/home/kemkem/work/dyndns/DynHost
PATH_LOG=$PATH_APP/log
PATH_IPCHECK=$PATH_APP/ipcheck.py
 
#
# CONFIG END
#
 
#prevent error when ipcheck.err exists
rm -f $PATH_APP/ipcheck.err
 
IP=`lynx -dump http://monip.org | grep 'IP' | sed 's/.*: //;'`
 
echo >> $PATH_LOG
echo "Run dynhost" >> $PATH_LOG
date >> $PATH_LOG
 
echo "Current IP" >> $PATH_LOG
echo "$IP" >> $PATH_LOG
 
if [ -z "$IP" ]; then
        echo "No IP retrieved" >> $PATH_LOG
else
        echo "Update IP" >> $PATH_LOG
        RESULT=`$PATH_IPCHECK -a $IP $LOGIN $PASSWORD $HOST`
        echo "Result : $RESULT" >> $PATH_LOG
        if [ -z $RESULT ]; then
                echo "Success" >> $PATH_LOG
        else
                echo "Error : $RESULT" >> $PATH_LOG
        fi
fi
