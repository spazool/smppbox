#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################
#
# Класс с служебными ф-иями
#
#####################################

import sys,datetime

colors = [ "\x1b\x5b0;%d;49m" % f for f in range(30,38) ] + [ "\x1b\x5b1;%d;49m" % f for f in range(30,38) ] 


def toDWORD(i):
    return ''.join( map(chr,[x&0xff for x in [i>>24,i>>16,i>>8,i]]))
    #return ''.join( map(chr,[x&0xff for x in [i,i>>8,i>>16,i>>24]]))

def fromDWORD(s):
    #return ord(s[0]) + (ord(s[1])<<8) + (ord(s[2])<<16) + (ord(s[3])<<24)
    return ord(s[3]) + (ord(s[2])<<8) + (ord(s[1])<<16) + (ord(s[0])<<24)

def toWORD(i):
    return ''.join(map(chr,[x&0xff for x in [i,i>>8]]))

def fromWORD(s):
    return ord(s[0]) + (ord(s[1])<<8)

def toHexString(pck,spliter=" "):
    return spliter.join(["%02X" % ord(p) for p in pck ])

def fromHexString(hexstring,spliter=" "):
    return ''.join([ "%s" % chr(int(h,16)) for h in hexstring.split(spliter) ])

def upLen(string,lenght,sym="\x00"):
    return string.ljust(lenght-len(string),sym)

def to_c_octetstring(string,lenght):
    if (len(string)<lenght):
	return string+"\x00"
    else: 
	return Exception("Lenght error. max(%d)" % lenght)

def get_c_octetstring(string,length=0):
    if (length > 0):
	string = string[:length]
    if (string.find("\x00")==-1):
	raise Exception("\\x00 not found in C-Octet String")
    return string[:string.find("\x00")-1]

def to_c_octetstring_hex(string,lenght):
    string = string.toHexString(string,"")
    if (len(string)<lenght):
	return string+"\x00"
    else: 
	return Exception("Lenght error. max(%d)" % lenght)


def hEX(intg):
    return "0x"+ (hex(intg)[2:].rjust(8,"0")).upper()


def say(text,level=0,group=""):

    levelcode="[INFO ] "
    colorcode = ""
    if (level==1): levelcode="[DEBUG] "
    if (level==2): levelcode="[ERROR] "
    if (group!=""): group = "[%s] " % group

    text=datetime.datetime.today().strftime("[%Y-%m-%d %H:%M:%S] ")+levelcode+group+text
    
    sys.stdout.write(unicode(text+"\n","utf-8",errors='replace').encode(output_encoding,"ignore"))
    sys.stdout.flush()




smpp_command_id={}
smpp_command_id["generic_nack"]         = 0x80000000
smpp_command_id["bind_receiver"]        = 0x00000001
smpp_command_id["bind_receiver_resp"]   = 0x80000001
smpp_command_id["bind_transmitter"]     = 0x00000002
smpp_command_id["bind_transmitter_resp"]= 0x80000002
smpp_command_id["query_sm"]             = 0x00000003
smpp_command_id["query_sm_resp"]        = 0x80000003
smpp_command_id["submit_sm"]            = 0x00000004
smpp_command_id["submit_sm_resp"]       = 0x80000004
smpp_command_id["deliver_sm"]           = 0x00000005
smpp_command_id["deliver_sm_resp"]      = 0x80000005
smpp_command_id["unbind"]               = 0x00000006
smpp_command_id["unbind_resp"]          = 0x80000006
smpp_command_id["replace_sm"]           = 0x00000007
smpp_command_id["replace_sm_resp"]      = 0x80000007
smpp_command_id["cancel_sm"]            = 0x00000008
smpp_command_id["cancel_sm_resp"]       = 0x80000008
smpp_command_id["bind_transceiver"]     = 0x00000009
smpp_command_id["bind_transceiver_resp"]= 0x80000009
smpp_command_id["outbind"]              = 0x0000000B
smpp_command_id["enquire_link"]         = 0x00000015
smpp_command_id["enquire_link_resp"]    = 0x80000015
smpp_command_id["submit_multi"]         = 0x00000021
smpp_command_id["submit_multi_resp"]    = 0x80000021
smpp_command_id["alert_notification"]   = 0x00000102
smpp_command_id["data_sm"]              = 0x00000103
smpp_command_id["data_sm_resp"]         = 0x80000103

def get_smppclass_name(header):
    for com in smpp_command_id:
	if (header.command_id==smpp_command_id[com]):
	    return com
    return "unknown_reserved"

