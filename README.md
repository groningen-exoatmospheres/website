# ExoAIM Lab website

Source of the ExoAIM Lab (Exo-Atmospheric Interpretation and Modeling) group website —
Kapteyn Astronomical Institute, University of Groningen.

Built with [Hugo](https://gohugo.io) and the [HugoBlox](https://hugoblox.com) "research group"
theme. Every push to `main` is built and deployed to GitHub Pages by
`.github/workflows/hugo.yaml`.

## Where things are

| What | Where |
|---|---|
| Homepage slider | `content/_index.md` |
| Team profiles | `content/authors/<id>/_index.md` + `avatar.jpg` |
| Research pages | `content/research/<topic>/index.md` + `featured.*` |
| News posts | `content/post/<date_title>/index.md` + `featured.*` |
| Publications | `content/publication/<firstauthor><year>_<keyword>/` (`index.md`, `cite.bib`, `featured.*`) |
| Menu | `config/_default/menus.yaml` |
| Site settings | `config/_default/params.yaml`, `config/_default/hugo.yaml` |
| Custom styling | `assets/scss/custom.scss` |
| Publication helper script | `scripts/update_publications.py` |

## Preview locally

Install Hugo **extended** and Go, then from the repository root:

```bash
hugo server
```

and open http://localhost:1313. (No need to commit the `public/` folder: GitHub Actions builds it.)

## Publications

Publications are kept in sync with the group's SciX/ADS library by a helper script:

```bash
export ADS_API_TOKEN=...          # personal token: https://scixplorer.org/user/settings/token
python3 scripts/update_publications.py --dry-run   # preview
python3 scripts/update_publications.py             # add new papers + update existing ones
```

- New papers get a folder with `index.md`, `cite.bib` and a proposed `featured` image
  (a figure from the arXiv HTML version). Review the summary, tags and caption.
  Alternative figures are saved in `scripts/_candidates/<folder>/` (not published).
- Existing arXiv-only entries are upgraded to their journal version, and missing PDF links
  are filled in (`--no-update` to disable).
- Delete any folder you don't want: it will not be re-created.
- `--since 2025` ignores older papers, `--fill-figures` adds images where missing,
  `--clean-images` tidies all featured images.
- Optional but recommended: `pip install pillow` (image cleaning) and
  `brew install librsvg` (for figures that only exist as SVG).

Never commit the ADS token.

## Adding a team member

Copy an existing folder in `content/authors/`, rename it (this becomes the author id),
edit `_index.md` (name, role, `user_groups`, social links, bio) and replace `avatar.*`
(a square photo of ~600 px is plenty). Use the same id in publication `authors:` lists to
link papers to the profile.
