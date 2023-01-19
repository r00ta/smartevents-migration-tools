from kubernetes import client, config

# Load the kubeconfig file
config.load_kube_config()

# Create a SecretsV1Api object
v1 = client.CoreV1Api()

# Define the label selector for the Secrets
label_selector = "app.kubernetes.io/managed-by=bridge-fleet-shard-operator,app.kubernetes.io/component=ingress"

# List all Secrets with the specified label
secrets = v1.list_secret_for_all_namespaces(label_selector=label_selector).items

# Iterate through the Secrets
for secret in secrets:
    print("patching secret " + secret.metadata.name + " in namespace " + secret.metadata.namespace)
    
    # Create a patch object with the updated data
    patch = 
        [
            {
                "op": "replace",
                "path": "/data/tls.key",
                "value": "**REDACTED**"
            },
            {
                "op": "replace",
                "path": "/data/tls.certificate",
                "value": "**REDACTED**"
            }
        ]

    # Patch the Secret
    v1.patch_namespaced_secret(
        name=secret.metadata.name,
        namespace=secret.metadata.namespace,
        body=patch
    )    
