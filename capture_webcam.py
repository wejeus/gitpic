#!/usr/bin/python

# Author: Samuel Wejeus (samuel@isalldigital.com)

import cv2
import numpy as np
import time
import os
import subprocess
import sys

# Configuration
OUTPUT_DIR = "~/Pictures/gitpic/"
DEBUG = True

def capture(cameraFeed, path, message):
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    thickness = 1;
    padding = 10

    # we need couple of  frames before camera has adjusted to light conditions
    frame = None
    for x in range(0, 8):
        _, frame = cameraFeed.read()
    
    # add commit message
    (_, textHeight), _ = cv2.getTextSize(message, fontFace, fontScale, thickness);
    textPosY = textHeight
    lines = message.splitlines()
    for line in lines:
        position = (padding, textPosY+padding)
        # little hack to get a outline on text since opencv does not support it natively
        cv2.putText(frame, line, position, fontFace, fontScale, (0, 0, 0), thickness+2, lineType = 0)
        cv2.putText(frame, line, position, fontFace, fontScale, (255, 255, 255), thickness, lineType = cv2.CV_AA)
        textPosY = textPosY + textHeight + padding
    
    # output final image
    cv2.imwrite(path, frame)

# Program ----------------------------------------------

print "Running gitpic.."

projectBasePath = subprocess.Popen(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE).communicate()[0]
commitMessage = subprocess.Popen(["git", "log", "--format=%B", "-n", "1 HEAD"], stdout=subprocess.PIPE).communicate()[0].strip()
if DEBUG:
    projectBasePath = os.path.dirname(os.path.abspath(__file__))
    commitMessage = "Debug commit message\nspanning multiple\nlines\n=)"

if projectBasePath == "" or commitMessage == "":
    print "Error: no project or message!"
    sys.exit(1)

projectName = os.path.basename(projectBasePath).strip()
uri = os.path.expanduser(OUTPUT_DIR + projectName + "/")

# create dir if needed
cmd_makeDirs = "mkdir -pv " + os.path.dirname(uri)
ret = subprocess.call(cmd_makeDirs, shell=True)
if ret != 0:
    print "Error: could not create needed dirs!"
    sys.exit(1)

# prepare output filename
filename = time.strftime("%d-%m-%Y-%H-%M") + ".png"
imagePath = uri + filename

if DEBUG:
    print "gitpic: " + commitMessage + " -> " + imagePath

# init opencv camera
cameraFeed = cv2.VideoCapture(0)
capture(cameraFeed, imagePath, commitMessage)



