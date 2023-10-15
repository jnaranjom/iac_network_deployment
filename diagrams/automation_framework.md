```mermaid
flowchart LR
    A[(MongoDB)]
    B[[FastAPI]]
    C(MongoDB Cloud Atlas)
    subgraph BACKEND
        A <--> B
    end
    subgraph USER INTERACTION
        C --> A
    end
```
