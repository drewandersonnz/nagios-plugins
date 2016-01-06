#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Web Jan  6 18:45:29 2016

@author: Drew Anderson www.drewanderson.org
"""

import argparse

args = argparse.ArgumentParser()
args.add_argument("domain", help="domain to check")
args.add_argument("--ip", help="IP domain must report as", default=None)
args = args.parse_args()

check_command = "check_domain_expiry"
print("""define service {
    host_name               domains.fakehost
    service_description     %(domain)s domain expiry
    check_command           %(check_command)s!%(domain)s
    use                     generic-service
    notification_interval   0 ; set > 0 if you want to be renotified
}
""" % dict(domain=args.domain, check_command=check_command))

check_command = "check_domain_response_ip"
if args.ip:
    check_command = "check_domain_response_ip_match"

print("""define service {
    host_name               domains.fakehost
    service_description     %(domain)s domain ip
    check_command           %(check_command)s!%(domain)s
    use                     generic-service
    notification_interval   0 ; set > 0 if you want to be renotified
}
""" % dict(domain=args.domain, check_command=check_command))
print("""define service {
    host_name               domains.fakehost
    service_description     %(domain)s domain ip www
    check_command           %(check_command)s!www%(domain)s
    use                     generic-service
    notification_interval   0 ; set > 0 if you want to be renotified
}
""" % dict(domain=args.domain, check_command=check_command))

print()
