# dsl-jekyll-theme

Shared Jekyll theme for **Hertie Data Science Lab** websites — the single source of
visual truth (layout, branding, colours) for all DSL sites: the onboarding site, course
/ cohort sites, and anything new. Restyle once here and every consuming site follows.

## Use it

In a consuming site's `_config.yml`:

```yaml
remote_theme: hertie-data-science-lab/dsl-jekyll-theme
plugins:
  - jekyll-remote-theme
```

and in its `Gemfile`:

```ruby
gem "jekyll-remote-theme"
```

The theme provides the `default`, `page`, and `home` layouts (plus course-specific
`assignment`, `lectures`, `schedule`, `class`), the site header/footer/nav, the
stylesheet at `/assets/css/main.css`, and brand images under `/assets/images/`.
A consuming site supplies its own content, `_data/nav.yml`, and `_config.yml`
(`course_name`, `course_semester`, `schoolname`, `address`, etc.).

## Restyle

All brand colours live in [`_sass/_user_vars.scss`](_sass/_user_vars.scss) (Hertie red
`#BA0020` etc.). Shared components (cards, buttons, callouts, the maths pyramid, the
two-approaches comparison, de-emphasised resource lists) live in
[`_sass/_cards.scss`](_sass/_cards.scss). Edit, push to `main`, and the change fans out
(see below).

## Auto-propagation

On a push to `main`, [`.github/workflows/notify-consumers.yml`](.github/workflows/notify-consumers.yml)
sends a `repository_dispatch` (`theme-updated`) to every repo listed in
[`consumers.txt`](consumers.txt), triggering each to rebuild and pick up the new theme.

**Setup (once):** add a repo secret `THEME_DISPATCH_TOKEN` — a fine-grained PAT (or
GitHub App token) with `actions: write` on the consumer repos. (The default
`GITHUB_TOKEN` cannot trigger workflows in other repositories.) Without it, the fan-out
step no-ops and consumers simply re-theme on their next own build (or weekly schedule).

## Brand assets

Logo / favicon / pattern under `assets/images/` are vendored from the canonical
[`dsl-assets`](https://github.com/hertie-data-science-lab/dsl-assets) repo. Update them
there first, then refresh the copies here.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```
