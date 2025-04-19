# crosshair_camera
An aim-assist camera project for Raspberry Pi, automatically displaying a fullscreen feed with a green crosshair on boot, powered by OpenCV and systemd.

# AWM Crosshair Camera Project

## Overview

This project aims to automatically start a Raspberry Pi camera feed with a green crosshair overlay in fullscreen mode upon system boot. It utilizes OpenCV for camera access and drawing the crosshair, and a systemd service to manage the automatic startup of the Python script. Fullscreen functionality is achieved using the `cv2.setWindowProperty` function in OpenCV.

## Files

* `crosshair_camera.py`: The main Python script responsible for capturing the camera feed, drawing the crosshair, and displaying it in a window (now fullscreen).
* `/etc/systemd/system/crosshair.service`: The systemd service definition file that manages the automatic startup of the `crosshair_camera.py` script on boot.

## Setup and Installation

1.  **Connect the Camera:** Ensure your camera is properly connected to your Raspberry Pi.
2.  **Install Dependencies:** Make sure you have OpenCV and `python3` installed:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip libopencv-dev python3-opencv
    ```
3.  **Create the Python Script:** Save the `crosshair_camera.py` code (as provided in our previous successful interaction) in the `/home/pi` directory.
4.  **Create the Systemd Service File:**
    * Create the file `/etc/systemd/system/crosshair.service` with the following content:
        ```ini
        [Unit]
        Description=AWM Crosshair Camera
        After=graphical.target
        Requires=graphical.target

        [Service]
        User=pi
        WorkingDirectory=/home/pi
        ExecStart=/usr/bin/python3 /home/pi/crosshair_camera.py
        Restart=on-failure
        Environment=DISPLAY=:0
        Environment=XAUTHORITY=/home/pi/.Xauthority

        [Install]
        WantedBy=graphical.target
        ```
5.  **Enable and Start the Service:**
    ```bash
    sudo systemctl enable crosshair.service
    sudo systemctl start crosshair.service
    ```
6.  **Reboot:** Reboot your Raspberry Pi to test if the camera starts automatically in fullscreen with the crosshair.

## Functionality

* **Automatic Startup:** The systemd service ensures the camera script runs automatically after the graphical environment is loaded.
* **Crosshair Overlay:** A green crosshair is drawn at the center of the camera feed, providing a visual aiming aid.
* **Fullscreen Display:** The camera feed is displayed in fullscreen mode using `cv2.setWindowProperty`.
* **Quit Option:** Pressing the `q` key in the camera window will close the application.
* **Logging:** The script logs its activity and any errors to `/home/pi/crosshair_camera.log`.

## Notes

* This setup assumes you are running a graphical environment on your Raspberry Pi.
* The `cv2.setWindowProperty` method for fullscreen might behave slightly differently depending on your window manager.

## Author
Dhinoj DS
