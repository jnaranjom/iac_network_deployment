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
    subgraph OBSERVABILITY
      direction LR
      D --- E
    end
    subgraph NSoT
      Components["IPAM
      DCIM"]
      A -.- Components
    end
    subgraph VERSION CONTROL
      F
    end
    D -.- B
    D -.- F
    B --- A
    B --- F
    A -.- A1
    F -.- A1
    subgraph NETWORK INFRA
      C
    end
    B --- C


