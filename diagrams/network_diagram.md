## Network Diagram (MPLS VPN network)

- IOSXE devices
- All devices connected to the same Management network
- Baseline (Hostname and MGMT address already applied to the devices)

```mermaid
flowchart LR
  subgraph CUSTOMER SITE 01
      A[EDGE01] --- B(PE01)
  end
  subgraph MPLS CORE
      B --- C(P01)
      C --- D(PE02)
  end
  subgraph CUSTOMER SITE 02
      D(PE02) --- E[EDGE02]
  end
```
