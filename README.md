# DMARC2Syslog
Python script to read DMARC reports from a mailbox and covert it to syslog messages for the purpose of collecting the reports in a SIEM solution.

Supported mailbox access:
  1. EWS (Exchange Web Serivce)

Supported Syslog messages foramts:
  1. LEEF v1

Requirements:
  1. Python 3.10
  2. exchangelib 4.6.2 : installation command -> pip install exchangelib 

How to use it:
  1. Provide the requried configuration in the confgiruation file "config.ini" 
  2. create a task scheduler or cron job to run the script file "start.py", as an example each 10 mintues.
  3. The script manages the last time it checked for rep
