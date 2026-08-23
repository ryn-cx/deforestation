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

A detail page only carries the first 24 episodes of a season and lists a token
for every page of them, so the rest are fetched through `detail_widgets`.
