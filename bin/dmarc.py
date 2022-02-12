from lxml import etree

class DMARCReport: 
    _xpath_version = "./version"
    _xpath_metadata_org_name = "./report_metadata/org_name"
    _xpath_metadata_email = "./report_metadata/email"
    _xpath_metadata_extra_contact_info = "./report_metadata/extra_contact_info"
    _xpath_metadata_report_id = "./report_metadata/report_id"
    _xpath_date_range_begin = "./report_metadata/date_range/begin"
    _xpath_date_range_end = "./report_metadata/date_range/end"
    _xpath_policy_published_domian = "./policy_published/domain"
    _xpath_policy_published_adkim = "./policy_published/adkim"
    _xpath_policy_published_aspf = "./policy_published/aspf"
    _xpath_policy_published_p = "./policy_published/p"
    _xpath_policy_published_sp = "./policy_published/sp"
    _xpath_policy_published_pct = "./policy_published/pct"
    _xpath_policy_published_fo = "./policy_published/fo"
    _xpath_record = "./record"
    _xpath_record_row_source_ip = "./row/source_ip"
    _xpath_record_row_count = "./row/count"
    _xpath_record_row_policy_evaluated_disposition = "./row/policy_evaluated/disposition"
    _xpath_record_row_policy_evaluated_dkim = "./row/policy_evaluated/dkim"
    _xpath_record_row_policy_evaluated_spf = "./row/policy_evaluated/spf"
    _xpath_record_identifiers_header_from = "./identifiers/header_from"
    _xpath_record_identifiers_envelope_from = "./identifiers/envelope_from"
    _xpath_record_auth_results_dkim_domain = "./auth_results/dkim/domain"
    _xpath_record_auth_results_dkim_result = "./auth_results/dkim/result"
    _xpath_record_auth_results_dkim_selector = "./auth_results/dkim/selector"
    _xpath_record_auth_results_spf_domain = "./auth_results/spf/domain"
    _xpath_record_auth_results_spf_result = "./auth_results/spf/result"
    _leef_v1_header_dmarc_report ='LEEF:1.0|BH|DMARC2Syslog|1.0|1|'
    _leef_v1_delimiter ="\t"
    _attr_key_dmarc_report_version = "ver="
    _attr_key_dmarc_report_metadata_org_name  = "orgName="
    _attr_key_dmarc_report_metadata_email  = "email="
    _attr_key_dmarc_report_metadata_extra_contact_info  = "extraContactInfo="
    _attr_key_dmarc_report_metadata_report_id  = "reportID="
    _attr_key_dmarc_report_date_range_begin  = "dateRangeBegin="
    _attr_key_dmarc_report_date_range_end  = "dateRangeEnd="
    _attr_key_dmarc_report_policy_published_domian  = "policyPublishedDomain="
    _attr_key_dmarc_report_policy_published_adkim  = "policyPublishedADKIM="
    _attr_key_dmarc_report_policy_published_aspf  = "policyPublishedASPF="
    _attr_key_dmarc_report_policy_published_p  = "policyPublishedP="
    _attr_key_dmarc_report_policy_published_sp  = "policyPublishedSP="
    _attr_key_dmarc_report_policy_published_pct  = "policyPublishedPCT="
    _attr_key_dmarc_report_policy_published_fo  = "policyPublishedFO="
    _attr_key_dmarc_record_row_source_ip  = "RecordRowSourceIP="
    _attr_key_dmarc_record_row_count  = "RecordRowCount="
    _attr_key_dmarc_record_row_policy_evaluated_disposition = "RecordRowPolicyEvaluatedDisposition="
    _attr_key_dmarc_record_row_policy_evaluated_dkim  = "RecordRowPolicyEvaluatedDKIM="
    _attr_key_dmarc_record_row_policy_evaluated_spf  = "RecordRowPolicyEvaluatedSPF="
    _attr_key_dmarc_record_identifiers_header_from  = "RecordIdentifiersHeaderFrom="
    _attr_key_dmarc_record_identifiers_envelope_from  = "RecordIdentifiersEnvelopeFrom="
    _attr_key_dmarc_record_auth_results_dkim_domain  = "RecordAuthResultsDKIMDomain="
    _attr_key_dmarc_record_auth_results_dkim_result  = "RecordAuthResultsDKIMResult="
    _attr_key_dmarc_record_auth_results_dkim_selector  = "RecordAuthResultsDKIMSelector="
    _attr_key_dmarc_record_auth_results_spf_domain  = "RecordAuthResultsSPFDomain="
    _attr_key_dmarc_record_auth_results_spf_result  = "RecordAuthResultsSPFResult="

    def __init__(self):
        self.version = "none"
        self.metadata_org_name = "none"
        self.metadata_email = "none"
        self.metadata_extra_contact_info = "none"
        self.metadata_report_id = "none"
        self.date_range_begin = "none"
        self.date_range_end = "none"
        self.policy_published_domian = "none" 
        self.policy_published_adkim = "none"
        self.policy_published_aspf = "none"
        self.policy_published_fo = "none"
        self.policy_published_p = "none"
        self.policy_published_sp = "none"
        self.policy_published_pct = "none"
        self.records = []
        self.leef_v1_header_dmarc_report = "none"
        self.leef_v1_dmarc_report_records = []
        self.leef_v1_dmarc_report = []

    def parse_dmarc_xml(self,xml):
        self.__parse_dmarc_xml_header(xml)
        self.__parse_dmarc_xml_policy_published(xml)
        self.__parse_dmarc_xml_record(xml)
            
        
    def __parse_dmarc_xml_header(self,xml):   
        self.version = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_version)
        self.org_name = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_metadata_org_name)
        self.email = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_metadata_email)
        self.date_range_begin = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_date_range_begin)
        self.date_range_end = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_date_range_end)
        self.metadata_extra_contact_info = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_metadata_extra_contact_info)
        self.metadata_report_id = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_metadata_report_id)

    def __parse_dmarc_xml_policy_published(self,xml):       
        self.policy_published_domian = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_policy_published_domian)
        self.policy_published_adkim = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_policy_published_adkim)
        self.policy_published_aspf = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_policy_published_aspf)   
        self.policy_published_fo = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_policy_published_fo)
        self.policy_published_p = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_policy_published_p)
        self.policy_published_pct = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_policy_published_pct)
        self.policy_published_sp = self.__parse_dmarc_report_xml_value(xml,DMARCReport._xpath_policy_published_sp)

    def __parse_dmarc_report_xml_value(self,element,_xpath):
        try:
            value = element.find(_xpath).text
            if(value is None):
                return "none"
            else:
                return value
        except:
            return "none"

    def __parse_dmarc_xml_record(self,xml):        
        records = xml.findall(DMARCReport._xpath_record)
        for record in records:
            new_record = DMARCRecord()
            new_record.record_row_source_ip = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_row_source_ip)
            new_record.record_row_count = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_row_count)
            new_record.record_row_policy_evaluated_spf = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_row_policy_evaluated_spf)
            new_record.record_row_policy_evaluated_dkim = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_row_policy_evaluated_dkim)
            new_record.record_row_policy_evaluated_disposition = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_row_policy_evaluated_disposition)
            new_record.record_auth_results_dkim_domain = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_auth_results_dkim_domain)
            new_record.record_auth_results_dkim_result = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_auth_results_dkim_result)
            new_record.record_auth_results_dkim_selector = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_auth_results_dkim_selector)
            new_record.record_auth_results_spf_domain = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_auth_results_spf_domain)
            new_record.record_auth_results_spf_result = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_auth_results_spf_result)
            new_record.record_identifiers_header_from = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_identifiers_header_from)
            new_record.record_identifiers_envelope_from = self.__parse_dmarc_report_xml_value(record,DMARCReport._xpath_record_identifiers_envelope_from)
            self.records.append(new_record)
    
    def build_leef_v1_from_dmarc_report(self):
        self.__build_leef_v1_header_dmarc_report()
        self.__build_leef_v1_dmarc_records()
        self.__build_leef_v1_dmarc_report()
              
    def __build_leef_v1_header_dmarc_report(self):  
        self.leef_v1_header_dmarc_report = DMARCReport._leef_v1_header_dmarc_report
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_version + self.version + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_metadata_org_name + self.org_name + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_metadata_email + self.email + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_metadata_extra_contact_info + self.metadata_extra_contact_info + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_metadata_report_id + self.metadata_report_id + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_date_range_begin + self.date_range_begin + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_date_range_end + self.date_range_end + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_policy_published_domian + self.policy_published_domian + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_policy_published_adkim + self.policy_published_adkim + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_policy_published_aspf + self.policy_published_aspf + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_policy_published_p + self.policy_published_p + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_policy_published_sp + self.policy_published_sp + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_policy_published_pct + self.policy_published_pct + DMARCReport._leef_v1_delimiter
        self.leef_v1_header_dmarc_report = self.leef_v1_header_dmarc_report + DMARCReport._attr_key_dmarc_report_policy_published_fo + self.policy_published_fo
    
    def __build_leef_v1_dmarc_records(self):
        for record in self.records:
            tmp = ""
            tmp = DMARCReport._attr_key_dmarc_record_row_source_ip + record.record_row_source_ip + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_row_count + record.record_row_count + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_row_policy_evaluated_disposition + record.record_row_policy_evaluated_disposition + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_row_policy_evaluated_dkim + record.record_row_policy_evaluated_dkim + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_row_policy_evaluated_spf + record.record_row_policy_evaluated_spf + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_identifiers_header_from + record.record_identifiers_header_from + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_identifiers_envelope_from + record.record_identifiers_envelope_from + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_auth_results_dkim_domain + record.record_auth_results_dkim_domain + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_auth_results_dkim_result + record.record_auth_results_dkim_result + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_auth_results_dkim_selector + record.record_auth_results_dkim_selector + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_auth_results_spf_domain + record.record_auth_results_spf_domain + DMARCReport._leef_v1_delimiter
            tmp = tmp + DMARCReport._attr_key_dmarc_record_auth_results_spf_result + record.record_auth_results_spf_result
            self.leef_v1_dmarc_report_records.append(tmp)

    def __build_leef_v1_dmarc_report(self):
        for record in self.leef_v1_dmarc_report_records:
            self.leef_v1_dmarc_report.append( self.leef_v1_header_dmarc_report  + DMARCReport._leef_v1_delimiter + record )

        




class DMARCRecord:
    def __init__(self):
        self.record_row_source_ip = None
        self.record_row_count = None
        self.record_row_policy_evaluated_disposition = None
        self.record_row_policy_evaluated_dkim = None
        self.record_row_policy_evaluated_spf = None
        self.record_identifiers_header_from = None
        self.record_identifiers_envelope_from = None
        self.record_auth_results_dkim_domain = None
        self.record_auth_results_dkim_result = None
        self.record_auth_results_dkim_selector = None
        self.record_auth_results_spf_domain = None
        self.record_auth_results_spf_result = None
        