import gzip
import traceback
from lxml import etree
from logger import ExceptlogClient

class Utility:
    @staticmethod
    def decompress_gz_to_byte(compressed_content): 
        try:
            tmp = gzip.decompress(compressed_content)
            return tmp
        except Exception as exception: 
            ExceptlogClient.log_except(exception)
            return None
    
    @staticmethod
    def byte_to_xml(byte_content):
        xx = etree.XML(byte_content)
        return xx

    @staticmethod
    def xml_to_string(xml):
        return etree.tostring(xml, encoding='utf8').decode('utf8')

  

