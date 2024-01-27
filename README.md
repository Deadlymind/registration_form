# registration_form
>
> # Django Registration Form

<!-- ![Project Image](https://raw.githubusercontent.com/Deadlymind/registration_form/main/readme_image.png) -->

<!-- [![Project Video](src/readme_image.png)](src/Recording.mp4) -->



[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Django Version](https://img.shields.io/badge/Django-4.2-blue.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![JavaScript Version](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)](https://www.javascript.com/)
[![HTML Version](https://img.shields.io/badge/HTML-5-orange.svg)](https://html.spec.whatwg.org/multipage/)
[![CSS Version](https://img.shields.io/badge/CSS-3-blue.svg)](https://www.w3.org/Style/CSS/)

![Project Image](https://raw.githubusercontent.com/Deadlymind/registration_form/main/readme_image.png)

> A simple Django registration form with email notification.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User-friendly registration form.
- Email notification for new registrations.
- Basic success page.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Deadlymind/registration_form.git
   ```
2. Navigate to the project directory:
```bash
    cd registration_form
```

3. Create a virtual environment (optional but recommended):
```bash
    python -m venv venv
```

4. Activate the virtual environment:

- On Windows:
```
    .\venv\Scripts\activate
```

- On Linux/macOS:
```bash
    source venv/bin/activate
```

5. Install dependencies:
```bash
    pip install -r requirements.txt
```
6. Apply migrations:
```bash
    python manage.py migrate
```
7. Run the development server:
```bash
    python manage.py runserver
```

## Usage
Open your web browser and go to http://127.0.0.1:8000/registration/.
Fill out the registration form and submit.
Check your email for a notification about the new registration.

## Configuration
Email Settings
In the project/settings.py file, configure the following settings:

<pre>
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='your-email@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='your-email-password')
</pre>
Make sure to replace 'your-email@gmail.com' and 'your-email-password' with your actual Gmail credentials. It's recommended to use environment variables or a configuration file for sensitive information.

## Contributing

If you'd like to contribute, please fork the repository and create a new branch. Pull requests are welcome.

## License

This project is open source. 

zzzz
