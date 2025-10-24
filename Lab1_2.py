import re

# Входной многострочный текст
log_text = """
2023-01-15 12:34:56 INFO [server@192.168.1.1]: Starting service
ERROR: Couldn't connect to database at host 10.0.0.1
2023-01-15 12:35:01 WARNING User ADMINISTRATOR logged in from IP 8.8.8.8
User support@example.com requested access denied
2023-01-15 12:35:05 CRITICAL SERVER IS DOWN
"""

# Регулярные выражения
ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
timestamp_pattern = r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b'
uppercase_words_pattern = r'\b[A-Z]+\b'
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'

# 1. Находим все IPv4 адреса
ipv4_addresses = re.findall(ipv4_pattern, log_text)
print("IPv4 addresses:", ipv4_addresses)

# 2. Находим все временные метки в формате YYYY-MM-DD HH:MM:SS
timestamps = re.findall(timestamp_pattern, log_text)
print("Timestamps:", timestamps)

# 3. Находим все слова, написанные в верхнем регистре
uppercase_words = re.findall(uppercase_words_pattern, log_text)
print("Uppercase words:", uppercase_words)

# 4. Заменяем все найденные email-адреса на [EMAIL PROTECTED]
protected_log = re.sub(email_pattern, '[EMAIL PROTECTED]', log_text)
print("Log text after email protection:\n", protected_log)