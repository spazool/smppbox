#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Проект: Средства разработки приложений использующих протокола SMPP 3.4
#
# sb_pdu.py -зеализует абстрактные классы  для работы протокола. 
# 
# Автор: Дмитрий Высочин
# Дата: 16.03.2008
 
from smpputil import *
import sb_smpp_opt as opt

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
    
    def __copy__(self,header):
	self.command_id = header.command_id
	self.command_status_id = header.command_status_id
	self.sequence_number = header.sequence_number
	self.length = header.length
	
    # Построение заголовков
    @classmethod
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
		break

	for c in smpp_statuses:
	    if (smpp_statuses[c]==self.command_status_id):
		self.command_status = c
		self.command_status_text = smpp_statuses_text[c]
		break

	res = "HEADER:\n"
	res+= "\tLenght:%s (%s)\n" % (len(self),hEX(len(self)))
	res +="\tCommand_id:%s (%s)\n" % (self.command_id_text, hEX(self.command_id))
	res+= "\tCommand status:%s (%s) %s\n" % (str(self.command_status),hEX(self.command_status_id),self.command_status_text)
	res+= "\tSequence number:"+str(self.sequence_number)+"\n"
	res+= "\thex:%s\n" % toHexString(self.__head__())
	return res


# Абстрактный класс установки соединения
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
	return self.__head__()+self.__body__()

    @classmethod
    def __reverce__(self,pck):
	raise Exception("this packet not reversed.")
	pass

# Абстрактный класс ответа установки соединения
class __sb_bind_resp__(__sb_pdu_header__):
    def __init__(self,system_id,sc_interface_version="",command_id=smpp_command_id["bind_transceiver_resp"]):
	
	self.system_id = system_id
	self.sc_interface_version = sc_interface_version
	__sb_pdu_header__.__init__(self,command_id,smpp_statuses["ESME_ROK"],0)
	
    def __body__(self):
	res = to_c_octetstring(self.system_id,16)
	res += self.sc_interface_version
	return res

    @classmethod
    def __reverce__(self,pck,pdu_header=None):
	if (pdu_header==None):
	    pdu_header = __sb_pdu_header__.__reverce__(pck)
	pck = pck[16:]
	system_id = get_c_octetstring(pck,16)
	resp = __sb_bind_resp__(system_id,pck[len(system_id)+1:])    
	#resp.__sb_pdu_header__ = pdu_header
	resp.__copy__(pdu_header)
	#print hEX(pdu_header.command_status_id),hEX(resp.command_status_id)
	return resp

    def __str__(self):
	res = str(__sb_pdu_header__.__str__(self))
	res += "BODY:\n"
	res +="\tsystem_id:%s\n" % self.system_id
	res +="\tsc_interface_version:%s\n" % toHexString(self.sc_interface_version)
	res +="\thex:%s" % toHexString(self.__body__()) 
	return res
 
    def pck(self):
	return self.__head__()+self.__body__()


# Базовый пакет для всех пакетов без тела или не распознанных
class __sb_custom__(__sb_pdu_header__):
    def __init__(self,command_id=smpp_command_id["unbind"],body=""):
	self.body=body
	__sb_pdu_header__.__init__(self,command_id,smpp_statuses["ESME_ROK"],0)
	
    def __body__(self):
	return self.body

    @classmethod
    def __reverce__(self,pck,pdu_header=None):
	if (pdu_header==None):
	    pdu_header = __sb_pdu_header__.__reverce__(pck)
	if (len(pck)>16):
	    resp = __sb_custom__(body=pck[16:])    
	else:
	    resp = __sb_custom__() 
	resp.__copy__(pdu_header)
	return resp

    def __str__(self):
	res = str(__sb_pdu_header__.__str__(self))
	res += "BODY:\n"
	res +="\thex:%s" % toHexString(self.__body__()) 
	return res
 
    def pck(self):
	return self.__head__()+self.__body__()

# Пакет ошибки
class __sb_generic_nack__(__sb_pdu_header__):
    def __init__(self,command_id=smpp_command_id["generic_nack"],smpp_status=smpp_statuses["ESME_ROK"]):
	__sb_pdu_header__.__init__(self,command_id,smpp_status,0)
	
    def __body__(self):
	return ""

    @classmethod
    def __reverce__(self,pck,pdu_header=None):
	if (pdu_header==None):
	    pdu_header = __sb_pdu_header__.__reverce__(pck)
	resp = __generic_nack__()    
	resp.__copy__(pdu_header)
	return resp

    def __str__(self):
	res = str(__sb_pdu_header__.__str__(self))
	res += "BODY:\n"
	res +="\thex:%s" % toHexString(self.__body__()) 
	return res
 
    def pck(self):
	return self.__head__()+self.__body__()