def get_smppclass(name):
    pck = __import__("sb_smpp")
    cls = getattr(pck,name)
    return cls


smpp_statuses = {}
smpp_statuses["ESME_ROK"] = 0x00000000
smpp_statuses["ESME_RINVMSGLEN"] = 0x00000001
smpp_statuses["ESME_RINVCMDLEN"] = 0x00000002
smpp_statuses["ESME_RINVCMDID"] = 0x00000003
smpp_statuses["ESME_RINVBNDSTS"] = 0x00000004
smpp_statuses["ESME_RALYBND"] = 0x00000005
smpp_statuses["ESME_RINVPRTFLG"] = 0x00000006
smpp_statuses["ESME_RINVREGDLVFLG"] = 0x00000007
smpp_statuses["ESME_RSYSERR"] = 0x00000008
smpp_statuses["ESME_RINVSRCADR"] = 0x0000000A
smpp_statuses["ESME_RINVDSTADR"] = 0x0000000B
smpp_statuses["ESME_RINVMSGID"] = 0x0000000C
smpp_statuses["ESME_RBINDFAIL"] = 0x0000000D
smpp_statuses["ESME_RINVPASWD"] = 0x0000000E
smpp_statuses["ESME_RINVSYSID"] = 0x0000000F
smpp_statuses["ESME_RCANCELFAIL"] = 0x00000011
smpp_statuses["ESME_RREPLACEFAIL"] = 0x00000013
smpp_statuses["ESME_RMSGQFUL"] = 0x00000014
smpp_statuses["ESME_RINVSERTYP"] = 0x00000015
smpp_statuses["ESME_RINVNUMDESTS"] = 0x00000033
smpp_statuses["ESME_RINVDLNAME"] = 0x00000034
smpp_statuses["ESME_RINVDESTFLAG"] = 0x00000040
smpp_statuses["ESME_RINVSUBREP"] = 0x00000042
smpp_statuses["ESME_RINVESMCLASS"] = 0x00000043
smpp_statuses["ESME_RCNTSUBDL"] = 0x00000044
smpp_statuses["ESME_RSUBMITFAIL"] = 0x00000045
smpp_statuses["ESME_RINVSRCTON"] = 0x00000048
smpp_statuses["ESME_RINVSRCNPI"] = 0x00000049
smpp_statuses["ESME_RINVDSTTON"] = 0x00000050
smpp_statuses["ESME_RINVDSTNPI"] = 0x00000051
smpp_statuses["ESME_RINVSYSTYP"] = 0x00000053
smpp_statuses["ESME_RINVREPFLAG"] = 0x00000054
smpp_statuses["ESME_RINVNUMMSGS"] = 0x00000055
smpp_statuses["ESME_RTHROTTLED"] = 0x00000058
smpp_statuses["ESME_RINVSCHED"] = 0x00000061
smpp_statuses["ESME_RINVSCHED"] = 0x00000061
smpp_statuses["ESME_RINVEXPIRY"] = 0x00000062
smpp_statuses["ESME_RINVDFTMSGID"] = 0x00000063
smpp_statuses["ESME_RX_T_APPN"] = 0x00000064
smpp_statuses["ESME_RX_P_APPN"] = 0x00000065
smpp_statuses["ESME_RX_R_APPN"] = 0x00000066
smpp_statuses["ESME_RQUERYFAIL"] = 0x00000067
smpp_statuses["ESME_RINVOPTPARSTREAM"] = 0x000000C0
smpp_statuses["ESME_ROPTPARNOTALLWD"] = 0x000000C1
smpp_statuses["ESME_RINVPARLEN"] = 0x000000C2
smpp_statuses["ESME_RMISSINGOPTPARAM"] = 0x000000C3
smpp_statuses["ESME_RINVOPTPARAMVAL"] = 0x000000C4
smpp_statuses["ESME_RDELIVERYFAILURE"] = 0x000000FE
smpp_statuses["ESME_RUNKNOWNERR"] = 0x000000FF

