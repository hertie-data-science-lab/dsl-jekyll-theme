# dsl-jekyll-theme

Shared Jekyll theme for **Hertie Data Science Lab** websites — the single source of visual
truth for every DSL site: the onboarding site, course / cohort sites, and anything new.
Restyle once here and every consuming site follows on its next version bump.

## What this theme provides

Generic chrome only:

- layouts `default`, `page`, `post`
- the head, header, nav and footer partials
- the stylesheet at `/assets/css/main.css` and brand images under `/assets/images/`

A consuming site supplies everything else — see **Use it** below. `course_name` and
`course_semester` are optional: the chrome falls back to `title`, and without a semester
no semester line renders.

**Course-specific layouts are not here.** The Schedule, Lectures, Labs, Readings, All
Materials, Assignments and Home pages of a DSL course site are rendered by templates in
[`dsl-teaching-toolkit`](https://github.com/hertie-data-science-lab/dsl-teaching-toolkit)
(`templates/site/`), which the course sync writes into each site repo. They read front
matter that repo's `site.py` generates, so they change with it and are tested against it.

## Use it

In a consuming site's `_config.yml`, pinned to a `<ref>` — a tag or a full commit SHA,
never a branch:

```yaml
remote_theme: hertie-data-science-lab/dsl-jekyll-theme@<ref>
plugins:
  - jekyll-remote-theme
```

and in its `Gemfile`:

```ruby
gem "jekyll-remote-theme"
```

An unpinned site rebuilds against whatever merged here minutes ago, with no review in
between — which has broken live sites twice.

The site must supply its own content, `_data/nav.yml` (the tab bar `_includes/nav.html`
reads), and a `_config.yml` with at least `title` — plus `schoolname`, `schoolurl` and
`address` for the header and footer. It may also ship `_sass/_course.scss`: Jekyll puts a
site's own `_sass` ahead of the theme's, and `assets/css/main.scss` imports `course`
**last**, so that file overrides anything here with every theme variable in scope. This
repo's copy is empty, so a site without one still resolves the import.

## Versioning

There are **no tags yet**. Consumers pin a SHA: `dsl_course/site_repo.py` in the toolkit
pins `9288394…` for every cohort site, and `mds-onboarding` and `course-website-template`
currently track `main` unpinned.

The plan, once the current work lands:

- **`v1.0.0`** at `9288394` — the last commit before the course layouts left the theme, so
  today's sites can move from a SHA to a tag with no rendering change.
- **`v2.0.0`** at the merge of the branch that removes them. A major, because a consuming
  site that used the Schedule / Lectures / Assignments layouts loses them.

After that, SemVer: **major** when a layout, include or CSS class a consumer may depend on
goes or is renamed; **minor** for something new that existing sites render fine without;
**patch** for a fix that changes no contract. Cut the tag on `main`, then bump each
consumer's pin — for DSL course sites that is `THEME_REF` in the toolkit, and the next
sync carries it to every cohort.

## Restyle

Brand colours live in [`_sass/_user_vars.scss`](_sass/_user_vars.scss) (Hertie red
`#BA0020` etc.). Shared components (cards, buttons, callouts) live in
[`_sass/_cards.scss`](_sass/_cards.scss).

A consuming site's own styles go in its `_sass/_course.scss` — see **Use it** above. DSL
course sites are written one by the course sync.

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
