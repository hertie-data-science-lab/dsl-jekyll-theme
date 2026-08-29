# Fixture site

`fixture/` is a small consuming site, used by `.github/workflows/pr-build.yml` to build
this theme on every PR. Building the theme repo alone proves nothing: it has no pages, so
no layout and no include is ever rendered.

It covers what this theme owns - the `default`, `page` and `post` layouts, the head,
header, nav and footer, and the whole stylesheet. It sets `title` rather than
`course_name`, and no semester, because that is the shape a non-course consumer has and
the shape the chrome's fallbacks are for.

The COURSE-specific layouts and includes are no longer here: they live in
[`dsl-teaching-toolkit`](https://github.com/hertie-data-science-lab/dsl-teaching-toolkit)
under `templates/site/`, which writes them into each site and builds its own fixture
cohort site with Jekyll on every PR.

Build it locally the way CI does:

```bash
bundle exec jekyll build --config _config.yml,tests/fixture/_config.yml
```
