#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sb_smpp,sb_pdu
from smpputil import *

p =sb_smpp.bind_transceiver("10301","AAA")
pck = p.pck()

cl = get_smppclass(get_smppclass_name(p))
revclass = cl.__reverce__(p.pck())