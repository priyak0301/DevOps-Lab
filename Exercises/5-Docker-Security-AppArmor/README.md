# Docker Security with AppArmor and Python

## Objective
Secure a Dockerized Flask application using an AppArmor profile and the Docker SDK for Python, then check restricted actions.

## Files
- `app.py` — Flask web application.
- `Dockerfile` — Builds the Docker image.
- `requirements.txt` — Flask dependency.
- `my-apparmor-profile` — AppArmor policy source.
- `apply_apparmor.py` — Builds the image and checks AppArmor support.
- `test_restricted_actions.py` — Checks profile status before testing restricted actions.

## Task 1: Flask Application
The Flask application serves a message at `/` on port 5000.

## Task 2: Build and Test
Build the image:

    docker build -t flask-apparmor .

Run the container:

    docker run -d --name flask-apparmor-test -p 5000:5000 flask-apparmor

Test the endpoint:

    curl -i http://localhost:5000/

Observed result: HTTP 200 OK.

## Task 3: AppArmor Profile
The policy source is stored in `my-apparmor-profile`.

On a supported Linux host with AppArmor enabled, review and validate the policy, install it at `/etc/apparmor.d/my-apparmor-profile`, and load it:

    sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile

Confirm the profile is loaded before starting a container with:

    docker run --security-opt="apparmor=my-apparmor-profile" -p 5000:5000 flask-apparmor

The policy must be validated against the target host and application. Saving a profile file does not prove enforcement.

## Task 4: Docker SDK for Python
Install the SDK:

    python3 -m pip install docker

Run:

    python3 apply_apparmor.py

The script checks Docker security options and reports when AppArmor support is unavailable.

## Task 5: Restricted-Action Tests
Run:

    python3 test_restricted_actions.py

The script checks whether the requested profile is reported active before testing restricted actions. A failed command alone does not prove AppArmor caused the denial; host audit logs should also be checked.

## Observed Results and Environment
- Docker image built successfully.
- Flask container started and returned HTTP 200 OK.
- Docker SDK for Python 7.2.0 installed.
- AppArmor kernel check returned `N` in the current Ubuntu WSL environment.
- Docker did not report AppArmor support.
- Container inspection returned a blank AppArmor profile.
- AppArmor enforcement and restricted-action blocking have not been demonstrated in this environment.
- Actual enforcement testing requires a supported Linux host with AppArmor enabled and the profile loaded.

## Theory Questions and Answers

### 1. What is the purpose of using AppArmor with Docker containers?
AppArmor adds mandatory access control by confining an application to permitted resources and operations. It provides an additional layer of security beyond ordinary container isolation.

### 2. How do AppArmor profiles help secure a Docker container?
Profiles define permitted and denied operations. They can restrict file access, program execution, capabilities, and certain network operations, reducing the impact of a compromised application.

### 3. Why restrict sensitive directories such as `/etc/` and `/var/`?
`/etc/` contains system configuration files, while `/var/` may contain logs, caches, and application data. Limiting unnecessary access reduces exposure and helps prevent unauthorized reading or modification. Rules must still allow files required by the application.

### 4. What other capabilities can be restricted using AppArmor profiles?
Depending on application requirements, restrictions can include capabilities such as `sys_admin`, `sys_ptrace`, `net_admin`, and `sys_module`. Policies should follow least privilege and be tested carefully.

### 5. How can you verify that an AppArmor profile is applied?
Inspect the container's `AppArmorProfile` field and Docker security options. On the Linux host, use `aa-status` and review AppArmor audit logs. A requested security option alone does not prove that a profile is loaded and enforcing its rules.
