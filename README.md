GitPic
=======

Make your git commit history more fun by automatically make a webcam capture for each commit you make! Captures will be saved and sorted based on project and time so you can easily browse your history. As a bonus the commit message is rendered to the captured image. Holy smokes thats awesome!

![gitpic](https://github.com/wejeus/gitpic/raw/master/capture.png)

## Install (Mac OSX)

GitPic relies on Python and OpenCV (and its Python bindings of course). Easiest way to install required packages is to first install MacPorts (http://www.macports.org/) then from a commandline run:

### Install OpenCV and Python bindings (Using MacPorts)
	
	sudo port install opencv +python27 // this will take a while..

### Install OpenCV and Python bindings (Using brew)
	
	brew install homebrew/science/opencv
	cd /Library/Python/2.7/site-packages/
	sudo ln -s /usr/local/Cellar/opencv/<VERSION>/lib/python2.7/site-packages/cv.py cv.py
	sudo ln -s /usr/local/Cellar/opencv/<VERSION>/lib/python2.7/site-packages/cv2.so cv2.so


To setup git always use the GitPic hooks setup a template dir:

	git config --global init.templatedir "~/.git_template"

Then copy the files "capture_webcam.py", "post-commit" to this folder or run the install script:
	
	./install.sh

Now every time you create a new git repository with 'git init' GitPic will automatically be installed! Whohoo! If you already have an existing git repository but still want all the GitPic goodness it is safe to run 'git init' again and git will copy any new hooks to your existing repository.

## Configuration

Images will by default be stored in ~/Pictures/gitpic/ but you can change this by editing the constant "OUTPUT_DIR" in the script.