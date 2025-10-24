Kubernetes Portfolio Project – Kube Center

This project was created to gain hands-on experience with containerization and orchestration using Docker and K3s Kubernetes. I built a simple Django web application and deployed it to a Linux virtual machine running K3s, then accessed it from my Windows system to test connectivity and service exposure.

The goal was to understand how Kubernetes manages containerized workloads, handles failures, and maintains availability through self-healing and scaling. The application includes health probes, a NodePort service for external access, and basic monitoring endpoints.

Features

Containerized Django web application using Docker

Deployed on K3s Kubernetes running on Ubuntu

Configured readiness and liveness probes for health checks

NodePort service for external access

Tested scaling, redundancy, and self-healing by deleting pods

Cross-platform deployment between Windows (host) and Linux (VM)

Technologies Used

Kubernetes (K3s)

Docker

Django

Python

Linux (Ubuntu)

YAML Configuration

Git and GitHub

Lessons Learned

This project gave me practical experience in containerization, orchestration, and troubleshooting within Kubernetes. I learned how to build and transfer Docker images between systems, configure YAML files for deployments and services, and work with readiness and liveness probes. It also helped me understand the relationship between Docker and Kubernetes and how orchestration tools maintain uptime and reliability.

Future Plans

I plan to expand this project with a more complex demonstration, such as a small interactive web game that visually shows pod replacement and scaling in real time.
