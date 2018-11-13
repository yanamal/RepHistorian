from stackapi import StackAPI
import ndjson
import APIkey

SITE = StackAPI('stackoverflow', key=APIkey.key)
SITE.max_pages = 300

rep = SITE.fetch('/users/1679187/reputation-history') # Some high-level user (past biggest privilege threshold)

for field in rep:
    if field != 'items':
        print field, rep[field]

with open('sample.json', 'w') as outfile:
    ndjson.dump(rep['items'], outfile)