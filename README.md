# NAT Gateway Simulator

A Python-based simulation of a Network Address Translation (NAT) Gateway for a private network.

This project demonstrates how multiple devices inside a private network can communicate with an Internet server through a single public IP address using NAT and PAT.

---

## Project Overview

In a private network, devices usually use private IP addresses such as:

* 10.0.0.10
* 10.0.0.11
* 10.0.0.12

These addresses are not directly routable over the public Internet.

A NAT Gateway solves this problem by translating private IP addresses into a public IP address when packets leave the private network.

This simulator demonstrates that process in software.

---

## Objectives

The main objectives of this project are:

* Simulate a private computer network.
* Simulate a NAT Gateway.
* Perform private-to-public IP translation.
* Demonstrate Port Address Translation (PAT).
* Maintain a NAT connection table.
* Perform reverse NAT for incoming responses.
* Track active connections.
* Block unsolicited inbound traffic.
* Expire inactive NAT connections.
* Maintain packet and connection statistics.

---

## Network Architecture

```text
                    INTERNET
                        │
                        │
               198.51.100.20:80
                        │
                        │
                ┌───────▼────────┐
                │  NAT GATEWAY   │
                │                │
                │ Private:       │
                │ 10.0.0.1       │
                │                │
                │ Public:        │
                │ 203.0.113.10   │
                └───────┬────────┘
                        │
                PRIVATE NETWORK
                        │
          ┌─────────────┼─────────────┐
          │             │             │
        PC-A           PC-B          PC-C
     10.0.0.10      10.0.0.11      10.0.0.12
```
