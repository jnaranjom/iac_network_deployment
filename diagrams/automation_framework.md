```mermaid
flowchart TB
    A[(MongoDB)]
    B[[FastAPI]]
    C(MongoDB Cloud Atlas)
    D(Ansible)
    E[[Network Infrastructure]]
    F[ENGINEER]
    subgraph BACKEND - SoT
        B --> A
    end
    subgraph FRONTEND
        F --> D
        F --> C
        C --> A
    end
    F --> FRONTEND
    subgraph AUTOMATION DEPLOYMENT
        D --> B
        D --> E
    end
```
