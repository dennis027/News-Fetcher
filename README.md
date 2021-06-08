# EAGLES NEWSHUB

> By: Dennis Kimani

> --------------------------------------------------------------------------------

> Project Name: Eagles NewsHub   



## Description

> This is an application that gives a list and preview news articles from various sources in the world.

## Specifications

> - Users are able to see various news sources and select the ones they prefer from the navbar where they hover and view diffrent sources.
> - Users are be able to see all the news articles from that news source in what they select.
> - The user can see the image description and time the news article was created.
> - The user can also be able to click on an article and redirected to the the news source.


## Setup/Installation Requirements

> - Link to deployed page: [Heroku](https://deman-magazine.herokuapp.com/)

### Running in Local Machine

 ## Prerequest
    * python3.6
    * pip 
    * virtual environment (venv)
 ## Clonning
    $ git clone https://github.com/dennis027/News-Fetcher.git
    $ cd News-Fetcher

 ## Creating the virtual environment

  $ python3.6 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python
 ## Installing Flask and other Modules

  $ python3.6 -m pip install Flask
  $ python3.6 -m pip install Flask-Bootstrap
  $ python3.6 -m pip install Flask-Script
 ## Setting up the API Key

  To be able to gather article info from the News API you will need an API Key.

  * Visit https://newsapi.org/ and register for an API key.
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it:

          export NEWS_API_KEY='<Your-Api-Key>'
          python3.6 manage.py server

  * Insert the API Key you received from News Api where <Your-Api-Key> is.
 ## To run the application, in your terminal:

  $ chmod +x start.sh
  $ ./start.sh




## Technologies used

> - astroid==1.6.1
> - click==6.7
> - colorama==0.3.9
> - dominate==2.3.1
> - Flask==0.12.2
> - Flask-Bootstrap==3.3.7.1
> - Flask-Script==2.0.6
> - gunicorn==19.7.1
> - isort==4.2.15
> - itsdangerous==0.24
> - Jinja2==2.10
> - lazy-object-proxy==1.3.1
> - MarkupSafe==1.0
> - mccabe==0.6.1
> - pylint==1.8.2
> - six==1.11.0
> - visitor==0.1.3
> - Werkzeug==0.14.1
> - wrapt==1.10.11


## Support and contact details

> - Email Address: machariad196@gmail.com
> - Contact - +254799157137

## License and terms of use

> - [MIT License](license) this application's source code is free for any open source projects

## Aknowledgements
* Ken Gathaiga
* Francis Kipchumba
