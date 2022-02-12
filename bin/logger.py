import logging
import logging.handlers
import socket
import traceback

class SyslogClient:
    _syslog_logger = None
    _hostname = socket.gethostname()
    _application_name = "BH-DMARC2Syslog"
    _logger_name = "syslog"
    _datefmt="%Y-%m-%dT%H:%M:%S%z"
    _log_format = '%(asctime)s '+ _hostname +' ' + _application_name + ' %(message)s'

    @staticmethod
    def initiate (syslog_server,syslog_port):
        handler = logging.handlers.SysLogHandler(address = (syslog_server,syslog_port))#,facility=1)
        handler.formatter = logging.Formatter(SyslogClient._log_format, datefmt = SyslogClient._datefmt)
        
        SyslogClient._syslog_logger = logging.getLogger(name = SyslogClient._logger_name)
        SyslogClient._syslog_logger.setLevel(logging.INFO)
        SyslogClient._syslog_logger.addHandler(handler)
        
    @staticmethod
    def log_info_msg(msg):
        SyslogClient._syslog_logger.info(msg)

class ExceptlogClient:
    _Log_Format = ('[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')
    _debug_log_enable = False
    _error_log_enable = True
    _error_log_path = ""
    _file_logger = None
    _logger_name = "except"
    _datefmt="%Y-%m-%dT%H:%M:%S%z"

    @staticmethod
    def initiate(error_log_path,error_log_enable,debug_log_enable): 
        ExceptlogClient._error_log_enable = error_log_enable
        ExceptlogClient._error_log_path = error_log_path
        ExceptlogClient._debug_log_enable = debug_log_enable
    
        handler = logging.FileHandler(ExceptlogClient._error_log_path)
        handler.formatter = logging.Formatter(ExceptlogClient._Log_Format, datefmt = ExceptlogClient._datefmt)

        ExceptlogClient._file_logger = logging.getLogger(name = ExceptlogClient._logger_name)
        ExceptlogClient._file_logger.setLevel(logging.ERROR)
        ExceptlogClient._file_logger.addHandler(handler)

    @staticmethod
    def log_except(exception):
        if(ExceptlogClient._error_log_enable):
            ExceptlogClient._file_logger.error(exception)
        if(ExceptlogClient._debug_log_enable):
            ExceptlogClient._file_logger.exception(traceback.format_exc())
