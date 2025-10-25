import re

log_text = """
2023-01-15 12:34:56 INFO [server@192.168.1.1]: Starting service
ERROR: Couldn't connect to database at host 10.0.0.1
2023-01-15 12:35:01 WARNING User ADMINISTRATOR logged in from IP 8.8.8.8
User support@example.com requested access denied
2023-01-15 12:35:05 CRITICAL SERVER IS DOWN
"""

ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
timestamp_pattern = r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b'
uppercase_words_pattern = r'\b[A-Z]+\b'
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'

ipv4_addresses = re.findall(ipv4_pattern, log_text)
print("IPv4 addresses:", ipv4_addresses)

timestamps = re.findall(timestamp_pattern, log_text)
print("Timestamps:", timestamps)

uppercase_words = re.findall(uppercase_words_pattern, log_text)
print("Uppercase words:", uppercase_words)

protected_log = re.sub(email_pattern, '[EMAIL PROTECTED]', log_text)

print("Log text after email protection:\n", protected_log)
