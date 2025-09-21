Docker notes and examples

Quick start (local dev)

1. Build and run with docker-compose (requires Docker Desktop or docker CLI):

   cd docker
   docker compose up --build

   - Backend will be available at http://localhost:8000
   - Frontend dev server will be available at http://localhost:3000

Security & sandboxing notes (running untrusted code)

- If you need to execute arbitrary or user-submitted code, run it inside properly isolated containers. Use a separate image and a short-lived container per execution. Example approach:
  - Create a minimal runner image (e.g. based on python:3.12-slim) that contains only the necessary runtime.
  - Run containers with restricted capabilities and resource limits (cpu, memory) and with user namespaces mapped.
  - Use Docker's read-only filesystem mounts where possible.

- Example docker run flags for sandboxing:
  docker run --rm --network "none" --cpus="0.5" --memory="256m" --pids-limit=100 \
    --read-only --tmpfs /tmp:rw --security-opt no-new-privileges --user 1000:1000 your-runner-image:tag \
    /bin/sh -c "python /runner/run_task.py"

Using docker-py from the backend

- The `docker` Python package (docker-py) is included in the backend requirements. Example usage from your backend:

```python
import docker
client = docker.from_env()
container = client.containers.run(
    'your-runner-image:latest',
    command='python /runner/run_task.py',
    detach=True,
    network_disabled=True,
    mem_limit='256m',
    cpu_quota=50000,  # relative to cfs_period_us
    remove=True,
    security_opt=['no-new-privileges']
)
# Optionally use logs(), wait(), etc.
```

- Important: if your app is running inside Docker and you want to control sibling containers, mount the docker socket into the container (not recommended for production):

  -v /var/run/docker.sock:/var/run/docker.sock

  Mounting the host socket gives the container full control over the Docker daemon. Prefer a safer orchestration approach (separate service that receives jobs and runs containers with limited privileges) or use docker-in-docker with careful security controls.

Notes

- The example compose file mounts local code into containers for dev convenience. For production, build images with code baked in and avoid mounting local source.
- Always tune resource limits and timeouts when running arbitrary code.
