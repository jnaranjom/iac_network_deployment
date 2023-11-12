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
    subgraph NSoT
      Components["'IPAM
      DCIM
      DATA MODELS'"]
      A -.- Components
    end
    subgraph VERSION CONTROL
      F
    end
    D -.- B
    D -.- F
    B --- NSoT
    B --- VERSION CONTROL
    subgraph NETWORK INFRA
      C
    end


