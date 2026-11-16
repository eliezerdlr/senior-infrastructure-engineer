# Kubernetes Best Practices

## Resource Management

### Always Set Resource Requests and Limits
```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

**Guidelines:**
- Requests = guaranteed resources
- Limits = maximum resources
- Set requests based on normal usage
- Set limits based on peak usage
- Memory limit = 2x request is common
- Avoid CPU limits in most cases (causes throttling)

### Use Horizontal Pod Autoscaler
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## Pod Configuration

### Use Liveness and Readiness Probes
```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### Configure Pod Disruption Budgets
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: myapp
```

### Use Anti-Affinity for High Availability
```yaml
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
    - weight: 100
      podAffinityTerm:
        labelSelector:
          matchLabels:
            app: myapp
        topologyKey: kubernetes.io/hostname
```

## Security

### Run as Non-Root
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 1000
  fsGroup: 1000
```

### Read-Only Root Filesystem
```yaml
securityContext:
  readOnlyRootFilesystem: true
volumeMounts:
- name: tmp
  mountPath: /tmp
volumes:
- name: tmp
  emptyDir: {}
```

### Drop All Capabilities
```yaml
securityContext:
  capabilities:
    drop:
    - ALL
```

## Networking

### Use Network Policies
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

### Service Mesh for mTLS
- Istio, Linkerd, or Consul Connect
- Automatic encryption between services
- Traffic management capabilities

## Configuration Management

### Use ConfigMaps for Configuration
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "info"
  DATABASE_HOST: "postgres.default.svc"
```

### Use Secret References for Sensitive Data
```yaml
env:
- name: DATABASE_PASSWORD
  valueFrom:
    secretKeyRef:
      name: app-secrets
      key: database-password
```

### External Secrets for Production
- Use an approved external secret operator or platform workload identity
- Integrate with Vault, AWS Secrets Manager, or the organization-approved equivalent
- Never place plaintext values in manifests, command arguments, logs, or git
- Limit secret-reader permissions and define rotation and recovery ownership

## Observability

### Structured Logging
- Output JSON logs
- Include correlation IDs
- Use consistent field names

### Metrics
- Expose Prometheus metrics
- Use standard naming conventions
- Include SLI metrics

### Distributed Tracing
- Implement OpenTelemetry
- Propagate trace context
- Sample appropriately
