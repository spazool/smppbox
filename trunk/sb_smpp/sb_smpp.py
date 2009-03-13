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
