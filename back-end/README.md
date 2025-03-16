# Weather Alert App (Backend)

## Description

This is the backend for the **Weather Alert App**. It handles weather data fetching, user alert management, and notifications. The app allows users to set weather-related alerts for their location and get notified when conditions match their preferences.

## Features

- **Weather Data Fetching**: Retrieves real-time weather data from external APIs (e.g., OpenWeatherMap).
- **User Alerts**: Allows users to set alerts for specific weather conditions (e.g., temperature, rain).
- **Notifications**: Sends notifications to users when their set weather conditions are met.
- **Authentication**: Secure user authentication using JWT (JSON Web Tokens).
  
## Technologies Used

- **Node.js**: JavaScript runtime for server-side logic.
- **Express.js**: Web framework for building the API.
- **MongoDB** (or another DB): Database for storing user and alert data.
- **Mongoose**: ODM (Object Data Modeling) library for MongoDB.
- **JWT**: JSON Web Tokens for user authentication.
- **Axios**: For making HTTP requests to the weather API.
- **Nodemailer** (or another service): For sending email notifications.

## Installation

To run the backend locally:

Clone the repository:
   ```bash
   git clone https://github.com/IZEREDukundane/weather-alert-app.git
