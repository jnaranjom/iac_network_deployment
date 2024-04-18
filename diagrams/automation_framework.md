## Network Automation Platform

```mermaid
flowchart TB
    A[(MongoDB Cloud Atlas)]
    B[[FastAPI]]
    D(Ansible)
    E[[Network Devices]]
    F(((ENGINEER)))
    H(JENKINS)
    I(GITHUB)
    subgraph BACKEND - SoT
        B --> A
    end
    F --> H
    subgraph AUTOMATION DEPLOYMENT
        D --> B
        H --> I
        H --> D
    end
    subgraph INFRASTRUCTURE
        D --> E
    end
```
