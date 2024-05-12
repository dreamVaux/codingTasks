#!/bin/bash

if [ -d "new_folder" ]; then
	mkdir if_folder
fi

if [ -d "if_folder" ]; then
	mkdir hyperiondev
else
	mkdir new-projects
fi