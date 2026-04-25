# Release process

Releases are driven by Git tags in the format `v*.*.*` (example: `v1.2.3`).

## What happens on release

When a release tag is pushed, GitHub Actions will:

1. Validate Python source compiles.
2. Build and push multi-arch image to GHCR.
3. Generate SBOM and provenance attestation.
4. Scan image vulnerabilities with Trivy.
5. Sign image using Cosign keyless signing (OIDC).
6. Create GitHub Release notes automatically.

## Published image tags

- `vX.Y.Z`
- `vX.Y`
- `vX`
- `sha-<shortsha>`
- `latest` (only when release is from default branch)

## Image location

`ghcr.io/<owner>/<repo>`
