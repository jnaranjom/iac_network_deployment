## Network Automation Platform

```mermaid
flowchart TB
    A[(Nautobot)]
    B(Ansible)
    C[[Network Devices]]
    D(((ENGINEER)))
    E(GRAFANA)
    F(GITHUB)
    F1(NETWORK_DEPLOYMENT REPO)
    F2(NSOT OPERATIONS REPO)
    subgraph VERSION CONTROL
      F1 --->F
      F2 --- F
    end

