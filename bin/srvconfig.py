import configparser
from operator import truediv
import os
import sys
from logger import ExceptlogClient
from datetime import datetime


class DMARCServiceConfig:
    config = None
    _config_file_path = os.path.join(sys.path[0], "config", "config.ini") 
    start_datetime = ""
    ews_username = ""
    ews_password = ""
    ews_email = ""
    ews_service_endpoint = ""
    ews_disable_https_cert_verify = False 
    syslog_server = ""
    syslog_port = ""
    syslog_application = ""
    srv_max_worker = ""
    mailbox_type = ""
    _mailbox_type_ews = "ews"
    error_log_path = os.path.join(sys.path[0], "log", "error.log") 
    error_log_enable = True
    debug_log_enable = False
    
    
    @staticmethod
    def init_config():
        try:
            DMARCServiceConfig.config = configparser.ConfigParser()
            DMARCServiceConfig.config.read(DMARCServiceConfig._config_file_path)
            DMARCServiceConfig.start_datetime = DMARCServiceConfig.config['CONFIG']['start_datetime']
            DMARCServiceConfig.srv_max_worker = int(DMARCServiceConfig.config['CONFIG']['srv_max_worker'])
            DMARCServiceConfig.syslog_server = DMARCServiceConfig.config['SYSLOG']['syslog_server']
            DMARCServiceConfig.syslog_port = int(DMARCServiceConfig.config['SYSLOG']['syslog_port'])
            DMARCServiceConfig.mailbox_type = DMARCServiceConfig.config['CONFIG']['mailbox_type']
            
            if (DMARCServiceConfig.mailbox_type == DMARCServiceConfig._mailbox_type_ews):
                DMARCServiceConfig.ews_username = DMARCServiceConfig.config['EWS']['ews_username']
                DMARCServiceConfig.ews_password = DMARCServiceConfig.config['EWS']['ews_password']
                DMARCServiceConfig.ews_email = DMARCServiceConfig.config['EWS']['ews_email']
                DMARCServiceConfig.ews_service_endpoint = DMARCServiceConfig.config['EWS']['ews_service_endpoint']
                
                if (DMARCServiceConfig.config.has_option('EWS','ews_disable_https_cert_verify')):
                    DMARCServiceConfig.ews_disable_https_cert_verify = eval(DMARCServiceConfig.config['EWS']['ews_disable_https_cert_verify'])
                    
            
            DMARCServiceConfig.error_log_enable = eval(DMARCServiceConfig.config['CONFIG']['error_log_enable'])
            DMARCServiceConfig.debug_log_enable = eval(DMARCServiceConfig.config['CONFIG']['debug_log_enable'])
        
        except Exception as exception:
            ExceptlogClient.initiate(DMARCServiceConfig.error_log_path,DMARCServiceConfig.error_log_enable,True)
            ExceptlogClient.log_except(exception)



    @staticmethod
    def update_config_start_datetime():
        now = datetime.now().strftime("%Y-%m-%d-%H:%M")
        DMARCServiceConfig.config.set("CONFIG","start_datetime",now)
        with open(DMARCServiceConfig._config_file_path, "w") as configfile:
            DMARCServiceConfig.config.write(configfile)


