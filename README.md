# Tweet and Treat

Tweet and Treat is my first attempt at using both Python and the Django framework in a web application.  The concept is aimed at business owners who want to leverage the power of Twitter by offering short-term promotions (lasting ~3 hours) by tweeting the promotion at all public and recently active Twitter users within a 1 mile radius of their business.

## Technology Stack

New: Python, Django, Twitter::Streaming API, Geocoding (ie. Geopy)

Previously Worked with: HTML5, CSS3, Databases (SQLite3 for prototyping, PostGRES for production), OAuth Twitter REST API

## Minimum Viable Product

A single-page application that takes an address (of the business) and a deal to offer.  

Once submitted, a Twitter Streaming API client is activated and filtered to a radius of 1 mile of the business' address.

As tweets come in that allow location data to be attached, a direct message is then sent to each twitter handle with the deal from the business

The user can redeem the promo by simply showing up with the tweet, reflecting the time and, confirming the validity of the promo offer.

# Coding Process: Thoughts and Reflections

## :) Great Triumphs and Achievements

1.) Getting set up with Python and the Django environment on my machine was alone a daunting task.  When I starting coding at DBC in Ruby, one of the instructors held a session to help install software for development.  I literally gave him my computer and he worked his Linux magic.  I had no idea what he was doing at the time.  Now, installing the necessary components to get up and running with a new language and framework on my own was a great way to start the project.

2.) MVT: MVC is not MVT.  In terms of learning, it helps to compare one to another and find their similarities, but I found a great article that talks in depth about why we shouldn't see them as twins.

MORE TO COME>>.

## :( Failures: My Opportunities to Learn

1.) Virtualenv:  Learning Ruby can make you spoiled.  There is really sweet gem called 'bundle' and it basically takes care of any dependency issues you could run into with different plugins.  You can specify which versions of plugins you want to from project to project and it takes care of the rest.  With Python it's a little different.

2.) ModelForms: Just like Rails they do a ton of background work, but there are quirks.  Learning to combine them with multiple models was one that I encountered.  I believe the answer lies in inline forms but I found a workaround that was able to successfully write to the database.  

MORE TO COME>>.

## Things to do differently next time....

1.) I am doing this project in a text editor.  Its Sublime Text 2, and its what is comfortable with me, but the more and more I read, on the next project I will use an IDE like PyCharm or PyDev.

# Bugs and Issues
