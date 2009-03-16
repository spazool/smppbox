#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Проект: Средства разработки приложений использующих протокола SMPP 3.4
#
# sb_smpp_opt.py - SMPP Optional Parameter Description
# 
# Автор: Дмитрий Высочин
# Дата: 16.03.2008

def tlv_reserved(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["tlv_reserved"],value="")

def dest_addr_subunit(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dest_addr_subunit"],value=0)

def source_addr_subunit(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_addr_subunit"],value=0)

def dest_network_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dest_network_type"],value=0)

def source_network_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_network_type"],value=0)

def dest_bearer_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dest_bearer_type"],value=0)

def source_bearer_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_bearer_type"],value=0)

def dest_telematics_id(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["dest_telematics_id"],value="")

def source_telematics_id(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["source_telematics_id"],value=0)

def qos_time_to_live(__sb_quadleint_tlv__):
    def __init__(smpp_optional_tags["qos_time_to_live"],value=0)

def payload_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["payload_type"],value=0)

def additional_status_info_text(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["additional_status_info_text"],value="")

def receipted_message_id(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["receipted_message_id"],value="")

def ms_msg_wait_facilities(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ms_msg_wait_facilities"],value=0)

def privacy_indicator(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["privacy_indicator"],value=0)

def source_subaddress(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["source_subaddress"],value="")

def dest_subaddress(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["dest_subaddress"],value="")

def user_message_reference(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["user_message_reference"],value="")

def user_response_code(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["user_response_code"],value=0)

def language_indicator(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["language_indicator"],value=0)

def source_port(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["source_port"],value=0)

def destination_port(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["destination_port"],value=0)

def sar_msg_ref_num(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["sar_msg_ref_num"],value=0)

def sar_total_segments(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["sar_total_segments"],value=0)

def sar_segment_seqnum(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["sar_segment_seqnum"],value=0)

def sc_interface_version(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["sc_interface_version"],value=0)

def display_time(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["display_time"],value=0)

def ms_validity(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ms_validity"],value=0)

def dpf_result(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["dpf_result"],value=0)

def set_dpf(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["set_dpf"],value=0)

def ms_availability_status(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ms_availability_status"],value=0)

def network_error_code(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["network_error_code"],value="")

def message_payload(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["message_payload"],value="")

def delivery_failure_reason(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["delivery_failure_reason"],value=0)

def more_messages_to_send(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["more_messages_to_send"],value=0)

def message_state(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["message_state"],value=0)

def callback_num(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["callback_num"],value="")

def callback_num_pres_ind(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["callback_num_pres_ind"],value=0)

def callback_num_atag(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["callback_num_atag"],value="")

def number_of_messages(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["number_of_messages"],value=0)

def sms_signal(__sb__doubleint_tlv__):
    def __init__(smpp_optional_tags["sms_signal"],value=0)

def alert_on_message_delivery(__sb_reserved_tlv__)
    def __init__(smpp_optional_tags["alert_on_message_delivery"],value="")

def its_reply_type(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["its_reply_type"],value=0)

def its_session_info(__sb_reserved_tlv__):
    def __init__(smpp_optional_tags["its_session_info"],value="")

def ussd_service_op(__sb__singleint_tlv__):
    def __init__(smpp_optional_tags["ussd_service_op"],value=0)

