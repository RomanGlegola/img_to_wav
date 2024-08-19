#!/usr/bin/python
"""
Module img_to_wav.main

This module contains the main functionality for generating WAV files
from images using the SpectrogramGenerator class.
"""

import argparse
import wave
from array import array

import matplotlib.image as mpimg
import numpy as np


class SpectrogramGeneration:
    """
    Generates spectrogram from given image.
    """

    def __init__(self, image_filename: str):
        """
        Initializes a SpectrogramGenerator object.

        :param image_filename: filename of the image to generate the
            spectrogram from.
        """
        self.image = mpimg.imread(image_filename)

    def preprocess_image(self) -> np.ndarray:
        """
        Preprocesses the image by:
            * converting it to grayscale,
            * flipping it vertically,
            * raising its power to the third.

        :rtype np.ndarray: A numpy array representing the preprocessed image.
        """
        self.image = np.sum(self.image, axis=2).T[:, ::-1]
        self.image = self.image**3
        return self.image

    def generate_spectrogram(self) -> np.ndarray:
        """
        Converts the preprocessed image into an array of complex numbers,
        which is then inverse Fourier transformed to generate the spectrogram.

        :rtype: np.ndarray
        """
        width, height = self.image.shape
        audio_data = np.fft.irfft(a=self.image, n=height * 2, axis=1).reshape(
            width * height * 2
        )
        return audio_data

    @staticmethod
    def normalize_audio(audio_data: np.ndarray) -> bytes:
        """
        Normalizes generated audio data by:
            * calculating the average of the audio data,
            * multiplication of the audio data by a scaling factor to adjust
                its amplitude,
            * conversion of the audio data to a byte array using the
                array() function.

        :param np.ndarray audio_data: generated spectrogram.
        :rtype bytes: Normalized audio data.
        """
        audio_data -= np.average(audio_data)
        audio_data *= (2**15 - 1.0) / np.amax(a=audio_data)
        return array("h", np.int_(audio_data)).tobytes()


class WAVWriter:
    """
    Write  spectrogram to .wav file.
    """

    def __init__(self, output_filename: str, audio_data: bytes):
        """
        Initializes a WAVWriter object.

        :param str output_filename: The filename of the .wav file to generate
            the spectrogram to.
        :param bytes audio_data: normalized audio data.
        """
        self.output_filename: str = output_filename
        self.audio_data: bytes = audio_data

    def write_wav(self):
        """
        Writes an audio file in WAV format.

        :rtype: .wav
        """
        # pylint: disable=E1101
        with wave.open(f=self.output_filename, mode="w") as output_file:
            output_file.setparams(
                params=(1, 2, 44100, 0, "NONE", "not compressed")
            )
            output_file.writeframes(data=self.audio_data)
        # pylint: enable=E1101


def main():
    """
    Parses command-line arguments, processes an image to generate
    a spectrogram, and saves the result as a WAV file.

    Command-line arguments:
        * `input_image`: Optional argument specifying the path to the
            input image file. Default 'test.png'.
        * `output_wav`: Optional argument specifying the path to the
            output WAV file. Default 'result.wav'.
    """
    parser = argparse.ArgumentParser(
        description="Generate a WAV file from an image by converting "
                    "the image into a spectrogram."
    )
    parser.add_argument(
        "input_image",
        nargs="?",
        default="test.png",
        help="The input image file to be converted into a WAV file. "
             "Default is 'test.png'.",
    )
    parser.add_argument(
        "output_wav",
        nargs="?",
        default="result.wav",
        help="The output WAV file to save the generated audio. "
             "Default is 'result.wav'.",
    )

    args = parser.parse_args()

    spectrogram_generator = SpectrogramGeneration(
        image_filename=args.input_image
    )

    spectrogram_generator.preprocess_image()
    spectrogram = spectrogram_generator.generate_spectrogram()
    normalized_audio_data = spectrogram_generator.normalize_audio(
        audio_data=spectrogram
    )
    WAVWriter(
        output_filename=args.output_wav,
        audio_data=normalized_audio_data
    ).write_wav()


if __name__ == "__main__":
    main()
