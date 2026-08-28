# dsl-jekyll-theme

Shared Jekyll theme for **Hertie Data Science Lab** websites — the single source of visual
truth for every DSL site: the onboarding site, course / cohort sites, and anything new.
Restyle once here and every consuming site follows on its next version bump.

## What this theme provides

Generic chrome only:

- layouts `default`, `page`, `post`
- the head, header, nav and footer partials
- the stylesheet at `/assets/css/main.css` and brand images under `/assets/images/`

A consuming site supplies its own content, `_data/nav.yml`, and `_config.yml` (`title` or
`course_name`, `schoolname`, `address`, …). `course_semester` is optional; without it no
semester line renders.

**Course-specific layouts are not here.** The Schedule, Lectures, Labs, Readings, All
Materials, Assignments and Home pages of a DSL course site are rendered by templates in
[`dsl-teaching-toolkit`](https://github.com/hertie-data-science-lab/dsl-teaching-toolkit)
(`templates/site/`), which the course sync writes into each site repo. They read front
matter that repo's `site.py` generates, so they change with it and are tested against it.

## Use it

In a consuming site's `_config.yml`, **pinned to a tag**:

```yaml
remote_theme: hertie-data-science-lab/dsl-jekyll-theme@v1.0.0
plugins:
  - jekyll-remote-theme
```

and in its `Gemfile`:

```ruby
gem "jekyll-remote-theme"
```

Pin, do not track `main`. An unpinned site rebuilds against whatever merged here minutes
ago, with no review in between — which has broken live sites twice.

## Versioning

SemVer tags, and the major is what a consumer's pin is really for:

| Bump | For |
|---|---|
| **major** (`v2.0.0`) | a layout, include or CSS class a consumer may depend on is removed or renamed |
| **minor** (`v1.1.0`) | something new that existing sites keep rendering without |
| **patch** (`v1.0.1`) | a fix that changes no contract |

Cut a tag on `main`, then bump the pin in each consumer. For DSL course sites that is one
line — `site.THEME_REF` in the toolkit — and the next sync carries it to every cohort.

## Restyle

Brand colours live in [`_sass/_user_vars.scss`](_sass/_user_vars.scss) (Hertie red
`#BA0020` etc.). Shared components (cards, buttons, callouts) live in
[`_sass/_cards.scss`](_sass/_cards.scss).

A consuming site adds its own styles in `_sass/_course.scss`. `assets/css/main.scss`
imports it **last**, so it can override anything above and every variable declared here is
in scope for it. The copy in this repo is empty — Jekyll puts a site's own `_sass` ahead of
the theme's, so a site that ships the file gets its own and a site that does not resolves
to the empty one. DSL course sites are written one by the course sync.

## Auto-propagation

On a push to `main`, [`.github/workflows/notify-consumers.yml`](.github/workflows/notify-consumers.yml)
sends a `repository_dispatch` (`theme-updated`) to every repo in
[`consumers.txt`](consumers.txt), triggering a rebuild. A **pinned** consumer rebuilds
against its pin and so shows no change until the pin moves — which is the point. The
dispatch still matters for consumers that deliberately track a branch.

## Correctness gate

[`.github/workflows/pr-build.yml`](.github/workflows/pr-build.yml) builds a fixture
consuming site against the checkout on every PR (see [`tests/README.md`](tests/README.md)).
The theme has no pages of its own, so building this repo alone renders no layout at all.

## Brand assets

Logo / favicon / pattern under `assets/images/` are vendored from the canonical
[`dsl-assets`](https://github.com/hertie-data-science-lab/dsl-assets) repo. Update them
there first, then refresh the copies here.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```
