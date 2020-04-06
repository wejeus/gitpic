GitPic
=======

Make your git commit history more fun by automatically make a webcam capture for each commit you make! Captures will be saved and sorted based on project and time so you can easily browse your history. As a bonus the commit message is rendered to the captured image. Holy smokes thats awesome!

![gitpic](https://github.com/wejeus/gitpic/raw/master/capture.png)

## Install (Mac OSX)

GitPic relies on Python 3 and OpenCV (and its Python bindings of course). Just install via pip3

	$> pip3 install opencv-python

If you have not defined it yet you need to create a template dir for git in which we will put the script and relavant hooks. When you create a new git repo the hooks defined here will be copied to your project.

	$> git config --global init.templatedir "~/.git_template"

Then copy the files "capture_webcam.py", "post-commit" to this folder or run the install script:
	
	$> ./install.sh

If you already have a git repository for your project just do a re:init of the project and the new hooks will be copied
	
	$> git init

Now every time you create a new git repository with 'git init' GitPic will automatically be installed! Whohoo! If you already have an existing git repository but still want all the GitPic goodness it is safe to run 'git init' again and git will copy any new hooks to your existing repository.

## Configuration

Images will by default be stored in ~/Pictures/gitpic/ but you can change this by editing the constant "OUTPUT_DIR" in the script.