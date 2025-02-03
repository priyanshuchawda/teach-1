# teach-1
# teach-1

## Usage Instructions for `actions/attest-build-provenance@v2`

Within the GitHub Actions workflow which builds some artifact you would like to attest:

Ensure that the following permissions are set:

```yaml
permissions:
  id-token: write
  attestations: write
```

The `id-token` permission gives the action the ability to mint the OIDC token necessary to request a Sigstore signing certificate. The `attestations` permission is necessary to persist the attestation.

Add the following to your workflow after your artifact has been built:

```yaml
- uses: actions/attest-build-provenance@v2
  with:
    subject-path: '<PATH TO ARTIFACT>'
```

The `subject-path` parameter should identify the artifact for which you want to generate an attestation.

## Example Workflow for Generating Signed Build Provenance Attestations

```yaml
name: build-attest

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
      attestations: write

    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Build artifact
        run: make my-app
      - name: Attest
        uses: actions/attest-build-provenance@v2
        with:
          subject-path: '${{ github.workspace }}/path-to-artifact'
```

## Flake8 Installation and Usage

To ensure code quality and consistency, we use `flake8` for linting. Follow the steps below to install and use `flake8` in your project.

### Installation

1. Add `flake8` to your `environment.yml` file under the `dependencies` section:

```yaml
dependencies:
  - flake8
```

2. Install the dependencies using conda:

```sh
conda env update --file environment.yml --name base
```

### Usage

To run `flake8` and check your code for issues, use the following commands:

```sh
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

These commands will check your code for syntax errors, undefined names, and other issues, and provide statistics on the results.
