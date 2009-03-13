#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading,time
import sb_smpp_sdk.sb_smpp as smpp
from sb_smpp_sdk.smpputil import *

class socket_bind_client(threading.Thread):
    def __init__(self,host,port,bufferSize=2048,recv_event=None):
	self.ci = (host,port)
	self.bufferSize = bufferSize
	self.connected = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recv_event = recv_event
	threading.Thread.__init__(self)
	
    def run(self):
	self.sock.connect( self.ci )
	self.connected = True	
	while self.connected:
	    line=self.sock.recv(self.bufferSize)
	    if (line):
	        self.recv(line)
	    else:
		self.stop()
		break
		
	
    def recv(self,pck):
	#print "<<<<<<<<<<<<<<<<<< "+toHexString(pck)
    	if(self.recv_event!=None):
	    self.recv_event(pck)
	
    def send(self,pck):
	#print ">>>>>>>>>>>>>>>>>> "+toHexString(pck)
	self.sock.send(pck)


    def stop(self):
	if (self.connected):
	    try:
		self.connected = False
		self.sock.shutdown(1)
		self.sock.close()
	    except:
		pass
	    
    
class socket_bind_transceiver(threading.Thread):
    def __init__(self,bind_client,system_id,password,enquire_link_timeout=60):
	self.enquire_link_timeout = enquire_link_timeout # В секундах
	self.bind_client = bind_client
	self.bind_client.recv_event = self.recv;
	self.system_id = system_id
	self.bindpck = smpp.bind_transceiver(self.system_id,password)
	self.current_sequence_number=1
	threading.Thread.__init__(self)
	
    def run(self):
	self.bind_client.start()
	self.send(self.bindpck)
	enq_to = 0
	while self.bind_client.connected:
	    time.sleep(0.1)
	    enq_to+=1
	    if (enq_to>=(self.enquire_link_timeout * 10)):
		enq_to=0
		self.send(smpp.enquire_link())

    def recv(self,pck):
	cl = smpp.class_from_pck(pck,"sb_smpp_sdk.")
	print "\n----  <<<< Recv ---- <<<<<"
	print str(cl)
	if (cl.command_id == smpp_command_id["enquire_link"]):
	    self.send_resp(cl,smpp.enquire_link_resp())

    def send_resp(self,pck_inst,pck_resp):
	pck_resp.sequence_number = pck_inst.sequence_number
	print "----  >>>> Send Response ---- >>>>>"
	print str(pck_inst)
	self.bind_client.send(pck_resp.pck())
	
    def send(self,pck_inst,current_sequence_number=0):
	if (current_sequence_number==0):
	    pck_inst.sequence_number = self.current_sequence_number
	    self.current_sequence_number+=1
	else:
	    pck_inst.sequence_number = current_sequence_number
	print "----  >>>> Send Request---- >>>>>"
	print str(pck_inst)
	self.bind_client.send(pck_inst.pck())

    def stop(self):
	self.bind_client.stop()
	
	