# NAT Gateway Simulation for Private Networks

## Computer Networks Project Report

---

# 1. Introduction

Network Address Translation (NAT) is a networking technique used to translate private IP addresses into public IP addresses.

Private networks commonly use address ranges such as:

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

These addresses are intended for internal networks and are not directly routable over the public Internet.

NAT allows devices using private addresses to communicate with external networks through a public IP address.

This project implements a software simulation of a NAT Gateway using Python.

---

# 2. Problem Statement

A private network may contain multiple devices that need to communicate with Internet servers.

However, private IP addresses cannot be directly used as public Internet addresses.

The system therefore needs a mechanism that can:

1. Translate private IP addresses into a public address.
2. Distinguish multiple simultaneous connections.
3. Maintain mappings between internal and external connections.
4. Translate returning packets back to the correct private host.
5. Remove inactive connections.
6. Reject packets that do not correspond to an existing connection.

This project simulates these operations through a NAT Gateway.

---

# 3. Objectives

The objectives of the project are:

- To understand NAT operation.
- To simulate private and public IP addressing.
- To implement Port Address Translation.
- To simulate multiple internal hosts sharing one public IP.
- To maintain a NAT translation table.
- To implement reverse NAT.
- To track connection activity.
- To implement session timeout.
- To simulate unsolicited inbound packet rejection.
- To collect network statistics.

---

# 4. System Architecture

The simulated network contains three private hosts, one NAT Gateway and one Internet server.

```text
                         INTERNET

                    ┌─────────────────┐
                    │  Internet Server│
                    │ 198.51.100.20   │
                    │      Port 80     │
                    └────────┬────────┘
                             │
                             │
                    PUBLIC NETWORK
                             │
                    ┌────────▼────────┐
                    │   NAT GATEWAY   │
                    │                 │
                    │ Private IP      │
                    │ 10.0.0.1        │
                    │                 │
                    │ Public IP       │
                    │ 203.0.113.10    │
                    └────────┬────────┘
                             │
                    PRIVATE NETWORK
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼─────┐
        │   PC-A    │  │   PC-B    │  │   PC-C    │
        │10.0.0.10  │  │10.0.0.11  │  │10.0.0.12  │
        └───────────┘  └───────────┘  └───────────┘