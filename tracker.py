import re
import xml.etree.ElementTree as ET

def analyze_momo():
    try:
        tree = ET.parse('sms_data.xml')
        root = tree.getroot()
        received, sent = 0, 0

        for sms in root.findall('sms'):
            body = sms.get('body', '')
            # Regex: finds numbers (with or without commas) before 'RWF'
            match = re.search(r'([\d,]+)\s*RWF', body)
            if match:
                amount = int(match.group(1).replace(',', ''))
                if 'received' in body.lower() or 'deposit' in body.lower():
                    received += amount
                elif 'payment' in body.lower() or 'transferred' in body.lower():
                    sent += amount

        print(f'Total Received: {received} RWF')
        print(f'Total Sent: {sent} RWF')
        print(f'Balance: {received - sent} RWF')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    analyze_momo()
