from stackapi import StackAPI
import json

SITE = StackAPI('stackoverflow')
SITE.max_pages = 300

print SITE.page_size, SITE.max_pages


rep = SITE.fetch('/users/1679187/reputation-history') # Some high-level user (past biggest privilege threshold)

with open('sample.json', 'w') as outfile:
    json.dump(rep, outfile)