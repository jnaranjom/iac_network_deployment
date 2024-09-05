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


## Requirements to deploy a branch:

1. Create Site
2. Create ASN for site
3. Create new prefixes for the site
    - Associate VLAN to prefix
4. Associate VLANs to the site
5. Create new devices in the site:
    - Define role, location, status
6. Run the `SET MGMT IP` Job to setup management on the device im Nautobot
7. Run the `Deploy Small Branch` Job to setup the branch attributes
8. Deploy init config to the devices `pb_init_config.yml`
9. Deploy full config to the devices once these are online `pb_render_config.yml`

## Remove branch configuration from devices

1. Disconnect cable between branch router and ISP router
2. Disconnect cable between branch router and switch
3. Restore interface status to `Planned`
4. Remove IP addresses from Router and ISP router
5. Remove mode on switch interfaces
6. Delete `wan:p2p` addresses
7. Delete Default Gateway IPs from site prefixes
8. Delete BGP peering for the site
9. Delete routing instance for the router
