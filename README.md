# DevSecOps Pipeline

The DevSecOps pipeline utilizes GitLab CI/CD, integrating security assurance and compliance checks at each stage of the pipeline.

## Technologies used

- GitLab
- Docker
- SonarQube
- Safety (Python dependency scanner)
- Bandit

## Project structure

- `app/`: Contains the source code and configuration file for a sample web application
- `.gitlab-ci.yml`: Defines the GitLab CI/CD pipeline configuration
- `sonar-project.properties`: Configures SonarQube settings
## How it works

The GitLab CI/CD pipeline triggers on code push or merge request.
The pipeline builds a Docker image for the web application using the Dockerfile in the app/ directory.
Security Static Application Testing (SAST) is performed using SonarQube to scan the source code for vulnerabilities.
Automatic dependency scanning is conducted using Safety to detect vulnerabilities in application dependencies and libraries.
The pipeline commits clean code to the project's main branch.

To set up this pipeline, deploy a SonarQube server and provision a virtual machine for GitLab Runner. Docker must be installed on the GitLab Runner. Previously, due to Dockerhub restrictions in Russia (no longer relevant), consider deploying a local Docker registry for necessary images. Ensure to configure secure variables with appropriate passwords in the project settings on GitLab.






