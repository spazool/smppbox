#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Проект: Средства разработки приложений использующих протокола SMPP 3.4
#
# sb_smpp_opt.py - SMPP Optional Parameter Description
# 
# Автор: Дмитрий Высочин
# Дата: 16.03.2008

class tlv_reserved(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["tlv_reserved"],value="")

class dest_addr_subunit(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dest_addr_subunit"],value=0)

class source_addr_subunit(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_addr_subunit"],value=0)

class dest_network_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dest_network_type"],value=0)

class source_network_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_network_type"],value=0)

class dest_bearer_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dest_bearer_type"],value=0)

class source_bearer_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_bearer_type"],value=0)

class dest_telematics_id(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["dest_telematics_id"],value="")

class source_telematics_id(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_telematics_id"],value=0)

class qos_time_to_live(__sb_quadleint_tlv__):
    def __init__(smpp_optional_tags["qos_time_to_live"],value=0)

class payload_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["payload_type"],value=0)

class additional_status_info_text(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["additional_status_info_text"],value="")

class receipted_message_id(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["receipted_message_id"],value="")

class ms_msg_wait_facilities(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ms_msg_wait_facilities"],value=0)

class privacy_indicator(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["privacy_indicator"],value=0)

class source_subaddress(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["source_subaddress"],value="")

class dest_subaddress(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["dest_subaddress"],value="")

class user_message_reference(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["user_message_reference"],value="")

class user_response_code(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["user_response_code"],value=0)

class language_indicator(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["language_indicator"],value=0)

class source_port(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["source_port"],value=0)

class destination_port(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["destination_port"],value=0)

class sar_msg_ref_num(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["sar_msg_ref_num"],value=0)

class sar_total_segments(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["sar_total_segments"],value=0)

class sar_segment_seqnum(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["sar_segment_seqnum"],value=0)

class sc_interface_version(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["sc_interface_version"],value=0)

class display_time(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["display_time"],value=0)

class ms_validity(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ms_validity"],value=0)

class dpf_result(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dpf_result"],value=0)

class set_dpf(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["set_dpf"],value=0)

class ms_availability_status(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ms_availability_status"],value=0)

class network_error_code(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["network_error_code"],value="")

class message_payload(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["message_payload"],value="")

class delivery_failure_reason(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["delivery_failure_reason"],value=0)

class more_messages_to_send(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["more_messages_to_send"],value=0)

class message_state(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["message_state"],value=0)

class callback_num(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["callback_num"],value="")

class callback_num_pres_ind(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["callback_num_pres_ind"],value=0)

class callback_num_atag(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["callback_num_atag"],value="")

class number_of_messages(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["number_of_messages"],value=0)

class sms_signal(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["sms_signal"],value=0)

class alert_on_message_delivery(__sb_reserved_tlv__)
    def __init__(smpp_optional_tags["alert_on_message_delivery"],value="")

class its_reply_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["its_reply_type"],value=0)

class its_session_info(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["its_session_info"],value="")

class ussd_service_op(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ussd_service_op"],value=0)

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
    elif (tag==0x0210): return SC_interface_version
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