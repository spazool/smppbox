#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smpputil import *

########################################
# Заголовок пакета
########################################
class __sb_pdu_header__:
    def __init__(self,command_id,command_status,sequence_number=0):
	self.command_id = command_id
	self.command_id_text = ""
	self.command_status_id = command_status
	self.command_status = ""
	self.command_status_text = ""
	self.sequence_number = sequence_number
	self.length = 0

    def __len__(self):
	if ("__body__" in dir(self)):
	    return len(toDWORD(self.command_id)+toDWORD(self.command_status_id)+toDWORD(self.sequence_number))+len(self.__body__())+4
	else:
	    return self.length
 
    def __head__(self):
	return toDWORD(len(self))+toDWORD(self.command_id)+toDWORD(self.command_status_id)+toDWORD(self.sequence_number)

    # Построение заголовков
    def __reverce__(self,pck):
	length = fromDWORD(pck[0:4])
	command_id=fromDWORD(pck[4:8])
	command_status=fromDWORD(pck[8:12])
	sequence_number=fromDWORD(pck[12:16])
	header = __sb_pdu_header__(command_id,command_status,sequence_number)
	header.length = length
	return header

    def __str__(self):
	for c in smpp_command_id:
	    if (smpp_command_id[c]==self.command_id):
		self.command_id_text = c

	for c in smpp_statuses:
	    if (smpp_statuses[c]==self.command_status_id):
		self.command_status = c
		self.command_status_text = smpp_statuses_text[c]

	res = "HEADER:\n"
	res+= "\tLenght:%s (%s)\n" % (len(self),hEX(len(self)))
	res +="\tCommand_id:%s (%s)\n" % (self.command_id_text, hEX(self.command_id))
	res+= "\tCommand status:%s (%s) %s\n" % (str(self.command_status),hEX(self.command_status_id),self.command_status_text)
	res+= "\tSequence number:"+str(self.sequence_number)+"\n"
	res+= "\thex:%s\n" % toHexString(self.__head__())
	return res

class __sb_bind__(__sb_pdu_header__):
    def __init__(self,system_id,password,system_type="cpa",interface_version=0x00000034,addr_ton=0x00,addr_npi=0x00,addr_range="",command_id=smpp_command_id["bind_transceiver"],command_status_id=smpp_statuses["ESME_ROK"],sequence_number=0):
	self.system_id=system_id
	self.password= password
	self.system_type=system_type
	self.interface_version = interface_version
	self.addr_ton = addr_ton
	self.addr_npi = addr_npi
	self.addr_range = addr_range
	__sb_pdu_header__.__init__(self,command_id,command_status_id,sequence_number)
	
    def __body__(self):
	res = to_c_octetstring(self.system_id,16)
	res+= to_c_octetstring(self.password,9)
        res+= to_c_octetstring(self.system_type,13)
	res+= chr(self.interface_version)
        res+= chr(self.addr_ton)
	res+= chr(self.addr_npi)
        res+= to_c_octetstring(self.addr_range+"\x00",41)
	return res

    def __str__(self):
	res = str(__sb_pdu_header__.__str__(self))
	res +="BODY:\n"
	res +="\tsystem_id:%s\n" % self.system_id
	res +="\tpassword:%s\n" % self.password
	res +="\tsystem_type:%s\n" % self.system_type
	res +="\tinterface_version:%s\n" % hEX(self.interface_version)
	res +="\taddr_ton:%d, addr_npi:%d\n" % (self.addr_ton,self.addr_npi)
	res +="\taddr_range: %s\n" % str(self.addr_range)
	res +="\thex:%s" % toHexString(self.__body__()) 
	return res

    def pck(self):
	return __head__()+__body__()

    @classmethod
    def __reverce__(self,pck):
	raise Exception("this packet not reversed.")
	pass


class __sp_bind_resp__(__sb_pdu_header__):
    def __init__(self,system_id,sc_interface_version=""):
	
	self.system_id = system_id
	self.sc_interface_version = sc_interface_version
	__sb_pdu_header__.__init__(self,smpp_command_id["bind_transceiver_resp"],smpp_statuses["ESME_ROK"],0)
	
    def __body__(self):
	res = to_c_octetstring(self.system_id,16)
	res += self.sc_interface_version
	return res

    @classmethod
    def __reverce__(self,pck,pdu_header=None):
	if (pdu_header==None):
	    pdu_header = __sb_pdu_header__.__reverce__(pck)
	pck = pck[16:]
	system_id = get_c_octet_string(pck,16)
	resp = __sp_bind_resp__(system_id,pck[len(system_id)+1:])    
	resp.__sb_pdu_header__ = pdu_header
	return resp

    def __str__(self):
	res = str(__sb_pdu_header__.__str__(self))
	res += "BODY:\n"
	res +="\tsystem_id:%s\n" % self.system_id
	res +="\tsc_interface_version:%s\n" % toHexString(self.sc_interface_version)
	res +="\thex:%s" % toHexString(self.__body__()) 
	return res
 
    def pck(self):
	return __head__()+__body__()
