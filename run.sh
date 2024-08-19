#!/bin/bash

: '
This script performs the following tasks:
  * conversion of an image to an audio file using python script,
  * conversion of audio file to the spectrogram image using SoX.

Parameters:
  :param test.png: The input image file to be converted to an audio file.

Outputs:
  * result.wav: The audio file generated from the image.
  * result.jpg: The spectrogram image generated from the audio file.
'

# Convert the image to an audio file.
python main.py "test.png" "result.wav"

# Generate a spectrogram jpg file.
sox result.wav -n highpass 200 gain -l -2 spectrogram -o result.jpg
