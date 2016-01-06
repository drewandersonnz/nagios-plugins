#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Web Jan  6 18:45:29 2016

@author: Drew Anderson www.drewanderson.org
"""

import argparse

args = argparse.ArgumentParser()
args.add_argument("domain", help="domain to check")
args = args.parse_args()

print("""

define service {
    host_name               domains.fakehost
    service_description     domain %s
    check_command           check_domain_expiry!%s
    use                     generic-service
    notification_interval   0 ; set > 0 if you want to be renotified
}
""" % (args.domain, args.domain))
