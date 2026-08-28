# Releases

This project supports release-based documentation versioning.

## Release workflow

The documentation is published through GitHub Actions and GitHub Pages using MkDocs Material. Each release can keep a stable documentation version and provide a version switcher.

## Versioning strategy

The recommended workflow is:

1. create a GitHub release,
2. tag the repository,
3. let the CI workflow build the docs,
4. deploy the generated site to GitHub Pages.

## Example release tag

```bash
git tag v1.0.0
git push origin v1.0.0
```

This makes the release available in the docs version selector and keeps the stable documentation for that version.

## GitHub Pages

The published site is available through the GitHub Pages deployment URL associated with the repository.

## Repo link

- Repository: https://github.com/your-username/NLP-Mailer
