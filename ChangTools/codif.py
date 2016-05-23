#!/usr/bin/python
import sys,os
import pickle
import optparse
import pylab as pl
import re
from numpy import array,random,argsort, where
import smtplib
from datetime import datetime


def notif(toaddr='changh20@gmail.com', subject=None, message=None):
    """
    Sends an email notification through GMail .
    """
    username, passwd = _ReadCred()
    fromaddr=username

    # Initialize SMTP server
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,passwd)

    # Send email
    senddate=datetime.strftime(datetime.now(), '%Y-%m-%d -- %I:%M %p')
    if subject is None: 
        subject="Notification"
    m = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "Subject: %s\r\n" % subject + "\r\n" 
    if message is None: 
        msg = 'Notification'
    else: 
        msg = message
    time_stamp = '\tSent at '+senddate

    msg += time_stamp


    server.sendmail(fromaddr, [toaddr], m+msg)
    server.quit()

def _MakeCred(username, password): 
    ''' Make credentials file
    '''
    pickle.dump([username, password], open('dat/login.sav', 'wb'))
    return None

def _ReadCred(): 
    return pickle.load(open('dat/login.sav', 'rb'))
