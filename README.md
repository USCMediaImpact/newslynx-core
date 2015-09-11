[![travis-img](https://travis-ci.org/newslynx/newslynx-core.svg)](https://travis-ci.org/newslynx/newslynx-core)
# newslynx-core

NewsLynx Core is an expandable open-source toolkit for building modular content analytics workflows. It provides a fully RESTful API as well as a comprehensive `python` client and command line interface.

NewsLynx Core was built to power [`newslynx-app`](http://github.com/newslynx/newslynx-app) but is capable of powering a diverse range of potential applications, as well, including:

* A Mention.net-like pipeline for your personal or company blog.
* A Flexible timeseries store for content metrics which will automatically summarize and compare your data, as well as enable the additional of custom, computed metrics.
* A framework for configuring, scheduling, and monitoring arbitrary ``python`` jobs via API.
* A content-extraction API. 

## Installation

For most applications, refer to our [installation guide](http://newslynx.readthedocs.org/en/latest/install.html). If you'd like to setup a development environment, following the instructions below for MacOS X.  If you'd like to spin up a Virtual Machine, check out our [automation guide](https://github.com/newslynx/automation).

### Dependencies

#### Postgres

**NOTE** We recommend using [Postgres APP](http://postgresapp.com/). However, if you prefer the `brew` distribution, make sure to install it with plpythonu.

```
$ brew install postgresql --build-from-source --with-python
```

(Re)create a `postgresql` database

```shell
# If you already have a database called `newslynx`, delete it first
$ dropdb newslynx 
$ createdb newslynx
````

#### Redis

Install `redis`:

```shell
$ brew install redis
```

Open another tab in your shell and run:

```
$ redis-server
```

### Installation / Initialization 

**NOTE** we recommend that you install `newslynx` in a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

First clone this repository and move into it's root directory

```shell
$ git clone https://github.com/newslynx/newslynx-core.git
$ cd newslynx-core
```

**OPTIONAL**
Set your [configuration](http://newslynx.readthedocs.org/en/latest/config.html). If you don't do this, we will fallback on the [app's default configuration file](newslynx/app/config.yaml).


#### Initialize the database, super user, and install default sous chefs, tags, and recipes.

Run this command when working with `newslynx-app` 

```shell
$ make app_install
```

#### Initialize a bare install.
**[Expert mode]**  don't install the app's default sous chefs, tags, or recipes.

```
$ make bare_install 
```

#### Start the server

- In debug mode: `newslynx debug`
- Debug mode with errors: `newslynx debug --raise-errors`
- Production `gunicorn` server: `bin/run`

#### Start the task workers

```
$ bin/start_workers
```

#### Stop the task workers

```
$ bin/stop_workers
```

#### Start the cron daemon
```
$ newslynx cron
```


## Testing

`newslynx` is a complicated applcation, to simplify testing...


## Makefile

This repository contains a `Makefile` which provides access to the following commands:

* `make clean`
	- clean out cruft generated by `pip`.

* `make clean_sc`
	- clean out cruft generated by `pip` in `~/.newslynx/sous-chefs`

* `make install` 
	- installs `newslynx`
	- will first uninstall `newslynx` if a version already exists.

* `make app_install`
	- Installs `newslynx`, initializes the Super User, and adds the Recipes, Tags, and Sous Chefs needed to run `newslynx-app`

* `make bare_install`
	- Installs `newslynx` and initializes the Super User

* `make test_install`
	- removes all files under `~/.newslynx`
	- runs `make app_install`
	- runs `pip install -r test-requirements.txt`

* `distribute`
	- creates a new version of `newslynx` on PyPI

## Docs

* [Configuration](http://newslynx.readthedocs.org/en/latest/config.html)
* [First steps](http://newslynx.readthedocs.org/en/latest/getting-started.html)
* [Understanding Sous Chefs](http://newslynx.readthedocs.org/en/latest/sous-chefs.html)
* [Understanding Recipes](http://newslynx.readthedocs.org/en/latest/recipes.html)
* [Understanding Metrics](http://newslynx.readthedocs.org/en/latest/metrics.html)
* [Understanding Tags](http://newslynx.readthedocs.org/en/latest/taxonomy.html)
* [Understanding Content](http://newslynx.readthedocs.org/en/latest/content-items.html)
* [Understanding Events](http://newslynx.readthedocs.org/en/latest/events.html)
* [Full API Reference](http://newslynx.readthedocs.org/en/latest/api.html)
* [Command Line Interface](http://newslynx.readthedocs.org/en/latest/cli.html)
* [Write your own Sous Chef](http://newslynx.readthedocs.org/en/latest/writing-sous-chefs.html)

## Application Structure


## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

