# DMARC2Syslog
Python script to read DMARC reports from a mailbox, parse them, format them as syslog messages, and send them to syslog server. 

Useful to send DMARC report to SIEM to build use cases.

-------------------------------------------------------------------------------------------------------------------------------------------------
Supported mailbox access:
  1. EWS (Exchange Web Serivce)


-------------------------------------------------------------------------------------------------------------------------------------------------
Supported Syslog messages foramts:
  1. LEEF v1


-------------------------------------------------------------------------------------------------------------------------------------------------
Requirements:
  1. Python 3.10
  2. exchangelib 4.6.2 : installation command -> pip install exchangelib 


-------------------------------------------------------------------------------------------------------------------------------------------------
How to use it:
  1. Provide the requried configuration in the confgiruation file "config.ini" 
  2. create a task scheduler or cron job to run the script file "start.py", as an example each 10 mintues.
  3. The script manages the last time it checked for reports and it will check starting from last time check.


-------------------------------------------------------------------------------------------------------------------------------------------------
avaiable information for earch record in the DMARC report and the LEEF key name:
XML Tag | LEEF Key
--- | ---
dmarc_report_version | ver=
dmarc_report_metadata_org_name  | orgName=
dmarc_report_metadata_email  | email=
dmarc_report_metadata_extra_contact_info  | extraContactInfo=
dmarc_report_metadata_report_id  | reportID=
dmarc_report_date_range_begin  | dateRangeBegin=
dmarc_report_date_range_end  | dateRangeEnd=
dmarc_report_policy_published_domian  | policyPublishedDomain=
dmarc_report_policy_published_adkim  | policyPublishedADKIM=
dmarc_report_policy_published_aspf  | policyPublishedASPF=
dmarc_report_policy_published_p  | policyPublishedP=
dmarc_report_policy_published_sp  | policyPublishedSP=
dmarc_report_policy_published_pct  | policyPublishedPCT=
dmarc_report_policy_published_fo  | policyPublishedFO=
dmarc_record_row_source_ip  | RecordRowSourceIP=
dmarc_record_row_count  | RecordRowCount=
dmarc_record_row_policy_evaluated_disposition | RecordRowPolicyEvaluatedDisposition=
dmarc_record_row_policy_evaluated_dkim  | RecordRowPolicyEvaluatedDKIM=
dmarc_record_row_policy_evaluated_spf  | RecordRowPolicyEvaluatedSPF=
dmarc_record_identifiers_header_from  | RecordIdentifiersHeaderFrom=
dmarc_record_identifiers_envelope_from  | RecordIdentifiersEnvelopeFrom=
dmarc_record_auth_results_dkim_domain  | RecordAuthResultsDKIMDomain=
dmarc_record_auth_results_dkim_result  | RecordAuthResultsDKIMResult=
dmarc_record_auth_results_dkim_selector  | RecordAuthResultsDKIMSelector=
dmarc_record_auth_results_spf_domain  | RecordAuthResultsSPFDomain=
dmarc_record_auth_results_spf_result  | RecordAuthResultsSPFResult=


-------------------------------------------------------------------------------------------------------------------------------------------------
Configuration File:
Section | Config Tag | Value | Description
---| --- | --- | ---
CONFIG | start_datetime | YYYY-MM-DD-HH:MM | date/time to process the emails starting from it.
CONFIG | srv_max_worker | Number | number of threads to process the reports
CONFIG | mailbox_type | [ews] | connection type to mailbox 
CONFIG | error_log_enable | [true,false] | log errors to the log file .\log\error.log
CONFIG | debug_log_enable | [true,false] | log debug to the log file .\log\error.log
SYSLOG | syslog_server | IP | syslog server IP
SYSLOG | syslog_port | Port Number | Syslog server port number
EWS | ews_username | domain\userName | username to connect to mailbox through EWS
EWS | ews_password | userPass | password to connect to mailbox through EWS
EWS | ews_email | email@domain.com | mailbox email
EWS | ews_service_endpoint | https://mail.domian.com/ews/exchange.asmx | ews service endpoint URL
