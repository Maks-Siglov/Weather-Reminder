# WeatherReminder: Your Personal Weather Reminder
Welcome to WeatherReminder, your go-to solution for staying updated on the weather conditions in your favorite cities. With WeatherReminder, you can effortlessly register, subscribe to cities, and receive personalized weather notifications via email, all tailored to your preferred notification period.


## Getting Started


### Installation
Clone the Repository:

1. Clone the repository:

    ```bash
    git clone https://git.foxminded.ua/foxstudent105590/task_16-django-weather-reminded.git
    cd task_16-django-weather-reminded/
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements/prod.txt -r requirements/dev.txt

    ```

3. Apply migrations:

    ```bash
    cd weather_reminder/
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Visit `http://127.0.0.1:8000/admin/` to log in with your superuser account and start using WeatherReminder.

### Enable extended functionality

1. Project use email for sending reminder message. For using this feature add your email data in .env file
    - **Replace data in .env file**
     ```bash
    EMAIL_HOST='smtp.gmail.com /or another smtp'
    EMAIL_PORT=587
    EMAIL_HOST_USER='Replace with your email'
    EMAIL_HOST_PASSWORD='Replace with your app password'    
    ```

## Usage

- Register an Account:
Create an account using your email and password to unlock all the features WeatherReminder has to offer.

- Log In:
Sign in to your WeatherReminder account to access your personalized dashboard.

- Subscribe to Cities:
Choose the cities you want to receive weather notifications for and subscribe to them.

- Stay Updated:
Sit back and relax as WeatherReminder delivers customized weather updates straight to your inbox at your preferred notification intervals.

- Manage Subscriptions:
Edit, delete, or disable your subscriptions as needed to ensure you're always in control of your weather preferences.

- Contributing
WeatherReminder is an open-source project, and we welcome contributions from the community. Whether it's fixing bugs, adding new features, or improving documentation, your help is greatly appreciated. Please submit a pull request or open an issue on GitHub to get started.
