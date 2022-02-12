from exchangelib import DELEGATE, Account, Credentials,Configuration,NTLM,EWSDateTime

class ExchangeWebSrv:        
    def __init__(self, username,password,email,service_endpoint): 
        self.username = username
        self.password = password
        self.email = email
        self.server = ""
        self.auto_discover = False
        self.access_type = DELEGATE
        self.auth_type = NTLM
        self.service_endpoint = service_endpoint
        self.credentials = Credentials(username = self.username, password = self.password)
        self.configuration = Configuration(service_endpoint = self.service_endpoint, credentials=self.credentials, auth_type=self.auth_type)
        

    def connect(self):
        self.account = Account(primary_smtp_address= self.email, config=self.configuration, autodiscover=self.auto_discover, access_type=self.access_type)
    
    def __get_email_inbox_recieved_datetime__gt(self,date_time_string):
        date_time_filter = self.__return_datetime_filter(date_time_string)
        emails = self.account.inbox.filter(datetime_received__gt=date_time_filter)
        return emails
    
    def __return_datetime_filter(self,date_time_string): 
        return EWSDateTime.from_string(date_time_string)

    def __get_email_inbox_folder_path(self,folder_path):
        emails = self.account.inbox.glob(folder_path)
        return emails

    def __get_dmarc_email_attachment_gz(self,email):
        if len(email.attachments) > 0:
          return email.attachments[0]
        else:
         return None

    def get_dmarc_report_gz(self,date_time_string):
        dmarc_report_gz = []
        emails = self.__get_email_inbox_recieved_datetime__gt(date_time_string)
        for email in emails:
            tmp_dmarc_email_attachment_gz = self.__get_dmarc_email_attachment_gz(email)
            if (tmp_dmarc_email_attachment_gz != None):
                dmarc_report_gz.append(tmp_dmarc_email_attachment_gz)
        return dmarc_report_gz
    
