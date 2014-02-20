Uptown Saturday Night
=========
[uptown-prototype.appspot.com](http://uptown-prototype.appspot.com/)

Setting Up
-----------
* Download and Install [Python 2.7](http://www.python.org/download/releases/2.7/)
* Download and Install [GAE Python SDK](https://developers.google.com/appengine/downloads)
* Download and Install [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git)
* Checkout this repository ```git clone https://github.com/theMagicalKarp/uptown-prototype.git uptown```
* Start GAE SDK and select this project.

Libraries Used
-----------
* [Flask](http://flask.pocoo.org/) *URL Routing*
* [Jinja2](http://jinja.pocoo.org/) *HTML templating*
* [Bootstrap](http://getbootstrap.com/) *HTML Styling*
* [jQuery](http://jquery.com/) *Wrapper for JavaScript... Also required for bootstrap... D:*

What's Going On?!
-----------
[__/app.yaml:__](https://github.com/theMagicalKarp/uptown-prototype/blob/master/app.yaml) Basic config that Google App Engine uses to understands how to run our application. This is the first thing ran when starting the server.

[__/libs/:__](https://github.com/theMagicalKarp/uptown-prototype/tree/master/libs) Contains external python libraries such as Flask, werkzeug, ect...

[__/app/views.py:__](https://github.com/theMagicalKarp/uptown-prototype/blob/master/app/views.py) Contains instructions of how to map our application to specific urls. For example this [http://uptown-prototype.appspot.com/bootstrap](http://uptown-prototype.appspot.com/bootstrap) is generated from this
```python
@blueprint.route('/bootstrap', methods=['GET'])
def bootstrap():
    return render_template('bootstrap_examples.html')
```

[__/app/models/students.py:__](https://github.com/theMagicalKarp/uptown-prototype/blob/master/app/models/student.py) This holds information on how our student objects should be stored in the database.
