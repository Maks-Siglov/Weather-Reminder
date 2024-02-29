# Your Personal Weather Reminder
Welcome to WeatherReminder, your go-to solution for staying updated on the weather conditions in your favorite cities. With WeatherReminder, you can effortlessly register, subscribe to cities, and receive personalized weather notifications via email, all tailored to your preferred notification period.


## Getting Started

Clone the Repository:

```bash
git clone https://github.com/Maks-Siglov/Weather-Reminder.git
cd Weather-Reminder/
```

## Start With Docker


1. Establish docker user

    ```bash
      source env.sh
     ```

2. Create docker network

    ```bash
      docker network create mynetwork  
     ```

3. Start services 
    ```bash
      docker compose up  
     ```

4. Now you can log in as admin
   - **Email:** admin@gmail.com
   - **Password:** 336611qq 

5. See Enable Extended Functionality for enable sending email notification

## Run Locally

1. Install dependencies:

    ```bash
    pip install -r requirements/prod.txt -r requirements/dev.txt
    ```

2. Create postgres db and place data to the .env file:
    - **Example data in .env:**
    ```bash
    DB_NAME='weather_reminder'
    DB_USER='admin'
    DB_PASSWORD='admin'
    DB_HOST='localhost'
    DB_PORT=5432
    ```

3. Apply migrations:

    ```bash
    cd weather_reminder/
    python manage.py migrate
    ```

4. Load Dumpdata:

    ```bash
    python manage.py loaddata fixtures/dumpdata.json
    ```

5. Superuser:

   - **Create a Superuser:**
     ```bash
     python manage.py createsuperuser
     ```

   - **Or Login as the already created Admin:**
     - **Email:** admin@gmail.com
     - **Password:** 336611qq

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` and log in with your superuser account, start using WeatherReminder.

## Enable Extended Functionality

1. Project use email for sending reminder message. For using this feature add your email data in .env file
    - **Replace data in .env file**
     ```bash
    EMAIL_HOST='smtp.gmail.com /or another smtp'
    EMAIL_PORT=587
    EMAIL_HOST_USER='Replace with your email'
    EMAIL_HOST_PASSWORD='Replace with your app password'    
    ```
   
2. For getting weather data you need to Open Weather API key
    - **Replace data in .env file**
     ```bash
    OPEN_WEATHER_API_KEY='Place your Open Weather API key here'
    ```

## API Routes

### Authorization

##### Register:
- **Endpoint:** `/api/auth/v1/register/`
- **Method:** POST
- **Description:** Registration for a user. Request example:
```json
{
  "username": "test_username",
  "email": "some@gmail.com",
  "password": "2277744qq",
  "confirm_password": "2277744qq"
}
```

##### Login:
- **Endpoint:** `/api/auth/v1/login/`
- **Method:** POST
- **Description:** Login for a user. Request example:
```json
{
  "email": "some@gmail.com",
  "password": "2277744qq"
}
```


##### Logout:
- **Endpoint:** `/api/auth/v1/logout/`
- **Method:** POST
- **Description:** Logout for a user


### Subscription

##### Create:
- **Endpoint:** `/api/subscription/v1/create`
- **Method:** POST
- **Description:** Create subscription notification_period = 24 by default. Request example:
```json
{
  "user": 1,
  "city": "Kiev",
  "notification_period": 12
}
```

##### Edit:
- **Endpoint:** `/api/subscription/v1/<int:subscription_id>/edit`
- **Method:** PUT
- **Description:** Change subscription's notification_period . Request example:
```json
{
  "notification_period": 20
}
```

##### Delete:
- **Endpoint:** `/api/subscription/v1/<int:subscription_id>/delete`
- **Method:** DELETE
- **Description:** Delete subscription by id


##### Subscriptions List:
- **Endpoint:** `/api/subscription/v1/list/<str:username>`
- **Method:** GET
- **Description:** Return user's subscriptions


##### Disable subscription:
- **Endpoint:** `/api/subscription/v1/<int:subscription_id>/disable`
- **Method:** POST
- **Description:** Notifications will not be sent to the disabled subscription


##### Enable subscription:
- **Endpoint:** `/api/subscription/v1/<int:subscription_id>/enable`
- **Method:** POST
- **Description:** Enable disabled subscription


### Reminder

##### Get:
- **Endpoint:** `/api/weather-data/v1/get-subscription/`
- - **Method:** Get
- **Description:** Get subscription for notification:


##### Update:
- **Endpoint:** `/api/weather-data/v1/update-last-notification-time`
- - **Method:** POST
- **Description:** Update subscription last notification time


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
