import psutil
import pyautogui
import time

def is_laptop_plugged():
    # Get battery status
    battery = psutil.sensors_battery()
    return battery.power_plugged

def take_screenshot():
    # Get current timestamp for naming the screenshot
    timestamp = time.strftime("%Y%m%d%H%M%S")
    screenshot_name = f"screenshot_{timestamp}.png"

    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot
    screenshot.save(screenshot_name)
    print(f"Screenshot saved as {screenshot_name}")

def main():
    screenshot_taken = False  # Variable to track if a screenshot has been taken

    while True:
        # Check if laptop is unplugged and a screenshot hasn't been taken yet
        if not is_laptop_plugged() and not screenshot_taken:
            take_screenshot()
            screenshot_taken = True  # Set the flag to indicate that a screenshot has been taken
            break  # Exit the loop after taking the screenshot

        # Wait for 1 second before checking again
        time.sleep(1)

if __name__ == "__main__":
    main()