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

## After DOI Minting

Once Zenodo provides a DOI:

- Add the Zenodo DOI badge to `README.md`.
- Add the Zenodo DOI to `codemeta.json`.
- Add the Zenodo DOI to `metadata/schema_org_article.jsonld`.
- Add the Zenodo DOI to the GitHub Pages paper page.
- Add the Zenodo DOI to ORCID as software or research output.
