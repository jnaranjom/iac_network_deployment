```mermaid
flowchart TB
    A[(MongoDB SoT)]
    B[[FastAPI]]
    C(MongoDB Cloud Atlas)
    D(Ansible)
    E[[Network Infrastructure]]
    F[ENGINEER]
    subgraph BACK END
        B --> A
    end
    subgraph FRONT END
        F --> D
        F --> C
        C --> A
    end
    subgraph AUTOMATION DEPLOYMENT
        D --> B
        D --> E
    end
```
