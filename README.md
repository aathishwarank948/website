# Ex.07 Restaurant Website
# Date:1.10.2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
```
base.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Restaurant</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #f8ffae 0%, #43c6ac 100%);
            min-height: 100vh;
            cursor: url('https://cdn.jsdelivr.net/gh/berlin449/cursors/cursor-star.png'), auto;
            transition: background 0.5s;
        }
        .navbar {
            background: linear-gradient(90deg, #ff6a00 0%, #ee0979 100%);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border-radius: 0 0 20px 20px;
            animation: navFadeIn 1s;
        }
        @keyframes navFadeIn {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .navbar-brand, .nav-link {
            color: #fff !important;
            font-weight: bold;
            font-size: 1.2rem;
            letter-spacing: 1px;
            transition: color 0.3s, background 0.3s;
        }
        .nav-link:hover {
            color: #ffeb3b !important;
            background: rgba(255,255,255,0.1);
            border-radius: 8px;
        }
        .navbar-nav {
            flex-direction: row;
        }
        .banner {
            background: url('/static/webapp/banner.jpg') center/cover no-repeat;
            height: 320px;
            border-radius: 0 0 30px 30px;
            box-shadow: 0 8px 24px rgba(238,9,121,0.15);
            position: relative;
            overflow: hidden;
        }
        .banner::after {
            content: '';
            position: absolute;
            left: 0; top: 0; width: 100%; height: 100%;
            background: linear-gradient(90deg, rgba(255,106,0,0.3), rgba(238,9,121,0.3));
        }
        .footer {
            background: linear-gradient(90deg, #ee0979 0%, #ff6a00 100%);
            color: #fff;
            padding: 20px 0;
            text-align: center;
            font-size: 1.1rem;
            letter-spacing: 1px;
            border-radius: 20px 20px 0 0;
            box-shadow: 0 -4px 12px rgba(0,0,0,0.08);
        }
        /* Button Glow Effect */
        .btn-glow {
            background: linear-gradient(90deg, #43c6ac 0%, #f8ffae 100%);
            color: #ee0979;
            font-weight: bold;
            box-shadow: 0 0 12px #ee0979;
            border: none;
            transition: box-shadow 0.3s, background 0.3s;
        }
        .btn-glow:hover {
            box-shadow: 0 0 24px #ff6a00;
            background: linear-gradient(90deg, #ee0979 0%, #ff6a00 100%);
            color: #fff;
        }
        /* Cursor trail effect */
        .trail {
            position: fixed;
            pointer-events: none;
            width: 20px; height: 20px;
            border-radius: 50%;
            background: radial-gradient(circle, #ee0979 60%, #ff6a00 100%);
            opacity: 0.7;
            z-index: 9999;
            animation: trailFade 0.7s forwards;
        }
        @keyframes trailFade {
            to { opacity: 0; transform: scale(2); }
        }
    </style>
    <script>
    // Cursor trail effect
    document.addEventListener('mousemove', function(e) {
        var trail = document.createElement('div');
        trail.className = 'trail';
        trail.style.left = (e.pageX - 10) + 'px';
        trail.style.top = (e.pageY - 10) + 'px';
        document.body.appendChild(trail);
        setTimeout(function() { trail.remove(); }, 700);
    });
    </script>
</head>
<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="/">My Restaurant</a>
            <div>
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/menu/">Menu</a>
                <a class="nav-link" href="/administration/">Administration</a>
                <a class="nav-link" href="/contact/">Contact Us</a>
            </div>
        </div>
    </nav>
    {% block content %}{% endblock %}
    <div class="footer">
        &copy; 2025 Thalapamatti| Designed by Aathishwaran K
    </div>
</body>
</html>

home.html

{% extends 'webapp/base.html' %}
{% block content %}
<div class="banner"></div>
<div class="container mt-5 text-center">
    <h1 class="display-4" style="color:#ee0979; text-shadow: 2px 2px 8px #ff6a00; animation: pulse 1.5s infinite alternate;">Welcome to My Restaurant</h1>
    <p class="lead" style="color:#43c6ac; font-size:1.5rem;">Experience the <span style="color:#ff6a00; font-weight:bold;">best cuisine</span> in town!</p>
    <a href="/menu/" class="btn btn-lg btn-glow mt-3"><i class="fas fa-utensils"></i> View Menu</a>
</div>
<style>
@keyframes pulse {
    to { text-shadow: 4px 4px 16px #43c6ac; color: #ff6a00; }
}
</style>
{% endblock %}

menu.html

{% extends 'webapp/base.html' %}
{% block content %}
<div class="container mt-5">
    <h2 class="mb-4" style="color:#ee0979; text-shadow: 2px 2px 8px #43c6ac;">Our Menu</h2>
    <div class="row">
        {% for item in food_items %}
        <div class="col-md-3 mb-4">
            <div class="card h-100 food-card" style="border-radius:18px; box-shadow:0 4px 16px #ee097933; transition:transform 0.3s;">
                <img src="{{ item.image }}" class="card-img-top" alt="{{ item.name }}" style="border-radius:18px 18px 0 0; height:180px; object-fit:cover;">
                <div class="card-body text-center">
                    <h5 class="card-title" style="color:#ff6a00; font-weight:bold;">{{ item.name }}</h5>
                    <p class="card-text" style="color:#43c6ac;">{{ item.description }}</p>
                    <span class="badge bg-warning text-dark" style="font-size:1.1rem;">Rs{{ item.price }}</span>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
<style>
.food-card:hover {
    transform: scale(1.05) rotate(-2deg);
    box-shadow: 0 8px 32px #ff6a00aa;
    border: 2px solid #ee0979;
}
</style>
{% endblock %}

administration.html

{% extends 'webapp/base.html' %}
{% block content %}
<div class="container mt-5">
    <h2 class="mb-4" style="color:#43c6ac; text-shadow: 2px 2px 8px #ee0979;">Administration</h2>
    <div class="row">
        {% for admin in admins %}
        <div class="col-md-4 mb-4">
            <div class="card h-100 text-center admin-card" style="border-radius:18px; box-shadow:0 4px 16px #43c6ac33; transition:transform 0.3s;">
                <img src="{{ admin.photo }}" class="card-img-top rounded-circle mx-auto mt-3" style="width:120px;height:120px; border:4px solid #ee0979;" alt="{{ admin.name }}">
                <div class="card-body">
                    <h5 class="card-title" style="color:#ff6a00; font-weight:bold;">{{ admin.name }}</h5>
                    <p class="card-text" style="color:#43c6ac;">{{ admin.designation }}</p>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
<style>
.admin-card:hover {
    transform: scale(1.05) rotate(2deg);
    box-shadow: 0 8px 32px #43c6acaa;
    border: 2px solid #ff6a00;
}
</style>
{% endblock %}

contact.html

{% extends 'webapp/base.html' %}
{% block content %}
<div class="container mt-5">
    <h2 class="mb-4" style="color:#ff6a00; text-shadow: 2px 2px 8px #ee0979;">Contact Us</h2>
    <div class="card p-4" style="border-radius:18px; box-shadow:0 4px 16px #ff6a0033; background: linear-gradient(135deg, #f8ffae 0%, #43c6ac 100%);">
        <h5 style="color:#ee0979;"><i class="fas fa-map-marker-alt"></i> Address:</h5>
        <p style="color:#43c6ac; font-weight:bold;">{{ contact.address }}</p>
        <h5 style="color:#ee0979;"><i class="fas fa-phone"></i> Phone:</h5>
        <p style="color:#43c6ac; font-weight:bold;">{{ contact.phone }}</p>
        <h5 style="color:#ee0979;"><i class="fas fa-envelope"></i> Email:</h5>
        <p style="color:#43c6ac; font-weight:bold;">{{ contact.email }}</p>
    </div>
</div>
{% endblock %}

# OUTPUT:
website/Screenshot 2025-10-01 225705.png

# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
