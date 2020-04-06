#!/bin/bash
echo "Installing.."
mkdir -p ~/.git_template/hooks/
chmod +x capture_webcam.py
chmod +x post-commit
cp -f capture_webcam.py ~/.git_template/hooks/
cp -f post-commit ~/.git_template/hooks/
echo "done"