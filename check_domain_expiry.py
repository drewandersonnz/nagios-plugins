#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:52:29 2016

@author: Drew Anderson www.drewanderson.org
"""
import argparse
import datetime
import dateutil.parser
import sys

from subprocess import check_output

EXITOK = 0
EXITWARN = 1
EXITCRIT = 2
EXITUNKNOWN = 3

warning = 7
critical = 2

args = argparse.ArgumentParser()
args.add_argument("domain", help="domain to check")
args = args.parse_args()

def check_date(domain, date):
    if date:
        today = datetime.datetime.now(datetime.timezone.utc)
        parsed = dateutil.parser.parse(date).replace(tzinfo=datetime.timezone.utc)

        if parsed:

            diff = parsed - today
            diff = diff.days

            if diff < critical:
                print("CRITICAL: %s expires in %d days (%s)" % (domain, diff, date))
                sys.exit(EXITCRIT)

            if diff < warning:
                print("WARNING: %s expires in %d days (%s)" % (domain, diff, date))
                sys.exit(EXITWARN)

            print("OK: %s expires in %d days (%s)" % (domain, diff, date))
            sys.exit(EXITOK)

results = check_output(['whois', args.domain]).decode("utf-8")

output = {}

for line in results.splitlines():
    if line.find(":") != -1:
        key,value = line.split(':',1)
        output[key.strip()] = value.strip()

keys = [
    'domain_datebilleduntil',
    'Expiry date',
    'Expiration Date',
    'Registrar Registration Expiration Date',
    'Registry Expiry Date',
]

for key in keys:
    value = output.get(key, None)
    if value:
        check_date(args.domain, value)


# cannot find date
print("UNKNOWN: Cannot find expiry date for: %s" % args.domain)
# Use the below to discover what keys should be used for your expiry
#print(output)
sys.exit(EXITUNKNOWN)
