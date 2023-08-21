#!/usr/bin/env python

import csv

csv_path = 'dhcp_config/hosts.csv'
dhcp_hosts = []

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        dhcp_hosts.append(row)

print(json.dumps(dhcp_hosts))
