# img_to_wav

## Description

`img_to_wav` is a Python-based tool that converts images into WAV audio files by generating spectrograms from the image data. This tool utilizes inverse Fourier transformation to convert the processed image data into audio.

## Requirements

- Python 3.x
- `sox` (Ensure it's installed and accessible in your PATH, especially for Windows users)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RomanGlegola/img_to_wav.git
    cd img_to_wav
    ```

2. **Set up a virtual environment:**
    - On **Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    - On **Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install `Sound eXchange` (SoX):**
    - On **Windows**:
        1. Download and install SoX from [SourceForge](https://sourceforge.net/projects/sox/files/sox/).
        2. Add the SoX installation directory to your system's PATH.
    - On **Linux**:
        ```bash
        sudo apt-get install sox
        ```

## Usage

1. **Activate the virtual environment** (if not already active):
    - On **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - On **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

2. **Run the script to convert an image to a WAV file:**
    ```bash
    python main.py <input_image> <output_wav>
    ```
    - `<input_image>`: The image file you want to convert (default: `test.png`).
    - `<output_wav>`: The name of the output WAV file (default: `result.wav`).

   Example can be found in run.sh
