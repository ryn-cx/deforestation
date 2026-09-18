# Deforestation

[Prime Video](https://www.amazon.com/gp/video/storefront) API wrapper built
using [Good Ass Pydantic
Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and [Get
Around](https://github.com/ryn-cx/get-around).

Nothing is authenticated and nothing is scraped out of markup: a page is asked
for as the JSON the site's own web player renders it from.

## Installation

```bash
uv add git+https://github.com/ryn-cx/deforestation
```

## Usage

Every endpoint is called to get its model, and `download()` and `load()` are the
halves of that.

```python
from deforestation import Deforestation

client = Deforestation()

detail = client.detail(title_id)
widgets = client.detail_widgets(title_id, widget_token)
search = client.search(query)
suggestions = client.search_suggestions(prefix)

downloaded = client.detail.download(title_id)
detail = client.detail.load(downloaded)
```

An endpoint answers with the essentials of what it was asked for, read out of
the response and flattened into one model:

```python
detail = client.detail(title_id)

detail.title, detail.synopsis, detail.release_year, detail.image_url
detail.genres, detail.cast, detail.maturity_rating, detail.imdb_rating
detail.included_with_prime, detail.purchasable, detail.channels
detail.seasons, detail.episodes, detail.episode_pages
```

A detail page only carries the first 24 episodes of a season and lists a token
for every page of them, so the rest are fetched through `detail_widgets`.

```python
for page in client.detail(season_id).episode_pages:
    if not page.is_selected:
        episodes = client.detail_widgets(season_id, page.token).episodes
```

A response is far larger than the parts that are kept, so it is read as the JSON
it was served as rather than through a model of the whole of it. The models are
still generated rather than written: every recorded response is written out as
what `parse.py` makes of it, and those files are what Good Ass Pydantic
Integrator builds `models.py` from.
