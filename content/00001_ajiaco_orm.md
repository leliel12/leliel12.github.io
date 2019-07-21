Title: Ajiaco ORM
Date: 2019-07-08 17:35
Modified: 2019-07-08 17:35
Category: Python
Tags: orm, python, ajiaco, sqlalchemy
Slug: ajiaco_orm
Summary: Design notes about the Ajiaco ORM

Several years ago i was luckily part of the team that design and developed
one of the current de facto standard frameworks for experimental economy:
oTree (http://otree.org); and was a significant
advancement over the old [z-Tree](https://www.ztree.uzh.ch/en.html)

The project is web-framework developed on top of [Django](https://www.djangoproject.com/), that
implement a custom set of objects (Model, views and templates) and functions, to facilitate
the creation of:

- Multiplayer strategy games.
- Controlled behavioral experiments.
- Survey and quizzes.

Let's be honest: oTree is a **REALLY good project**, and very active. The last
companion application [oTree Studio](https://otree.readthedocs.io/en/latest/tutorial/part0_studio.html#tutorial-studio)  (part of [oTree hub](https://www.otreehub.co)) is a must;
their community is really active in their [forum](https://groups.google.com/forum/#!forum/otree), and several experiments was released (and published) with the tool ([oTree Citations](https://scholar.google.com/scholar?cites=5704587714172176698&as_sdt=2005&sciodt=0,5&hl=es))

## Critisism?

oTree is awesome, myself made something like ~12 experiments with the project, so i need to explain
why I decided to start new .

1. **Many languages:** oTree is written in Python, thats fine; it's easy, expressive, and with a big community of programmers. So if you want to create an experiment, most of your logic will be written in this language. In other hand, the templates/pages are coded in HTML (With the Django-Templates language)); if you want more interactive templates and custom styles you will ended needing CSS and Javascript. In the end, you will

2. **Django Hack:**

3. **Lack of customization:**

4. **Experimental features:**

5. **Classes everywhere:**



### How i imagine want to use the ORM

```python
# lets asume we have some kind of game
game.user.add_fields(
    name=str, age=int, money=game.Money)

```

### 1. Mapping Python types to SQLAlchemy column types


### 2. The Model super-class


#### 2.5 Custom models


### 3. The Database class

```python

import decimal as decimal

from ajiaco import Database, Model


db = db.Storage("sqlite:///")

db.create_model(
    name="User",
    base_model=Model,
    fields={"name": str, "age": int, money: dec.Decimal})
```

### 4. Transactions
