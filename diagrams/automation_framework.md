## Network Automation Platform

```mermaid
flowchart TB
    A[(MongoDB Cloud Atlas)]
    B[[FastAPI]]
    C(MongoDB Compass App)
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
        C --> A
        
        G --> B
    end
    F --> C
    F --> H
    F --> G
    subgraph AUTOMATION DEPLOYMENT
        D --> B
        H --> I
        H --> D
    end
    subgraph INFRASTRUCTURE
        D --> E
    end
```
