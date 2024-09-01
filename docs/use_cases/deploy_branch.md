### Workflow to deploy new branches

## Description

Automation solution to deploy configuration for new branches

## Components

- Nautobot:
    - Job to create:
        - Connections
        - Trunk link
        - L3 link with ISP
        - IP addresses:
            - VLANs
            - Prefixes
        - BGP sessions

- Ansible:
    - Render full device configuration

- Console:
    - Apply configuration to the device

## Workflow

1. Define branch to deploy
2. Define devices to deploy in the branch
3. Run job:
    - Create connection between router and switch (2nd interface on each device)
    - Allocate prefixes for each VLAN (Site VLANs)
    - Create subinterfaces on the edge router
    - Set first IP for each prefix on the corresponding subinterface
    - Set the switch interfaces as trunk (802.1Q Mode=Tagged)
    - Set last set of ports as access ports for the site VLANs
    - Create connection between edge router and ISP (Last interface on the router)
    - Allocate prefix for the ISP connection
    - Set the interfaces IP on the ISP link
    - Allocate ASN to branch
    - Setup BGP session between the edge router and the ISP router

## Output

New devices get set in the proper location, with a dynamically allocated IP assigned and an init configuration set on the device for remote mgmt
