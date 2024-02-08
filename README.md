# World Clock App

This Streamlit application provides users with a convenient way to check the current time in different timezones around the world. Users can view the time for default locations as well as select additional locations based on their preferences. The app also includes a dynamic clock display that updates every second.

## Installation

To run this application, ensure you have Python installed on your system. You will also need to install the necessary dependencies. You can do this by running:

pip install streamlit

pip install zoneinfo

## Usage

To start the World Clock App, run the following command in your terminal:

streamlit run <filename>.py


Replace `<filename>` with the name of the Python script containing the provided code.

Once the app is running, you will see a title "World Clock App" displayed at the top of the page. The app will then show the current time for default locations, including "America/Los_Angeles", "Europe/Amsterdam", "Asia/Tokyo", and "Australia/Sydney".

You can also select additional locations by using the multiselect dropdown provided. Choose from locations such as "America/New_York", "Europe/London", "Asia/Tokyo", and "Australia/Sydney" to view the current time in those areas as well.

## Dynamic Clock Display

The app features a dynamic clock display that updates every second. This display shows the current time in real-time, providing users with an accurate and continuously updating clock.

## Code Structure

- The `get_current_time` function retrieves the current time for a given timezone using the `datetime` and `zoneinfo` modules.
- The `world_clock_app` function sets up the Streamlit application, displays the current time for default locations, allows users to select additional locations, and implements the dynamic clock display.
- The `if __name__ == "__main__":` block executes the `world_clock_app` function when the script is run directly.

## Note

Keep in mind that the dynamic clock display utilizes a while loop with a sleep function, which may cause the app to become unresponsive in certain environments. It is recommended to use this feature judiciously and considerate of system resources.

Enjoy using the World Clock App to stay updated with the current time across different timezones!
