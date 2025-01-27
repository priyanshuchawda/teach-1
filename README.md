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
          subject-path: '${{ github.workspace }}/my-app'
```
