import sys
import concurrent.futures
from dmarc import DMARCReport
from ews import ExchangeWebSrv
from utility import Utility
from logger import SyslogClient,ExceptlogClient
from srvconfig import DMARCServiceConfig
from dmarc import DMARCReport


sys.path.append('.')

def main():
    
    init_main()
    
    if(DMARCServiceConfig.mailbox_type == DMARCServiceConfig._mailbox_type_ews):
        attachments_gz = init_ews()
    
    if(attachments_gz is not None):
        init_thread(DMARCServiceConfig.srv_max_worker,attachments_gz)

    DMARCServiceConfig.update_config_start_datetime()

def init_main():
    DMARCServiceConfig.init_config()
    ExceptlogClient.initiate(DMARCServiceConfig.error_log_path,DMARCServiceConfig.error_log_enable,DMARCServiceConfig.debug_log_enable)
    try:
        SyslogClient.initiate(DMARCServiceConfig.syslog_server,DMARCServiceConfig.syslog_port)
    except Exception as exception:
        ExceptlogClient.log_except(exception)

def init_ews():
    try:
        exchangeWebSrv = ExchangeWebSrv(DMARCServiceConfig.ews_username,DMARCServiceConfig.ews_password,DMARCServiceConfig.ews_email,DMARCServiceConfig.ews_service_endpoint)
        exchangeWebSrv.connect()
        attachments_gz = exchangeWebSrv.get_dmarc_report_gz(DMARCServiceConfig.start_datetime) 
        return attachments_gz
    except Exception as exception: 
        ExceptlogClient.log_except(exception)
        

def init_thread(srv_max_worker,attachments_gz):
    try:    
        with concurrent.futures.ThreadPoolExecutor(max_workers=srv_max_worker) as executor:
            for attachment_gz in attachments_gz:
                executor.submit(exec_thread,attachment_gz)
    except Exception as exception:
        ExceptlogClient.log_except(exception)

def exec_thread(attachment_gz):
    try:
        result = Utility.decompress_gz_to_byte(attachment_gz.content)
        if(result is None):
            sys.exit()
        result = Utility.byte_to_xml(result)
        dmarcXML = DMARCReport()
        dmarcXML.parse_dmarc_xml(result)
        dmarcXML.build_leef_v1_from_dmarc_report()
        for leef_v1_msg in dmarcXML.leef_v1_dmarc_report:
            SyslogClient.log_info_msg(leef_v1_msg) 
    except Exception as exception:
        ExceptlogClient.log_except(exception)

if __name__ == "__main__":
    main()