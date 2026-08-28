# Fixture site

`fixture/` is a complete cohort site, used by `.github/workflows/pr-build.yml` to build
this theme on every PR. Building the theme repo alone proves nothing: it has no pages, so
no layout and no include is ever rendered.

It is **real generated output**, copied from `hertie-dsl-demo-f2026.github.io` - what
`python3 -m dsl_course.site sync` actually writes. Not hand-written, so it cannot drift
into a shape the toolkit never produces. It covers every layout, the `_data/` files the
includes read, and the deep `_data/materials.yml` nesting the All Materials index recurses
over.

Build it locally the way CI does:

```bash
bundle exec jekyll build --config _config.yml,tests/fixture/_config.yml
```

Refresh it after a change to what the toolkit generates:

```bash
python3 tests/refresh-fixture.py   # needs `gh` authenticated
```

Consuming sites pull this theme with `remote_theme:`, which takes only `_layouts`,
`_includes`, `_sass` and `assets` - so nothing under `tests/` reaches them.
