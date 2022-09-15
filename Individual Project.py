# https://stackoverflow.com/questions/54994426/online-banking-web-scraping
# https://stackoverflow.com/questions/69984767/cant-scrape-discover-bank-page
# https://stackoverflow.com/questions/11892729/how-to-log-in-to-a-website-using-pythons-requests-module/17633072

# The biggest issue I have found is that all my bank/credit card accounts use 17 step verification.
# That's an exaggeration but my point still stands.
# With multi-step verification and me potentially locking myself out of my accounts, I adapted the code for the
# time being. Instead of going straight to my account, the code will read over pdf bank/credit card statements
# and compile/export everything that way.


import re
import pdfplumber
import pandas as pd
from collections import namedtuple

entry_re = re.compile(r'Date (\d+/\d+) \(.*?Description (.*)(.*?Deposits/Additions)(.*?Withdrawals/Subtractions)')
Row = namedtuple('Row','Date Description Deposits_Additions Withdrawals_Subtractions Ending_Daily_Balance')

def dr_cr(last_pos,row):
    return 'Deposits/Additions' if last_pos[row] < 100 else 'Withdrawals/Subtractions'

def numbify(num):
    return float(num.replace('$',''))

def page_to_df(lines, last_pos, id_info=('','','','','')):
    entry, date, description, deposits, withdrawal = id_info
    rows = []

    for idx, line in enumerate(lines.split('\n')):
        if line.startswith('Date'):
            entry = entry_re.search(line)
            date = entry.group(1)
            description = entry.group(2)
            deposits = entry.group(3)
            withdrawal = entry.group(4)
        if '\d+/\d+ [A-Z]' in line:
            *dat, descrip, amt = line.split()
            if dr_cr(last_pos, idx) == 'Deposit':
              deposit, withdraw = numbify(amt), 0
            else:
                deposit, withdraw = numbify(amt), 0
            rows.append(Row(date, description, deposits, withdrawal))
        df = pd.DataFrame(rows)
    return df, (entry,date,description,description)

df = pd.DataFrame()
id_info = ('','','','','')
with pdfplumber.open('WellsFargo.pdf') as pdf:
    for page in pdf.pages:
        lines = page.extract_text(x_tolerance=2, y_tolerance=0)
        words = page.extract_words(x_tolerance=2, y_tolerance=0)
        rows_dict = {rows_dict.get(word['bottom']): word['x1'] for word in words}
        new_df, id_info = page_to_df(lines, last_pos, id_info)
        df = pd.concat([df, new_df]).reset_index(drop=True)