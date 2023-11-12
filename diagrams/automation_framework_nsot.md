## Network Automation Platform

```mermaid
flowchart TB
    A[(Nautobot)]
    A1(IPAM)
    A2(DCIM)
    A3(Data Models)
    B(Ansible)
    C[[Network Devices]]
    D(((ENGINEER)))
    E(GRAFANA)
    F(GITHUB)
    subgraph NSoT
      A --- A1
      A --- A2
      A --- A3
      A --- F 
    end
    subgraph DEPLOYMENT
      B
    end
    D -.- B
    D -.- F
    B --- C
    B --- A
    subgraph NETWORK INFRA
      C
    end


