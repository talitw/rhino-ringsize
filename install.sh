#!/bin/bash

install_path="$HOME/Library/Application Support/McNeel/Rhinoceros/MacPlugins/PythonPlugins/RingSize{c079b327-5ac5-4133-8ca6-5209661ac833}/dev"
mkdir -p "$install_path"
cp RingSize_cmd.py "$install_path"
