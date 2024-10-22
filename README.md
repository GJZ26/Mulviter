# TermiView: Terminal-Based Multimedia Viewer

TermiView is a simple terminal-based application designed for viewing images, videos, and capturing camera input directly from the command line.

## Supported Platforms
TermiView has been tested and works seamlessly in the following environments:
- CMD (Windows Command Prompt)
- PowerShell
- Git Bash

## Features

- **Image Viewing**: Display PNG, JPG, and JPEG images directly in the terminal.
- **Video Playback**: Play MP4 videos right from the command line.
- **Camera Capture**: Access and display live feed from the default camera (if available).

## Commands

- **Show Image**  
  ```bash
  show-image PATH
  ```  
  Displays the image located at `PATH`. Supported formats: PNG, JPG, JPEG.

- **Show Video**  
  ```bash
  show-video PATH
  ```  
  Plays the video file located at `PATH`. Supported format: MP4.

- **Show Camera**  
  ```bash
  show-camera
  ```  
  Captures and displays live video from the default camera.

## Installation

To install Mulviter, follow these steps:

1. Ensure you have Python installed on your system.
2. Create a virtual environment:
   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run Mulviter with your desired command:
   ```bash
   python app.py [command]
   ```
