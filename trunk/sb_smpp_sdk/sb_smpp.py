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
    
def class_from_pck(pck,path=""):
    header = sb_pdu.__sb_pdu_header__.__reverce__(pck)
    return  get_smppclass(get_smppclass_name(header),path).__reverce__(pck,header)


