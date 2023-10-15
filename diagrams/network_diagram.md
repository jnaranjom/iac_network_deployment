## Network Diagram (MPLS VPN network)

- IOSXE devices
- All devices connected to the same Management network
- Baseline (Hostname and MGMT address already applied to the devices)

```mermaid
flowchart LR
  A[EDGE01]
  subgraph MPLS CORE
      A --- B(PE01)
      B --- C(P01)
      C --- D(PE02)
      D --- E[EDGE02]
  end
  E[EDGE02]
```
