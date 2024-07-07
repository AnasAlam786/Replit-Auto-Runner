# Repl.it Automation Script

This Python script uses Selenium to automate the process of checking and rerunning Repl.it instances. It is designed to maintain the uptime of specified Repl.it projects by periodically checking their status and restarting them if necessary.

## Features

- Uses Selenium to interact with Repl.it and Facebook login.
- Periodically checks the status of Repl.it instances.
- Automatically restarts instances that are paused or unavailable.

## Requirements

- Python 3.6+
- Google Chrome browser
- ChromeDriver
- Selenium
- Pickle file containing Facebook cookies

## Installation

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    ```

2. **Navigate to the project directory:**

    ```sh
    cd repl-it-automation
    ```

3. **Install the required Python packages:**

    ```sh
    pip install selenium
    ```

4. **Download ChromeDriver:**

    Ensure that the ChromeDriver version matches your installed version of Google Chrome. You can download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

5. **Create a `cookies.pkl` file:**

    - Manually log in to Facebook using a browser.
    - Extract cookies using browser developer tools or a browser extension.
    - Save the cookies in a `cookies.pkl` file.

## Usage

1. **Run the script:**

    ```sh
    python script.py
    ```

    The script will open a Chrome browser, navigate to Facebook to log in using cookies, and then navigate to Repl.it to start the monitoring and rerunning process.

2. **Script flow:**

    - The script will first load Facebook cookies to bypass the login process.
    - It will then navigate to the Repl.it login page and initiate the login process.
    - The script will periodically check the status of Repl.it instances and restart them if necessary.

## File Structure

- `script.py`: The main script containing the automation logic.
- `cookies.pkl`: Pickle file containing Facebook cookies for authentication.

## Notes

- Ensure that the `cookies.pkl` file is up-to-date and contains valid Facebook cookies.
- The script uses specific XPath and class names to interact with the Repl.it interface. These may change over time, so you might need to update the script accordingly.
- Adjust the `time.sleep` values if necessary to match the load times of your internet connection and Repl.it response times.



