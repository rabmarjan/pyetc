import gspread
# from oauth2client.client import SignedJwtAssertionCredentials
import json
from oauth2client.service_account import ServiceAccountCredentials

json_key = json.load(open('marjan-gsheet-06dbc61bc59c.json'))
scope = ['https://spreadsheets.google.com/feeds']

# credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key['client_email'], json_key['private_key'].encode(), scope)
credentials = ServiceAccountCredentials.from_json_keyfile_name('marjan-gsheet-06dbc61bc59c.json', scope)

gc = gspread.authorize(credentials)
print(gc)
print(gc)
worksheet = gc.open('CSB__Application-Navigation-Page').get_worksheet(1)

list_of_lists = worksheet.get_all_values()
clientlist = []

for row in list_of_lists[1:]:
    description = row[1]
    client = row[2]
    clienttype = row[3]
    applications = row[4]
    applist = [x.strip() for x in applications.split(',')]
    clientlist.append({client: {'type': clienttype, 'description': description, 'applications': applist}})

with open('ClientMap.json', 'w') as jsonFile:
    print(json.dumps(clientlist, indent=4), file=jsonFile)
