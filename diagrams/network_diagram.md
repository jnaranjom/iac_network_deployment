## Network Diagram (MPLS VPN network)

- IOSXE devices
- All devices connected to the same Management network
- Baseline (Hostname and MGMT address already applied to the devices)

```mermaid
flowchart LR
  subgraph CUSTOMER SITE 01
      A[EDGE01]
  end
  subgraph MPLS CORE
      A --- B(PE01)
      B --- C(P01)
      C --- D(PE02)
      D --- E[EDGE02]
  end
  subgraph CUSTOMER SITE 02
      E[EDGE02]
  end
```