class __sb_submit_sm_resp__(__sb_pdu_header__):
    def __init__(self,command_id=smpp_command_id["submit_sm_resp"],smpp_status=smpp_statuses["ESME_ROK"],message_id=""):
	self.message_id = message_id
	__sb_pdu_header__.__init__(self,command_id,smpp_status,0)
	
    def __body__(self):
	res = to_c_octetstring(self.message_id,65)
	return res

    @classmethod
    def __reverce__(self,pck,pdu_header=None):
	if (pdu_header==None):
	    pdu_header = __sb_pdu_header__.__reverce__(pck)
	resp = __sb_submit_sm_resp__(message_id=get_c_octetstring(pck[16:],65))    
	resp.__copy__(pdu_header)
	return resp

    def __str__(self):
	res = str(__sb_pdu_header__.__str__(self))
	res += "BODY:\n"
	res +="\tmessage_id:%s\n" % self.message_id
	res +="\thex:%s" % toHexString(self.__body__()) 
	return res
 
    def pck(self):
	return self.__head__()+self.__body__()



class __sb_submit_sm__(__sb_pdu_header__):
    def __init__(self,service_type="",source_addr_ton=1,source_addr_npi=1,source_addr="",\
    dest_addr_ton=1,dest_addr_npi=1,destination_addr="",esm_class=0x00000000,protocol_id=0,\
    priority_flag=0,schedule_delivery_time="",validity_period="",registered_delivery=0,\
    replace_if_present_flag=0,data_coding=0x00000000,sm_default_msg_id=0,short_message="",optionals="",command_id=smpp_command_id["submit_sm"]):
	self.service_type=service_type
	self.source_addr_ton=source_addr_ton
	self.source_addr_npi=source_addr_npi
	self.source_addr=source_addr
	self.dest_addr_ton=dest_addr_ton
	self.dest_addr_npi=dest_addr_npi
	self.destination_addr=destination_addr
	self.esm_class=esm_class
	self.protocol_id=protocol_id
	self.priority_flag=priority_flag
	self.schedule_delivery_time=schedule_delivery_time
	self.validity_period=validity_period
	self.registered_delivery=registered_delivery
	self.replace_if_present_flag=replace_if_present_flag
	self.data_coding=data_coding
	self.sm_default_msg_id=sm_default_msg_id
	#self.sm_length=sm_length
	self.short_message=short_message
	self.optionals=""
	__sb_pdu_header__.__init__(self,command_id,smpp_statuses["ESME_ROK"],0)
	
    def __body__(self):
	return to_c_octetstring(self.service_type,6)+chr(self.source_addr_ton)+chr(self.source_addr_npi)+to_c_octetstring(self.source_addr,21)+\
	chr(self.dest_addr_ton)+chr(self.dest_addr_npi)+to_c_octetstring(self.destination_addr,21)+chr(self.esm_class)+chr(self.protocol_id)+chr(self.priority_flag)+\
	to_c_octetstring(self.schedule_delivery_time,17)+to_c_octetstring(self.validity_period,17)+chr(self.registered_delivery)+chr(self.replace_if_present_flag)+\
	chr(self.data_coding)+chr(self.sm_default_msg_id)+chr(len(self.short_message))+self.short_message+self.optionals
	
    @classmethod
    def __reverce__(self,pck,pdu_header=None):
	if (pdu_header==None):
	    pdu_header = __sb_pdu_header__.__reverce__(pck)
	pck = pck[16:]
	print toHexString(pck)
	resp = __sb_submit_sm__()
	resp.service_type,pck = get_c_octetstring(pck,6,True)
	print toHexString(pck)
	resp.source_addr_ton = ord(pck[0])
	resp.source_addr_npi = ord(pck[1])
	resp.source_addr,pck = get_c_octetstring(pck[2:],21,True)
	print toHexString(pck)
	resp.dest_addr_ton = ord(pck[0])
	resp.dest_addr_npi = ord(pck[1])
	resp.destination_addr,pck = get_c_octetstring(pck[2:],21,True)
	resp.esm_class = ord(pck[0])
	resp.protocol_id = ord(pck[1])
	resp.priority_flag = ord(pck[2])
	resp.schedule_delivery_time,pck = get_c_octetstring(pck[3:],17,True)
	resp.validity_period,pck = get_c_octetstring(pck,17,True)
	resp.registered_delivery = ord(pck[0])
	resp.replace_if_present_flag = ord(pck[1])
	resp.data_coding = ord(pck[2])
	resp.sm_default_msg_id = ord(pck[3])
	smlen = ord(pck[4])
	pck = pck[5:]
	resp.short_message = pck[:smlen]
	resp.optionals = pck[smlen:]
	
	resp.__copy__(pdu_header)
	return resp

    def __str__(self):
	res = str(__sb_pdu_header__.__str__(self))
	res += "BODY:\n"
	res += "\tservice_type:%s\n" % self.service_type
	res += "\tsource      ton:%d npi:%d addr:[%s]\n" % (self.source_addr_ton,self.source_addr_npi,self.source_addr)
	res += "\tdestination ton:%d npi:%d addr:[%s]\n" % (self.dest_addr_ton,self.dest_addr_npi,self.destination_addr)
	res += "\tesm_class:%d (%s)\n" % (self.esm_class,hEX(self.esm_class))
	res += "\tprotocol_id:%d (%s)\n" % (self.protocol_id ,hEX(self.protocol_id))
	res += "\tpriority_flag:%d (%s)\n" % (self.priority_flag ,hEX(self.priority_flag))
	res += "\tschedule_delivery_time:%s\n" % self.schedule_delivery_time
	res += "\tvalidity_period:%s\n" % self.validity_period
	res += "\tregistered_delivery:%d (%s)\n" % (self.registered_delivery ,hEX(self.registered_delivery))
	res += "\treplace_if_present_flag:%d (%s)\n" % (self.replace_if_present_flag ,hEX(self.replace_if_present_flag))
	res += "\tdata_coding:%d (%s)\n" % (self.data_coding ,hEX(self.data_coding))
	res += "\tsm_default_msg_id:%d (%s)\n" % (self.sm_default_msg_id ,hEX(self.sm_default_msg_id))
	res += "\tsm_len:%d\n" % (len(self.short_message))
	res += "\tshort_message:%s (%s)\n" % (self.short_message,toHexString(self.short_message))
	res +="\toptionals_hex:%s\n" % toHexString(self.optionals) 
	res +="\thex:%s" % toHexString(self.__body__()) 
	return res
 
    def pck(self):
	return self.__head__()+self.__body__()




