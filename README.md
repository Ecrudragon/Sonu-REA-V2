# Sonu REA V2

Sonu REA V2 is a responsive, Android-first educational guide for responsible app analysis. It focuses on explicit authorization, safe test environments, careful data handling, reproducible validation, and coordinated vulnerability disclosure.

## Project contents

- `index.html` — static, responsive project site.
- `docs/RESPONSIBLE_USE.md` — scope, safety, and responsible disclosure guidance.
- `CONTRIBUTING.md` — contribution expectations.
- `SECURITY.md` — private vulnerability reporting guidance.
- `scripts/check_html.py` — dependency-free structural check for the homepage.
- `.github/workflows/` — HTML validation and GitHub Pages deployment.

## Preview locally

Open `index.html` in a browser. The page has no build step. Tailwind CSS, Lucide icons, and fonts are loaded from third-party CDNs, so those assets require an internet connection.

## Publish with GitHub Pages

The `Deploy GitHub Pages` workflow publishes the static site after a push to `main` or a manual run. In repository Settings → Pages, choose GitHub Actions as the deployment source if it is not already selected. After the first successful workflow run, GitHub displays the published URL in the Pages settings.

## Responsible use

Use this guide only for applications you own or are explicitly authorized to assess. Respect software licenses, privacy, platform terms, and applicable law. Do not use it to bypass payments, authentication, integrity checks, or other security controls, or to modify third-party apps without permission. This repository is educational and is not legal advice. See [`docs/RESPONSIBLE_USE.md`](docs/RESPONSIBLE_USE.md).

## Security and contributions

Never commit APKs, credentials, signing keys, private certificates, personal data, or confidential vulnerability details. Report security issues privately as described in [`SECURITY.md`](SECURITY.md), and review [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a change.

## License

No open-source license has been selected for this repository. Unless a license is added, all rights remain with the respective copyright holder; do not assume permission to reuse or redistribute the content. Third-party dependencies and assets remain under their own terms.
