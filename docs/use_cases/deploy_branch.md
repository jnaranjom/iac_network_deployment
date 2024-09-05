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
    - LAN:
        - Create connection between router and switch (2nd interface on each device) <- Done
        - Create connection between edge router and ISP (Last interface on the router) <- Done
        - Create subinterfaces on the edge router for the LAN side <- Done
        - Allocate prefixes for each VLAN (Site VLANs) <- Done
        - Set first IP for each prefix on the corresponding subinterface <- Done
        - Set last set of ports as access ports for the site VLANs <- Done
        - Set the switch uplink interface as trunk (802.1Q Mode=Tagged) <- Done

    - WAN:
        - Allocate prefix for the ISP connection <- Done
        - Set the interfaces IP on the ISP link <- Done
        - Setup BGP session between the edge router and the ISP router <- Done

## Output

New devices get set in the proper location, with a dynamically allocated IP assigned and an init configuration set on the device for remote mgmt
