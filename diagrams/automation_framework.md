## Network Automation Platform

```mermaid
flowchart TB
    A[(MongoDB Cloud Atlas)]
    B[[FastAPI]]
    C(MongoDB Compass App)
    D(Ansible)
    E[[Network Infrastructure]]
    F(((ENGINEER)))
    G(GRAFANA)
    subgraph BACKEND - SoT
        B --> A
    end
    subgraph FRONTEND
        C --> A
        D --> B
        G --> B
    end
    F --> C
    F --> D
    subgraph AUTOMATION DEPLOYMENT
        D --> E
    end

```
