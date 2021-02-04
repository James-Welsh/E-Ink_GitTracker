# GitTracker

A tool that can be used to show most recent repo modifed as well as some info
relating to the repo on a WaveShare 2.13" V2 screen mounted to a pi zero W.

Here are the goals that I would like to hit:

- [X] Display most recently modified public repo name.
- [X] Display most recently modified repo including private ones.
- [X] Display more info regarding repo (name, time edited, etc..)
- [X] Create a command line version that can be used without the Waveshare e ink display.
- [X] Write a HowTo guide for the project.

## How to use

- Once the repo is cloned create a file called key.txt within the src/ directory.
- Generate a 'Personal access token' by clicking on your picture on the top right
    > Settings > Developer settings > Personal access tokens.
- Paste this into key.txt
- Run either CommandLine.py or eInk_display.py (depending on whether you want to
    run on the e ink display or in console) from the src directory making sure you
    have all required python libraries.
    - Pillow
    - Datetime
    - All waveshare dependencies
- USE PYTHON 3.
