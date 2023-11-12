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
    F1(NET DEPLOY)
    F2(NSOT OPS)
    F3(Data Models)
    D ---> A
    D ---> F
    D ---> B
    B ---> C
    B --- A
    subgraph NSoT
      A --- A1
      A --- A2
      A --- A3
    end
    subgraph VERSION CONTROL
      F --- F1
      F --- F2
      F --- F3
    end
    subgraph NETWORK INFRA
      C
    end
    subgraph DEPLOYMENT
      B
    end