smpp_statuses_text = {}
smpp_statuses_text["ESME_ROK"] = "No Error"
smpp_statuses_text["ESME_RINVMSGLEN"] = "Message Length is invalid"
smpp_statuses_text["ESME_RINVCMDLEN"] = "Command Length is invalid"
smpp_statuses_text["ESME_RINVCMDID"] = "Invalid Command ID"
smpp_statuses_text["ESME_RINVBNDSTS"] = "Incorrect BIND Status for given com-mand"
smpp_statuses_text["ESME_RALYBND"] = "ESME Already in Bound State"
smpp_statuses_text["ESME_RINVPRTFLG"] = "Invalid Priority Flag"
smpp_statuses_text["ESME_RINVREGDLVFLG"] = "Invalid Registered Delivery Flag"
smpp_statuses_text["ESME_RSYSERR"] = "System Error"
smpp_statuses_text["ESME_RINVSRCADR"] = "Invalid Source Address"
smpp_statuses_text["ESME_RINVDSTADR"] = "Invalid Dest Addr"
smpp_statuses_text["ESME_RINVMSGID"] = "Message ID is invalid"
smpp_statuses_text["ESME_RBINDFAIL"] = "Bind Failed"
smpp_statuses_text["ESME_RINVPASWD"] = "Invalid Password"
smpp_statuses_text["ESME_RINVSYSID"] = "Invalid System ID"
smpp_statuses_text["ESME_RCANCELFAIL"] = "Cancel SM Failed"
smpp_statuses_text["ESME_RREPLACEFAIL"] = "Replace SM Failed"
smpp_statuses_text["ESME_RMSGQFUL"] = "Message Queue Full"
smpp_statuses_text["ESME_RINVSERTYP"] = "Invalid Service Type"
smpp_statuses_text["ESME_RINVNUMDESTS"] = "Invalid number of destinations"
smpp_statuses_text["ESME_RINVDLNAME"] = "Invalid Distribution List name"
smpp_statuses_text["ESME_RINVDESTFLAG"] = "Destination flag is invalid (submit_multi)"
smpp_statuses_text["ESME_RINVSUBREP"] = "Invalid ‘submit with replace’ request (i.e. submit_sm with replace_if_present_flag set)"
smpp_statuses_text["ESME_RINVESMCLASS"] = "Invalid esm_class field data"
smpp_statuses_text["ESME_RCNTSUBDL"] = "Cannot Submit to Distribution List"
smpp_statuses_text["ESME_RSUBMITFAIL"] = "submit_sm or submit_multi failed"
smpp_statuses_text["ESME_RINVSRCTON"] = "Invalid Source address TON"
smpp_statuses_text["ESME_RINVSRCNPI"] = "Invalid Source address NPI"
smpp_statuses_text["ESME_RINVDSTTON"] = "Invalid Destination address TON"
smpp_statuses_text["ESME_RINVDSTNPI"] = "Invalid Destination address NPI"
smpp_statuses_text["ESME_RINVSYSTYP"] = "Invalid system_type field"
smpp_statuses_text["ESME_RINVREPFLAG"] = "Invalid replace_if_present flag"
smpp_statuses_text["ESME_RINVNUMMSGS"] = "Invalid number of messages"
smpp_statuses_text["ESME_RTHROTTLED"] = "Throttling error (ESME has exceeded allowed message limits)"
smpp_statuses_text["ESME_RINVSCHED"] = "Invalid Scheduled Delivery Time"
smpp_statuses_text["ESME_RINVSCHED"] = "Invalid Scheduled Delivery Time"
smpp_statuses_text["ESME_RINVEXPIRY"] = "Invalid message     validity  period (Expiry time)"
smpp_statuses_text["ESME_RINVDFTMSGID"] = "Predefined Message Invalid or Not Found"
smpp_statuses_text["ESME_RX_T_APPN"] = "ESME Receiver Temporary App Error Code"
smpp_statuses_text["ESME_RX_P_APPN"] = "ESME Receiver Permanent App Error Code"
smpp_statuses_text["ESME_RX_R_APPN"] = "ESME Receiver Reject Message Error Code"
smpp_statuses_text["ESME_RQUERYFAIL"] = "query_sm request failed"
smpp_statuses_text["ESME_RINVOPTPARSTREAM"] = "Error in the optional part of the PDU Body."
smpp_statuses_text["ESME_ROPTPARNOTALLWD"] = "Optional Parameter not allowed"
smpp_statuses_text["ESME_RINVPARLEN"] = "Invalid Parameter Length."
smpp_statuses_text["ESME_RMISSINGOPTPARAM"] = "Expected Optional Parameter missing"
smpp_statuses_text["ESME_RINVOPTPARAMVAL"] = "Invalid Optional Parameter Value"
smpp_statuses_text["ESME_RDELIVERYFAILURE"] = "Delivery   Failure (used for data_sm_resp)"
smpp_statuses_text["ESME_RUNKNOWNERR"] = "Unknown Error"
