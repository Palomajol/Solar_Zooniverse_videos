# Solar_Zooniverse_videos
This directory is an extension on the https://github.com/CharKap/Solar_Zooniverse_Processor.git package. This code written in python file Video_production.py uses the output of the Solar data output and converts it into a mp4 video per recorded HEK event. 

# Required Packages
In order for this code to work the following packages are required:
  1. sunpy 
  2. matplotlib
  3. ffmpeg
  
First two can be installed using Anaconda with _pip install_ the ffmpeg can be easily installed through Homebrew (for Mac) or through _conda install -c conda-forge ffmpeg_ 

# Getting started
Before trying to run the code first go through the Zooniverse_processor workflow, the produced output of this workflow will be used in the code to produce the video's. It is possible to run this code before the **Preparing to export**, since it does not use any of these outputs. 

# Running the code
The python file Video_production.py should be saved in the wroking directory in which the Zooniverse_processor workflow was executed. Your directory should have a folder files which contains the subdirectory fits/ and generated/. The code is executed using the terminal in the correct directory and typing _python Video_production.py run_ 

# Workings
The code first checks whether the subdirectory where the mp4 videos are written files/generated/mp4/ exists. If it does not yet exist the directory is made. The code then looks at all folders in the files/fits/ directory checking for folders containing HEK events, denoted by SOL in their foldername as written by Zooniverse_processor. For each SOL* folder a sequence of fits files is then taken from the directory and combined using the makevideo function. The results is a mp4 video for each of the HEK events saved in the working directory, saved under fits/generated/mp4/SOL*foldername*.mp4. The function makevideo has by default overwrite=False, this can be changed by the user if desired.  

