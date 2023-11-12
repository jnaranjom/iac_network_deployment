## Network Automation Platform

```mermaid
flowchart TB
    A[(Nautobot)]
    A1(Data Models)
    B(Ansible)
    C[[Network Devices]]
    D(((ENGINEER)))
    E(GRAFANA)
    F(GITHUB)
    subgraph PLATFORM
      Components["'IPAM
      DCIM
      DATA MODELS'"]
      A -.- Components
    end
    D -.- B
    D -.- F
    B --- C
    B --- A
    B --- F
    subgraph NETWORK INFRA
      C
    end


