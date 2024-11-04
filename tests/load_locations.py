import csv
import json
import random

csv_file_path = '/home/netadmin/automation/iac_network_deployment/tests/locations.csv'

with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    locations = [row for row in csv_reader]

output_list = []
for location in locations:
    description = location['name'].upper()
    if location['location_type__name'] not in ['City', 'Country', 'State']:
        zip_code = str(random.randint(10000, 99999))
    else:
        zip_code = ""
    location_obj = {
        'name': location['name'],
        'description': description,
        'address': location['physical_address'],
        'parent': location['parent__name'],
        'location_type': location['location_type__name'],
        'tenant': location['tenant__name'],
        'status': location['status__name'],
        'zip_code': zip_code,
    }
    output_list.append(location_obj)

output_json_path = '/home/netadmin/automation/iac_network_deployment/tests/locations.json'
with open(output_json_path, mode='w') as json_file:
    json.dump(output_list, json_file, indent=4)
