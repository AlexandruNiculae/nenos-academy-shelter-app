# What is CI/CD

Continuous Integration and Continuous Deployment (CI/CD) is a software development practice that automates the process of building, testing, and deploying applications. It helps ensure that code changes are automatically verified and deployed with minimal manual intervention.

## CI (Continuous Integration)
Continuous Integration is the practice of frequently integrating code changes into a shared repository. The most common steps in a CI pipeline include:

- **Code Checkout**: Pull the latest code from the repository.
- **Build**: Compile or package the application.
- **Linting**: Run static code analysis tools like `pylint` to enforce coding standards.
- **Unit Tests**: Execute tests using frameworks like `pytest` to ensure code correctness.
- **Security Scanning**: Analyze dependencies for vulnerabilities.
- **Artifacts Creation**: Store build outputs for later use in deployment.

## CD (Continuous Deployment)
Continuous Deployment (or Continuous Delivery) automates the release process, ensuring that tested code changes are deployed quickly and reliably. Common steps in a CD pipeline include:

- **Pulling Artifacts**: Retrieve built images or binaries.
- **Running Integration Tests**: Validate that services work together correctly.
- **Deploying to Staging**: Test deployment in a pre-production environment.
- **Approval Gates**: Require manual approval (optional, for Continuous Delivery).
- **Deploying to Production**: Push the new version to live users.
- **Rollback Strategies**: Ensure quick recovery in case of failure.

# GitHub Actions
GitHub Actions is a CI/CD tool integrated with GitHub that allows developers to automate workflows for building, testing, and deploying code.

## What it allows under the free plan
GitHub provides **free usage** for GitHub Actions in public repositories. For private repositories, free-tier limits apply:

- **2,000 free minutes per month** for personal accounts.
- **3,000 minutes** for Pro and Team plans.
- **50,000 minutes** for Enterprise plans.
- **Supports Linux, macOS, and Windows runners.**

## Limitations
GitHub Actions enforces the following restrictions:

- **Job Timeout**: Each job can run for a maximum of **6 hours**.
- **Concurrency Limits**: The free plan allows **up to 20 concurrent jobs**.
- **Storage Limits**: Artifact and log storage have retention policies (default is 90 days).
- **Additional minutes are billed** beyond the free limit.

# How to run
To create a GitHub Actions workflow, follow these steps:

1. **Create a `.github/workflows/` directory** in your repository if it doesn’t exist.
2. **Add a YAML file** (e.g., `ci-cd-pipeline.yml`) inside the workflows directory.
3. **Define your CI/CD pipeline** in the YAML file, for example:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Build Docker image
        run: docker build -t my-python-app .

      - name: Run linting with pylint
        run: docker run --rm my-python-app pylint your_python_module

      - name: Run tests with pytest
        run: docker run --rm my-python-app pytest
```

# Where to see the results
After a workflow runs, you can view the results in GitHub:

1. **Go to your repository on GitHub**.
2. **Click on the 'Actions' tab** at the top.
3. **Select the workflow run** you want to inspect.
4. **Check the logs** by expanding each job and step.
5. **Download artifacts** (if applicable) from the workflow run.

This allows you to debug errors, monitor deployments, and verify the success of each workflow execution.