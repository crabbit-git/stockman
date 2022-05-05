# Stockman

## What's this then?

Rome wasn't built in a day, but let's find out if I can build a somewhat functional inventory management web application in a week while also doing the ol' day job.

I have a few implementation-specific ideas that will probably require quite a bit of time to put into effect and would potentially make the application less viable as an "off the shelf" product for different use cases, so I will likely not go into those to begin with. For now, this will be extremely stripped down until it's up and running, then I will start to explore some smallish tweaks here and there to add some "nice to have" functionality as time permits. Some of these "nice to have" features will be built into the planning stage from the outset but will be visually highlighted to indicate that they may not end up in the initial version of the end result. It's possible (perhaps even rather likely) that I may think of some other bits and bobs later on, in which case I might expand on the functionality on the fly once the core application is working as intended.

This heavily relies upon the [Flask](https://palletsprojects.com/p/flask/) web framework and [jinja2](https://palletsprojects.com/p/jinja/) HTML templating. It uses [Psycopg](https://www.psycopg.org/) to allow [PostgreSQL](https://www.postgresql.org/) database syntax to be accessible to a [Python](https://www.python.org/) front end.

Also, no, this has no formal licence yet but if I actually end up investing significant time in it to the extent that I may ultimately use it myself, that might change. Until then, this is copyright me 2022 pls do not steal xoxoxox (I don't know why you'd want to anyway, it'll be extremely jank). Obviously if you do clone this repo for whatever reason, its contents are provided with bugger all liability, warranty, or guarantee of functionality whatsoever, because I'm a mere student of software development at this point and am incredibly likely to break stuff; if by some freak accident it breaks your computer and ruins your life, don't blame me. OK? OK.


## The Brief

We were given a set of four possible project brief to choose from. The one I chose was as follows:

> Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

The full version of the brief is in `task.md` for the curious.


## How do I use it, though?

The simplest way is probably to access it via the [Flask](https://palletsprojects.com/p/flask/) web framework, which will let you map a port on your local machine ("localhost", usually IP 127.0.0.1, the port by default being 5000) on which you can access the contents of the repo. There is a `.flaskenv` file in the root to configure the runtime environment for Flask, but if you know what you're doing and would rather override that very rudimentary configuration, go for it. In any case, install Flask if you don't already have it installed.

You're also going to need something that can manage SQL databases; the one I used was [PostgreSQL](https://www.postgresql.org/), so that'd be a solid choice. It's also the only one I'm going to provide basic instructions for, so bear that in mind.

To allow the Python code to interface with PSQL, you're also going to need to install [Psycopg](https://www.psycopg.org/). You won't be directly calling it once it's installed, but the code requires it to work.

Obviously, you're going to need the actual contents of this repository, so either clone the repository to some directory on your local machine (e.g. either with [Git](https://git-scm.com/) using `git clone`) or access it from the GitHub website and click on `Code` then `Download ZIP` and unzip the contents to a directory of your choosing.

With all the files ready to go, open a terminal window and run the PostgreSQL command `createdb stockroom` to create an empty database. You'll then need to populate the database with the appropriate tables. If you want to put data in yourself, either by running a big batch SQL `INSERT INTO` script or by adding things one by one in the web interface, you just need the tables to start off empty, so navigate to the root directory you plonked the files from this repository into and run `psql -d stockroom -f db/stockroom_empty.sql`. If you would prefer to have a muck about with some sample data to begin with, instead do `psql -d stockroom -f db/stockroom_filled.sql`. If you're more of a command line type, you can run `python console.py` (or `python3 console.py` if you have more than one Python version installed) after creating the tables with `psql -d stockroom -f db/stockroom_empty.sql` to have a mess around with the sample data in a terminal window.

Once your database is set up with at least tables (and some contents if you like), run Flask with from the repository's root directory with `flask run` to map the contents of the repository to a port to make it available to web browsers on your system. Once that's done, open a browser and navigate to the address shown in the terminal window when you ran Flask, which by default should be `localhost:5000` and/or `127.0.1.1:5000`. You can access the web interface of the application from there.
