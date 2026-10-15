# Exercise 10: Multi-Node Kubernetes Cluster

## Objective
Deploy two Flask applications on a three-node Minikube Kubernetes cluster using Deployments, Services, replicas, and pod anti-affinity.

## Cluster
- Profile: devops-multinode
- Nodes: 3
- Kubernetes version: v1.35.1

## Applications

### Product Catalog
- File: product_catalog.py
- Endpoint: GET /products
- Replicas: 2
- Service: product-catalog-service
- NodePort: 30081

### Shopping Cart
- File: shopping_cart.py
- Endpoints: GET /cart, POST /cart
- Replicas: 3
- Service: shopping-cart-service
- NodePort: 30082

## Docker Images
- product-catalog:latest
- shopping-cart:latest

## Kubernetes Manifests
- product-catalog.yaml
- shopping-cart.yaml

## Validation
- Three Kubernetes nodes reached Ready status.
- Product Catalog deployment reached 2/2 ready replicas.
- Shopping Cart deployment reached 3/3 ready replicas.
- Both NodePort Services were created.
- Shopping Cart GET and POST requests were tested successfully.

## Notes
The Shopping Cart stores data in application memory. Data is not shared between replicas and can be lost when a pod restarts.
