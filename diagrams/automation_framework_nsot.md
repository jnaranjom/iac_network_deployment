## Network Automation Platform

```mermaid
flowchart TB
    D(((ENGINEER)))
    A[(Nautobot)]
    A1["Data Models
    Templates
    Playbooks"]
    B(Ansible)
    C[[Network Devices]]
    E(GRAFANA)
    F(GITHUB)
    subgraph DEPLOY[DEPLOYMENT]
      B
    end
    subgraph OB[OBSERVABILITY]
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
    D -.- DEPLOY
    D -.- OB
    DEPLOY --- NSoT
    OB --- NSoT
    A -.- A1
    subgraph INFRA[NETWORK INFRASTRUCTURE]
      C
    end
    B ----- INFRA
    style INFRA fill:#bbf,stroke:blue
    linkStyle 7 stroke:blue



