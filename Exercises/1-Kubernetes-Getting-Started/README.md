# Kubernetes Exercise 1 - Hello Pod

## Objective

Deploy an Nginx container as a Kubernetes Pod using Minikube and expose it using a NodePort Service.

## Technologies Used

- Kubernetes
- Minikube
- Docker
- kubectl
- Nginx

## Architecture

```text
Browser
   ↓
NodePort Service
   ↓
Nginx Pod
   ↓
Nginx Container