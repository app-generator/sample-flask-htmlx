# [Flask HTMLx Sample](https://blog.appseed.us/flask-and-htmlx-open-source-sample/)

Open-Source sample that uses **[Flask and HTMLx](https://blog.appseed.us/flask-and-htmlx-open-source-sample/)** for the frontend logic. For newcomers, `Flask` is a leading web framework powered by Python and `HTMLx` is a lightweight JS utility library that allows accessing AJAX, CSS Transitions, WebSockets, and Server-Sent Events directly in HTML. 

<br />

> **Features**

- `Up-to-date` Dependencies
- Tech Stack:
  - `Flask`: manages authentication and routing
  - `HTMLx`: manages forms submit (no JS)
- `Auth`: Sign IN, Sign UP
- `Misc`: SQLite DB, SQLAlchemy, Forms Validation

<br />

> **Links**

- 👉 More [Flask Apps](https://appseed.us/apps/flask/) and [Dashboards](https://appseed.us/admin-dashboards/flask/) provided by AppSeed
- 👉 Free [Support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup).

<br />

![Flask HTMLx Sample - Open-Source Sample provided by AppSeed](https://user-images.githubusercontent.com/51070104/166150793-a2027357-a9fb-4c0d-b024-ee9d9e0e071b.gif)

<br />

## ✨ **Prerequisites** 

To get started with the application in the machine

- `Python3` - Make sure python3 and highr=er is installed on your system before proceeding to installation instructions.
- `Git` - Download and install Git.OSX and linux comes preinstalled with Git. Download and install Git in your windows machine if not installed yet.
- `Pip` - We will use pip to install required packages to be used in the project. 

<br />

## ✨ **Installation**

> 👉 Step 1 - **Cloning the repository.**

```bash
$ git clone git@github.com:app-generator/sample-flask-htmlx.git 
// OR via HTTPS
$ git clone https://github.com/app-generator/sample-flask-htmlx.git
```

<br />

> 👉 Step 2 - **Prepare Environment** (create virtual environment)

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> 👉 Step 3 - **Install Dependencies**

```bash
$ # Install requirements
$ pip3 install -r requirements.txt
```

<br />

> 👉 Step 4 - **Create Database**

```bash
$ flask shell    # launch Flask Shell
>>> 
>>> from app import db
>>> db.create_all()
```

<br />

> 👉 Step 4 - **Create Database**

```bash
$ flask run
```

<br />

> 👉 Step 5 - **Start the APP**

```bash
$ flask run
```

The app should be up & running on address `http://localhost:5000`

<br />

## ✨ **HTMLx** 

All forms managed by the app use HTMLx directives. Here is the Login Form Source Code and used HTMLx directives: 

- [hx-swap](https://htmx.org/attributes/hx-swap/)  
- [hx-post](https://htmx.org/attributes/hx-post/) 
- [hx-target](https://htmx.org/attributes/hx-target/)

<br />

```html
    <form  hx-swap="outerHTML" 
           hx-post="{{ url_for('auth.signin') }}" 
           hx-push-url="true" 
           hx-target=".content" 
           class="p-5 bg-white shadow mh-100 col-sm-8 col-md-6 col-lg-4" novalidate >
        
        <p class="h3 text-center p-2">SignIn</p>
        
        <!-- Truncated content -->

        <div class="form-input p-1">
            {{form.email.label}}
            {{form.email(class_="form-control")}}
        </div>

        <div class="form-input p-1">
            {{form.password.label}}
            {{form.password(class_="form-control")}}
        </div>

        <button class="btn p-2 px-3 rounded btn-primary h1" type="submit">Sign In</button>
    </form>
```        

<br />

---
**[Flask HTMLx Sample](https://blog.appseed.us/flask-and-htmlx-open-source-sample/)** - Open-Source Sample provided by [AppSeed](https://appseed.us)
