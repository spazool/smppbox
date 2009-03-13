#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    replace_if_present_flag=0,data_coding=0x00000000,sm_default_msg_id=0,short_message="",optionals="",command_id=smpp_command_id["submit_sm"]):
	sb_pdu.__sb_submit_sm__.__init__(self,service_type,source_addr_ton,source_addr_npi,source_addr,\
    dest_addr_ton,dest_addr_npi,destination_addr,esm_class,protocol_id,\
    priority_flag,schedule_delivery_time,validity_period,registered_delivery,\
    replace_if_present_flag,data_coding,sm_default_msg_id,short_message,optionals,command_id)

    
class deliver_sm_resp(sb_pdu.__sb_submit_sm_resp__):
    def __init__(self,command_id=smpp_command_id["deliver_sm_resp"],smpp_status=smpp_statuses["ESME_ROK"]):
	sb_pdu.__sb_submit_sm_resp__.__init__(self,command_id,smpp_status,"")


def class_from_pck(pck,path=""):
    header = sb_pdu.__sb_pdu_header__.__reverce__(pck)
    return  get_smppclass(get_smppclass_name(header),path).__reverce__(pck,header)


