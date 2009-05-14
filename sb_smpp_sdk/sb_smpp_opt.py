#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Проект: Средства разработки приложений использующих протокола SMPP 3.4
#
# sb_smpp_opt.py - SMPP Optional Parameter Description
# 
# Автор: Дмитрий Высочин
# Дата: 16.03.2008

import sb_pdu
from smpputil import *

########################################
# SMPP Optional Parameter Headers
########################################

class __sb_tlv__():
    def __init__(self,tag,value=0):
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

    def pck(self):
	return toWORD(self.tag)+toWORD(self.__len__())+self.__value__()

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

    def __len__(self):
	return 1
	

    @classmethod
    def __revert__(self,pck,start=0):
	tag = fromWORD(pck[start:start+2])
	length = fromWORD(pck[start+2:start+4])
	self.value = ord(pck[start+4:start+4+length])
	return __sb_singleint_tlv__(tag,self.value)


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

    def __len__(self):
	return 2


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

    def __len__(self):
	return 4


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
	return self.value

#    def __len__(self):
#	return len(self.__value__)
    
    def __str__(self):
	res =  __sb_tlv__.__str__(self)
	res +="\t\tValue:"+toHexString(self.value)+"\n"
	return res

    @classmethod
    def __revert__(self,pck,start=0):
	tag = fromWORD(pck[start:start+2])
	length = fromWORD(pck[start+2:start+4])
	value = pck[start+4:start+4+length]
	return __sb_reserved_tlv__(tag,value)




class tlv_reserved(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["tlv_reserved"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class dest_addr_subunit(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["dest_addr_subunit"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class source_addr_subunit(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["source_addr_subunit"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class dest_network_type(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["dest_network_type"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class source_network_type(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["source_network_type"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class dest_bearer_type(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["dest_bearer_type"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class source_bearer_type(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["source_bearer_type"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class dest_telematics_id(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["dest_telematics_id"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class source_telematics_id(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["source_telematics_id"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class qos_time_to_live(__sb_quadleint_tlv__):
    def __init__(tag=smpp_optional_tags["qos_time_to_live"],value=0):
        __sb_quadleint_tlv__.__init__(self,tag,value)

class payload_type(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["payload_type"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class additional_status_info_text(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["additional_status_info_text"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class receipted_message_id(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["receipted_message_id"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class ms_msg_wait_facilities(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["ms_msg_wait_facilities"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class privacy_indicator(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["privacy_indicator"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class source_subaddress(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["source_subaddress"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class dest_subaddress(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["dest_subaddress"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class user_message_reference(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["user_message_reference"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class user_response_code(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["user_response_code"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class language_indicator(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["language_indicator"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class source_port(__sb_doubleint_tlv__):
    def __init__(tag=smpp_optional_tags["source_port"],value=0):
        __sb_doubleint_tlv__.__init__(self,tag,value)

class destination_port(__sb_doubleint_tlv__):
    def __init__(tag=smpp_optional_tags["destination_port"],value=0):
        __sb_doubleint_tlv__.__init__(self,tag,value)

class sar_msg_ref_num(__sb_doubleint_tlv__):
    def __init__(tag=smpp_optional_tags["sar_msg_ref_num"],value=0):
        __sb_doubleint_tlv__.__init__(self,tag,value)

class sar_total_segments(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["sar_total_segments"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class sar_segment_seqnum(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["sar_segment_seqnum"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class sc_interface_version(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["sc_interface_version"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class display_time(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["display_time"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class ms_validity(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["ms_validity"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class dpf_result(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["dpf_result"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class set_dpf(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["set_dpf"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class ms_availability_status(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["ms_availability_status"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class network_error_code(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["network_error_code"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class message_payload(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["message_payload"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class delivery_failure_reason(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["delivery_failure_reason"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class more_messages_to_send(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["more_messages_to_send"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class message_state(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["message_state"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class callback_num(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["callback_num"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class callback_num_pres_ind(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["callback_num_pres_ind"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class callback_num_atag(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["callback_num_atag"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class number_of_messages(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["number_of_messages"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class sms_signal(__sb_doubleint_tlv__):
    def __init__(tag=smpp_optional_tags["sms_signal"],value=0):
        __sb_doubleint_tlv__.__init__(self,tag,value)

class alert_on_message_delivery(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["alert_on_message_delivery"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class its_reply_type(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["its_reply_type"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)

class its_session_info(__sb_reserved_tlv__):
    def __init__(tag=smpp_optional_tags["its_session_info"],value=""):
        __sb_reserved_tlv__.__init__(self,tag,value)

class ussd_service_op(__sb_singleint_tlv__):
    def __init__(tag=smpp_optional_tags["ussd_service_op"],value=0):
        __sb_singleint_tlv__.__init__(self,tag,value)


def get_tlv_class(tag):
    if (tag==0x0030): return ms_msg_wait_facilities
    elif (tag==0x0427): return message_state
    elif (tag==0x020D): return language_indicator
    elif (tag==0x0381): return callback_num
    elif (tag==0x0303): return callback_num_atag
    elif (tag==0x1203): return sms_signal
    elif (tag==0x0302): return callback_num_pres_ind
    elif (tag==0x0202): return source_subaddress
    elif (tag==0x0205): return user_response_code
    elif (tag==0x020C): return sar_msg_ref_num
    elif (tag==0x0421): return set_dpf
    elif (tag==0x0201): return privacy_indicator
    elif (tag==0x0204): return user_message_reference
    elif (tag==0x0000): return tlv_reserved
    elif (tag==0x0420): return dpf_result
    elif (tag==0x0006): return dest_network_type
    elif (tag==0x1380): return its_reply_type
    elif (tag==0x020F): return sar_segment_seqnum
    elif (tag==0x0019): return payload_type
    elif (tag==0x0008): return dest_telematics_id
    elif (tag==0x0501): return ussd_service_op
    elif (tag==0x000D): return source_addr_subunit
    elif (tag==0x1201): return display_time
    elif (tag==0x0422): return ms_availability_status
    elif (tag==0x000E): return source_network_type
    elif (tag==0x0203): return dest_subaddress
    elif (tag==0x0424): return message_payload
    elif (tag==0x0010): return source_telematics_id
    elif (tag==0x1383): return its_session_info
    elif (tag==0x020B): return destination_port
    elif (tag==0x0007): return dest_bearer_type
    elif (tag==0x0426): return more_messages_to_send
    elif (tag==0x020E): return sar_total_segments
    elif (tag==0x0210): return sc_interface_version
    elif (tag==0x0423): return network_error_code
    elif (tag==0x1204): return ms_validity
    elif (tag==0x000F): return source_bearer_type
    elif (tag==0x0425): return delivery_failure_reason
    elif (tag==0x0017): return qos_time_to_live
    elif (tag==0x001D): return additional_status_info_text
    elif (tag==0x0005): return dest_addr_subunit
    elif (tag==0x020A): return source_port
    elif (tag==0x0304): return number_of_messages
    elif (tag==0x130C): return alert_on_message_delivery
    elif (tag==0x001E): return receipted_message_id
    else: return tlv_reserved
    
def get_optionals(pck_part):
    res = []
    while(len(pck_part)>0):
	cls = get_tlv_class(fromWORD(pck_part[0:2])).__revert__(pck_part)
	res+=[cls]
	pck_part = pck_part[len(cls)+4:]
    return res
