## Network Automation Platform

```mermaid
flowchart TB
    A[(MongoDB Cloud Atlas)]
    B[[FastAPI]]
    D(Ansible)
    E[[Network Devices]]
    F(((ENGINEER)))
    G(GRAFANA)
    H(JENKINS)
    I(GITHUB)
    subgraph BACKEND - SoT
        B --> A
    end
    subgraph FRONTEND
        G --> B
    end
    F --> H
    F --> G
    subgraph AUTOMATION DEPLOYMENT
        D --> B
        D --> I
        H --> I
        H --> D
    end
    subgraph INFRASTRUCTURE
        D --> E
    end
```
