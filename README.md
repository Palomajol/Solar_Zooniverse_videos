# Solar_Zooniverse_videos
This directory is an extension on the https://github.com/CharKap/Solar_Zooniverse_Processor.git package. This code written in python file Video_production.py uses the output of the Solar data output and converts it into mp4 video's per recorded HEK event. 

# Required Packages
In order for this code to work the following packages are required:
  1. sunpy 
  2. matplotlib
  3. ffmpeg
  
All can be installed using Anaconda with _pip install_

# Getting started
Before trying to run the code first go through the Zooniverse_processor workflow, the produced output of this workflow will be used in the code to produce the video's. It is possible to run this code before the **Preparing to export**, since it does not use any of these outputs. 

# Running the code
The python file Video_production.py should be saved in the wroking directory in which the Zooniverse_processor workflow was executed. Your directory should have a folder files which contains the subdirectory fits/ and generated/. The code is executed using the terminal in the correct directory and typing _python Video_production.py run_ 
