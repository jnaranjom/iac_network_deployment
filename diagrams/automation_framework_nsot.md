## Network Automation Platform

```mermaid
flowchart TB
    A[(Nautobot)]
    A1["Data Models
    Templates
    Playbooks"]
    B(Ansible)
    C[[Network Devices]]
    D(((ENGINEER)))
    E(GRAFANA)
    F(GITHUB)
    subgraph OBSERVABILITY
      direction LR
      E
    end
    subgraph NSoT [NSoT]
      Components["IPAM
      DCIM"]
      A -.- Components
    end
    subgraph VERSION CONTROL
      F -.- A1
    end
    D -.- B
    D -.- F
    B --- A
    B --- F
    A -.- A1
    subgraph INFRA[NETWORK INFRA]
      C
    end
    B --- C
    D -.- E
    style INFRA fill:#bbf,stroke:blue,stroke-width:2px
    style D fill:crimson
    linkStyle 7 stroke:blue



