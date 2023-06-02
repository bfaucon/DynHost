#!/usr/bin/python
# -*- coding: utf-8 -*-
#=========================================================================
#              Test_Email.py
#-------------------------------------------------------------------------
# by Bruno Faucon - 2023
# version 0.1 2023-04-11
# test console + Email for alerting
# version 0.2 2023-05-30  
# mise à jour: Suppression du message si pas de paramètre pour éviter écriture dans le log.
#-------------------------------------------------------------------------
# tested with python 2.7 on Raspberry pi (wheezy) and MariaDB 5.5.34 on NAS Synology DS411J (DSM 5)
# 
#-------------------------------------------------------------------------
#
#===================================================================
 
#----------------------------------------------------------#
#             package importation                          #
#----------------------------------------------------------#
import sys
import smtplib
#from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText 

#-----------------------------------------------------------------#
#  constants : use your own values / utilisez vos propres valeurs #
#-----------------------------------------------------------------#
EMAIL_SMTP='smtp.famillefaucon.be'
EMAIL_PORT=587
EMAIL_LOGIN='brfa@famillefaucon.be'
EMAIL_PWD='lufa45mail'
EMAIL_FROM='rpi@one2care.be'
EMAIL_TO='bruno.faucon@one2care.be'

#----------------------------------------------------------#
#             Variables                                    #
#----------------------------------------------------------#

#----------------------------------------------------------#
#     Send Email                                           #
#----------------------------------------------------------#
def send_mail(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_TEXT):
   #print "send mail"
   msg = MIMEMultipart()
   msg['From'] = 'rpi@one2care.be'
   msg['To'] = EMAIL_TO
   msg['Subject'] = EMAIL_SUBJECT
   message = EMAIL_TEXT
   msg.attach(MIMEText(message))
   mailserver = smtplib.SMTP(EMAIL_SMTP, EMAIL_PORT)
   mailserver.ehlo()
   mailserver.starttls()
   mailserver.ehlo()
   mailserver.login(EMAIL_LOGIN, EMAIL_PWD)
   mailserver.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
   mailserver.quit()


#----------------------------------------------------------#
#     Primary code                                         #
#----------------------------------------------------------#

#print "Alerte consommation d'eau"
try:
	EMAIL_FROM = sys.argv[1]
	EMAIL_TO = sys.argv[2]
	EMAIL_SUBJECT = sys.argv[3]
	EMAIL_TEXT =  sys.argv[4]
	a = send_mail(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_TEXT)
except:
	a = 0
        #print ("Script d'envoi d'Email Paramètres: Mail From, Mail To, Subject, Message")

