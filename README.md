# Nikhil Kushwaha — Portfolio

A responsive, static personal portfolio for selected software, AI, and data projects.

## Features

- Responsive layout for mobile, tablet, and desktop
- Filterable project cards
- Keyboard-accessible navigation and reduced-motion support
- No JavaScript framework, build process, API key, or backend required
- Project descriptions state benchmark scope and prototype limitations
- Automated checks for local asset links, section anchors, and featured project links

## Run locally

Open `index.html` in a browser, or from the repository root run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Publish with GitHub Pages

1. Open the repository's **Settings → Pages**.
2. Set the deployment source to **Deploy from a branch**.
3. Choose the `main` branch and `/(root)` folder, then save.
4. Wait for Pages to publish the site and use the URL shown in Settings → Pages.

The site is plain static HTML/CSS/JavaScript, so no build step is needed.

## Validate changes

Python 3.10+:

```bash
python -m unittest discover -s tests -v
```

The tests use only Python's standard library and do not make network requests.

## Content maintenance

Project cards link to public repositories only. Keep descriptions aligned with implementation and update benchmark figures only when they can be reproduced from project evaluation.

## Contact

- GitHub: https://github.com/nikhil-247
- LinkedIn: https://www.linkedin.com/in/nikhil-kushwaha-265880273
- Email: nikhilkushwaha6027@gmail.com
