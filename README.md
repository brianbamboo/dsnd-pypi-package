# Sample Random Variables Python Package

## Installations
Because this is a Python package, you can just actually install locally by typing `pip install randomvariables`.

## Motivation
The primary motivation for this project was to gain experience with how Python packages are structured, writing my own Python package, learning how to install my own package locally, and finally, understanding how to upload a package to PyPI for public release. 

## File Descriptions
The randomvariables directory contains classes for the random variable types implemented in the library. Currently there are only two random variables implemented, Gaussian and exponential random variables.

## Summary
This package provides random variable classes whose only current meaningful functionality is generating realized values from their `generate` function(s), which are just a wrapper around their respective NumPy implementation of random number generation. In the future, random variables from other distributions will be added, along with hopefully some additional functionality that extends this beyond just a simple NumPy wrapper package. 

## Authors
Most of what's in this package/repo is written by me. Some inspiration was taken from content from the Udacity Data Scientist Nanodegree, where the example package is written on a library containing random variable distribution classes.

## Acknowledgements
Thanks to Udacity for including this optional project as part of their Data Scientist Nanodegree, which allowed me to gain some experience with writing my own Python package, installing, and uploading it to PyPI. Thanks to NumPy for providing some great random variable generation functions that I used :) 