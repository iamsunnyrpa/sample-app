# Containerized Application Foundation

This repository establishes a foundational structure for **containerized workloads**, specifically featuring a **sample Python application** and the requisite **Docker** and **Kubernetes** configuration files. These resources are designed to facilitate the process of building a Docker image and subsequently deploying it to a **DigitalOcean Kubernetes Service (DOKS)** cluster.

---

## Prerequisites

Before initiating the deployment process, ensure the following tools and services are installed, configured, and accessible within your environment:

* **Docker:** Essential for building and managing container images.
* **DigitalOcean Kubernetes Service (DOKS) Cluster:** A pre-provisioned and running Kubernetes cluster on DigitalOcean.
* **DigitalOcean Container Registry (DOCR):** A private container registry service to securely store your built Docker image.
* **doctl:** The official DigitalOcean command-line interface for interaction with DigitalOcean resources.
* **kubectl:** The standard Kubernetes command-line tool for managing cluster resources.

---

## Deployment Steps

Follow this sequential process to successfully deploy the web application to your DOKS cluster:

### 1. Clone the Repository

Clone the project repository and navigate into the application directory:

```bash
git clone [https://github.com/your-username/sample-app.git](https://github.com/your-username/sample-app.git)
cd sample-app
````

### 2\. Build the Docker Image

Navigate to the `app` directory and build the Docker image, replacing `<image-name>:<tag>` with your desired image identifier and version:

```bash
cd app
docker build -t <image-name>:<tag> .
```

Verify the successful creation of the image:

```bash
docker images
```

### 3\. Push the Image to DOCR

Follow the official **DigitalOcean Container Registry Quickstart** guide to authenticate and push your newly built image to your DOCR instance.

### 4\. Verify the Image in DOCR

Log into your DigitalOcean account and confirm the image details and availability within the Container Registry interface.

### 5\. Configure Registry Settings for DOKS

Ensure that your DOKS cluster is correctly configured to authenticate and pull images from your DOCR. Consult the **DOKS documentation** for detailed instructions on configuring image pull secrets and registry access.

### 6\. Update Kubernetes Manifest

Navigate to the `k8s` directory and modify the **`service-deployment.yaml`** file. Update the **`image` field** within the Deployment specification to reference the full path of your image in DOCR (e.g., `registry.digitalocean.com/<registry-name>/<image-name>:<tag>`).

### 7\. Authenticate to Your DOKS Cluster

Establish a connection to your DOKS cluster by following the steps outlined in the **DOKS Connect to Cluster Guide**.

### 8\. Verify Cluster Connection

Confirm that `kubectl` is authenticated and targeting the correct cluster context:

```bash
kubectl config current-context
```

### 9\. Deploy the Application

Apply the Kubernetes manifest to create the necessary Service and Deployment resources within your cluster:

```bash
kubectl apply -f service-deployment.yaml
```

### 10\. Validate the Deployment

Monitor the status of the deployed pods and services to ensure successful initialization:

```bash
kubectl get pods
kubectl get svc
```

The application is successfully deployed once the pods reach a `Running` status and the Service is assigned a public IP address (for a LoadBalancer type service).

-----

## Scaling the Application

### Horizontal Pod Autoscaler (HPA)

To enable automatic scaling of the deployment based on resource utilization (e.g., CPU or memory), implement a **Horizontal Pod Autoscaler (HPA)**:

1.  **Install Metrics Server:** Ensure the **Metrics Server** is installed in your cluster, as the HPA relies on it for resource utilization data. Install the Metrics Server using the official Kubernetes [Metrics Server GitHub repository](https://github.com/kubernetes-sigs/metrics-server)
   
2.  **Apply HPA Configuration:** Apply the provided HPA manifest:


```bash
kubectl apply -f hpa.yaml
```
-----
### Useful Documents:

[+] https://docs.docker.com/engine/install/

[+] https://docs.digitalocean.com/products/kubernetes/how-to/create-clusters/

[+] https://docs.digitalocean.com/products/container-registry/getting-started/quickstart/

[+] https://docs.digitalocean.com/reference/doctl/how-to/install/

[+] https://kubernetes.io/docs/tasks/tools/
