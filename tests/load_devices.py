import csv
import json

csv_file_path = '/home/netadmin/automation/iac_network_deployment/tests/devices.csv'

with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    devices = [row for row in csv_reader]

output_list = []
for device in devices:
    if 'rtr' in device['name']:
        function = 'router'
    else:
        function = 'switch'
    device_obj = {
        'device_type': device['device_type__model'],
        'description': f"{device['role__name'].split(':')[0].capitalize()} {function.capitalize()}",
        'location': device['location__name'],
        'manufacturer': device['device_type__manufacturer__name'],
        'name': device['name'],
        'platform': device['platform__name'],
        'role': device['role__name'],
        'serial_number': device['serial'],
        'status': device['status__name'],
        'tenant': device['tenant__name'],
    }
    output_list.append(device_obj)

    output_json_path = '/home/netadmin/automation/iac_network_deployment/tests/devices.json'
    with open(output_json_path, mode='w') as json_file:
        json.dump(output_list, json_file, indent=4)
