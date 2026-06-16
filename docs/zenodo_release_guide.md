# Zenodo Release Guide

Use this guide to mint a software DOI for this GitHub repository.

## One-Time Zenodo Setup

1. Sign in to https://zenodo.org/.
2. Open your profile menu and go to **Linked accounts**.
3. Connect GitHub.
4. Open the GitHub integration page in Zenodo.
5. Enable archiving for `tyilmaz23/DRLAlgoMapfree`.

Zenodo must be connected before publishing a GitHub release if you want the release to be archived automatically.

## Release

After Zenodo is connected and the repository is enabled:

```powershell
gh release create v1.0.0 --repo tyilmaz23/DRLAlgoMapfree --title "DRLAlgoMapfree v1.0.0" --notes-file docs/release_notes_v1.0.0.md --latest
```

Zenodo should then archive the GitHub release and mint a software DOI.

## DOI Minted

Zenodo created the software archive:

- Version DOI: https://doi.org/10.5281/zenodo.20715169
- Concept DOI: https://doi.org/10.5281/zenodo.20715168
- Zenodo record: https://zenodo.org/records/20715169

Add the Zenodo DOI to ORCID as software or research output.