########################################
# SMPP Optional Parameter Headers
########################################

class __sb_tlv__():
    def __init__(self,tag):
	self.tag = tag
	self.tag_text = "tlv_reserved"
	self.tag_text_technology = "Generic"
    
    def __len__(self):
	return len(self.__value__())

    def __str__(self):
	res ="\tOPTIONAL:\n"
	
	for c in smpp_optional_tags:
	    if (smpp_optional_tags[c]==self.tag):
		self.tag_text = c
		self.tag_text_technology = smpp_optional_tags_technology[c]
		break
	res+= "\t\tTag:%s (%s), Tech:%s\n" % (self.tag_text,hEX(self.tag,4),self.tag_text_technology)
	return res

    def __pck__(self):
	return toWORD(self.tag)+toWORD(self.__len__)+self.__value__()

class __sb_singleint_tlv__(__sb_tlv__):
    def __init__(self,tag=smpp_optional_tags["tlv_reserved"],value=0):
	self.value = value
	__sb_tlv__.__init__(self,tag)

    def __str__(self):
	res =  __sb_tlv__.__str__(self)
	ret +="\t\tValue:"+hEX(val,2)+"\n"
	return res

    def __value__(self):
	return chr(value)

    @classmethod
    def __revert__(self,pck,start=0):
	tag = fromWORD(pck[start:start+2])
	length = fromWORD(pck[start+2:start+4])
	value = ord(pck[start+4:start+4+length])
	return __sb_reserved_tlv__(tag,value)


class __sb_doubleint_tlv__(__sb_tlv__):
    def __init__(self,tag=smpp_optional_tags["tlv_reserved"],value=0):
	self.value = value
	__sb_tlv__.__init__(self,tag)

    def __str__(self):
	res =  __sb_tlv__.__str__(self)
	ret +="\t\tValue:"+hEX(val,4)+"\n"
	return res

    def __value__(self):
	return toWORD(value)

    @classmethod
    def __revert__(self,pck,start=0):
	tag = fromWORD(pck[start:start+2])
	length = fromWORD(pck[start+2:start+4])
	value = fromWORD(pck[start+4:start+4+length])
	return __sb_reserved_tlv__(tag,value)


class __sb_quadleint_tlv__(__sb_tlv__):
    def __init__(self,tag=smpp_optional_tags["tlv_reserved"],value=0):
	self.value = value
	__sb_tlv__.__init__(self,tag)

    def __str__(self):
	res =  __sb_tlv__.__str__(self)
	ret +="\t\tValue:"+hEX(val)+"\n"
	return res

    def __value__(self):
	return toDWORD(value)

    @classmethod
    def __revert__(self,pck,start=0):
	tag = fromWORD(pck[start:start+2])
	length = fromWORD(pck[start+2:start+4])
	value = fromDWORD(pck[start+4:start+4+length])
	return __sb_reserved_tlv__(tag,value)


class __sb_reserved_tlv__(__sb_tlv__):
    def __init__(self,tag=smpp_optional_tags["tlv_reserved"],value=""):
	self.value = value
	__sb_tlv__.__init__(self,tag)

    def __value__(self):
	return value

    
    def __str__(self):
	res =  __sb_tlv__.__str__(self)
	ret +="\t\tValue:"+toHexString(self.value)+"\n"
	return res

    @classmethod
    def __revert__(self,pck,start=0):
	tag = fromWORD(pck[start:start+2])
	length = fromWORD(pck[start+2:start+4])
	value = pck[start+4:start+4+length]
	return __sb_reserved_tlv__(tag,value)
	