Title: Ajiaco ORM
Date: 2019-07-08 17:35
Modified: 2019-07-08 17:35
Category: Python
Tags: orm, python, ajiaco, sqlalchemy
Slug: ajiaco_orm
Summary: Design notes about the Ajiaco ORM

Several years ago i was luckily part of the team that design and developed
one of the current de facto standard frameworks for experimental economy:
oTree ([http://otree.org](http://otree.org)); and was a significant
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

oTree is awesome, I already made ~12 experiments with this package, so i need to explain
why I decided to start new paralel project.

1. **Many languages:** oTree is written in Python, thats fine; it's easy, expressive, and with a big community of programmers. So if you want to create an experiment, most of your logic will be written in this language. In other hand, the templates/pages are coded in [HTML](https://en.wikipedia.org/wiki/HTML) (With the [Django-Templates language](https://docs.djangoproject.com/en/2.2/ref/templates/language/)); if you want more interactive templates and custom styles you will ended needing [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) and [Javascript](https://en.wikipedia.org/wiki/JavaScript). In the end, you will need 4 languages to create a moderate complex programs.

2. **Lack of customization:** In many cases, Django is the best out-of-the-box option for develop
anything web-related with Python. But when you try to create your own workflow, maybe you have a problem.

     The main idea of chosen any [framework](https://en.wikipedia.org/wiki/Software_framework), is to avoid to design a your own workflow; the problem starts when you try to design your own framework on top of another one. In other other words: you are trying to design your own *flexible-for-your-use-case-workflow* on top of another *flexible-for-another-more-general-use-case-workflow*.

     Check this talk [Niklas Meinzer - When Django is too bloated - Specialized Web-Applications with Werkzeug](https://www.youtube.com/watch?v=mXpBuELtpro), for another people with the same problem.


3. **Experimental features:** Implement  experimental features is necessary to any projects to live a long and happy life (imagine a
     parallel universe where a new web version of zTree are launched before oTree).

     All the efforts of the oTree community related to new features are to made a the project most simple to use for non-programmers (oTree studio and oTree Hub). I was a little skeptical about to try to remove the code of the process of making code. Normally you create empty shells will you still need to fill with code.

     In other hand, implement experimental features like artificial intelligence powered bots, can be a challenge, mostly because the rigid Synchronous Django-Layer bellow, and the lack of interest or man-power of their community.

4. **Classes everywhere:** In january of 2018 I give a full tutorial of Python + oTree in the
     [Bogotá Experimental Economics Workshop](https://www.urosario.edu.co/BEEC-2018/Evento/). Mostly of the contents was easy to explain, except for one concept: **Classes**, object oriented software are useful mostly for the encapsulation property, and in particular for the [MVC pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). But explain to a non programmer concepts like inheritance, methods, instantiation and state; was the difficult part.

     Django define their entire workflow with classes (models, views, management commands and middlewares), and this permeates the design of oTree. In most cases the user only want to define simple sequential commands, but still they need to define a class (with the proper methods and inheritance).

5.  **Page driven development:** This is the hard one. oTree (and z-Tree) are defined by their pages/stages, not by their subjects. In
    other words, most of the rules of the game are written inside the pages logic, and Subject/Player only consumes this the data generated for this logic and store it in the database. Even if we think the subjects/players from the [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) sugested by oTree, the behavior of the players are still dictated from the data injected by the page.

    Why this is important? Maybe, you want to create some facility to provide a way to implement *bots vs human* games, but in this case, yo must mix the logic of the bots, and the real players on the page. Remember: all behavior of the experiment are generated in the page.

    This is a limitation of the MVC pattern.

Avoid this 5 points (or at least try to) is my main goal as a designer of a more modern approach to create behavioral experiments.


## Designing a new framework


## The Database abstraction layer

### How i imagine want to use the ORM

```python
# lets asume we have some kind of game
game.subjects.fields(
    name=str, age=int, money=game.Money)

```

```python
game.define_data(
    subjects={
        "name": str,
        "age": int,
        "height": float},

    rounds={},

    groups={},

    roles={}
)

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
