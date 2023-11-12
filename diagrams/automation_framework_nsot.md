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
    subgraph OB[OBSERVABILITY]
      direction LR
      E
    end
    subgraph NSoT [NSoT]
      Components["IPAM
      DCIM"]
      A -.- Components
    end
    subgraph GITHUB[VERSION CONTROL]
      F -.- A1
    end
    D -.- NSoT
    D -.- GITHUB
    B --- NSoT
    B --- OB
    A -.- A1
    subgraph INFRA[NETWORK INFRASTRUCTURE]
      C
    end
    B ----- INFRA
    D -.- E
    style INFRA fill:#bbf,stroke:blue
    linkStyle 7 stroke:blue



