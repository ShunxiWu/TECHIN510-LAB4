import streamlit as st
import datetime
import time
from zoneinfo import ZoneInfo

# Function to get current time for a given timezone
def get_current_time(timezone):
    return datetime.datetime.now(tz=ZoneInfo(timezone))

# Streamlit app
def world_clock_app():
    st.title("World Clock App")

    # Define default timezones
    default_timezones = ["America/Los_Angeles", "Europe/Amsterdam", "Asia/Tokyo","Australia/Sydney"]

    # Display time for default locations
    for timezone in default_timezones:
        current_time = get_current_time(timezone)
        st.write(f"{timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Display time for user-selected locations
    selected_locations = st.multiselect("Select additional locations", ["America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"])
    if selected_locations:
        for location in selected_locations:
            current_time = get_current_time(location)
            st.write(f"{location}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Create a dynamic clock display
    clock_text = st.text("")
    
    # Update the clock every second
    while True:
        current_time = datetime.datetime.now()
        clock_text.markdown(
            f"<h1 style='text-align:center;'>{current_time.strftime('%H:%M:%S')}</h1>",
            unsafe_allow_html=True
        )
        
        # Sleep for 1 second
        time.sleep(1)

if __name__ == "__main__":
    world_clock_app()
