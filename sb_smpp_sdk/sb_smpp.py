#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Проект: Средства разработки приложений использующих протокола SMPP 3.4
#
# sb_smpp.py - все основные пакеты протокола SMPP 3.4
# 
# Автор: Дмитрий Высочин
# Дата: 16.03.2008


import sb_pdu
from smpputil import *

class bind_transmitter(sb_pdu.__sb_bind__):
    def __init__(self,system_id,password,system_type="cpa",interface_version=0x00000034,addr_ton=0x00,addr_npi=0x00,addr_range=""):
	sb_pdu.__sb_bind__.__init__(self,system_id,password,system_type,interface_version,addr_ton,addr_npi,addr_range,smpp_command_id["bind_transmitter"])
	
class bind_receiver(sb_pdu.__sb_bind__):
    def __init__(self,system_id,password,system_type="cpa",interface_version=0x00000034,addr_ton=0x00,addr_npi=0x00,addr_range=""):
	sb_pdu.__sb_bind__.__init__(self,system_id,password,system_type,interface_version,addr_ton,addr_npi,addr_range,smpp_command_id["bind_receiver"])
	
class bind_transceiver(sb_pdu.__sb_bind__):
    def __init__(self,system_id,password,system_type="cpa",interface_version=0x00000034,addr_ton=0x00,addr_npi=0x00,addr_range=""):
	sb_pdu.__sb_bind__.__init__(self,system_id,password,system_type,interface_version,addr_ton,addr_npi,addr_range)

class bind_transceiver_resp(sb_pdu.__sb_bind_resp__): pass

class unbind_resp(sb_pdu.__sb_custom__): 
    def __init__(self):
	sb_pdu.__sb_custom__.__init__(self,command_id=smpp_command_id["unbind_resp"]) 
	
	
class unbind(sb_pdu.__sb_custom__):
    def __init__(self):
	sb_pdu.__sb_custom__.__init__(self,command_id=smpp_command_id["unbind"]) 

class generic_nack(sb_pdu.__sb_generic_nack__): pass

class enquire_link_resp(sb_pdu.__sb_custom__):
    def __init__(self):
	sb_pdu.__sb_custom__.__init__(self,command_id=smpp_command_id["enquire_link_resp"]) 

class enquire_link(sb_pdu.__sb_custom__):
    def __init__(self):
	sb_pdu.__sb_custom__.__init__(self,command_id=smpp_command_id["enquire_link"])
    
class submit_sm(sb_pdu.__sb_submit_sm__):  pass

class submit_sm_resp(sb_pdu.__sb_submit_sm_resp__):  pass
    

class deliver_sm(sb_pdu.__sb_submit_sm__): 
    def __init__(self,service_type="",source_addr_ton=1,source_addr_npi=1,source_addr="",\
    dest_addr_ton=1,dest_addr_npi=1,destination_addr="",esm_class=0x00000000,protocol_id=0,\
    priority_flag=0,schedule_delivery_time="",validity_period="",registered_delivery=0,\
    replace_if_present_flag=0,data_coding=0x00000000,sm_default_msg_id=0,short_message="",optionals=[],command_id=smpp_command_id["submit_sm"]):
	sb_pdu.__sb_submit_sm__.__init__(self,service_type,source_addr_ton,source_addr_npi,source_addr,\
    dest_addr_ton,dest_addr_npi,destination_addr,esm_class,protocol_id,\
    priority_flag,schedule_delivery_time,validity_period,registered_delivery,\
    replace_if_present_flag,data_coding,sm_default_msg_id,short_message,optionals,command_id)

    
class deliver_sm_resp(sb_pdu.__sb_submit_sm_resp__):
    def __init__(self,command_id=smpp_command_id["deliver_sm_resp"],smpp_status=smpp_statuses["ESME_ROK"]):
	sb_pdu.__sb_submit_sm_resp__.__init__(self,command_id,smpp_status,"")


def get_command_class(command_id):
    if (command_id==0x80000103): return data_sm_resp
    elif (command_id==0x80000002): return bind_transmitter_resp
    elif (command_id==0x80000009): return bind_transceiver_resp
    elif (command_id==0x00000002): return bind_transmitter
    elif (command_id==0x80000021): return submit_multi_resp
    elif (command_id==0x80000003): return query_sm_resp
    elif (command_id==0x80000008): return cancel_sm_resp
    elif (command_id==0x80000006): return unbind_resp
    elif (command_id==0x00000001): return bind_receiver
    elif (command_id==0x80000000): return generic_nack
    elif (command_id==0x00000009): return bind_transceiver
    elif (command_id==0x00000004): return submit_sm
    elif (command_id==0x80000007): return replace_sm_resp
    elif (command_id==0x00000005): return deliver_sm
    elif (command_id==0x00000102): return alert_notification
    elif (command_id==0x00000103): return data_sm
    elif (command_id==0x00000021): return submit_multi
    elif (command_id==0x00000015): return enquire_link
    elif (command_id==0x0000000B): return outbind
    elif (command_id==0x00000008): return cancel_sm
    elif (command_id==0x00000003): return query_sm
    elif (command_id==0x00000007): return replace_sm
    elif (command_id==0x80000004): return submit_sm_resp
    elif (command_id==0x80000005): return deliver_sm_resp
    elif (command_id==0x00000006): return unbind
    elif (command_id==0x80000001): return bind_receiver_resp
    elif (command_id==0x80000015): return enquire_link_resp
    else: return generic_nack

def class_from_pck(pck):
    header = sb_pdu.__sb_pdu_header__.__reverce__(pck)
    cls = get_command_class(header.command_id)
    return cls.__reverce__(pck,header)


