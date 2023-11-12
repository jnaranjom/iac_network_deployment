## Network Automation Platform

```mermaid
flowchart TB
    A[(Nautobot)]
    A1(IPAM)
    A2(DCIM)
    A3(DATA MODELS)
    B(Ansible)
    C[[Network Devices]]
    D(((ENGINEER)))
    E(GRAFANA)
    F(GITHUB)
    F1(NETWORK_DEPLOYMENT REPO)
    F2(NSOT OPERATIONS REPO)
    D ---> A
    D ---> F
    subgraph NETWORK SOURCE OF TRUTH
      A --- A1
      A --- A2
      A --- A3
    end
    subgraph VERSION CONTROL
      F --- F1
      F --- F2
    end
    subgraph NETWORK INFRASTRUCTURE
      C
    end
    subgraph AUTOMATION DEPLOYMENT
      B
    end

