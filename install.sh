#!/bin/bash
echo "Installing.."
cp -f capture_webcam.py ~/.git_template/hooks/
cp -f post-commit ~/.git_template/hooks/
echo "done"