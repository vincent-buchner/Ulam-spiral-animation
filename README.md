# Mapping Prime Numbers in Ulam's Spiral using Manim

## Introduction

This project aims to visualize prime numbers in Ulam's Spiral using Python's Manim library. Ulam's Spiral is a graphical depiction of prime numbers arranged in a spiral pattern, named after mathematician Stanislaw Ulam who discovered it. By representing prime numbers in this manner, certain patterns and structures within prime numbers become apparent.

<u>If you're new to Manim:</u> First, welcome to the community! I recommend watching a video on installation, as manim requires FFMPEG to be installed. There's some great tutorial videos on YouTube.

## Installation

To run this project, you need to install Python and the Manim library. Clone the git repository and install the requirements.

```bash
git clone https://github.com/vincent-buchner/Ulam-spiral-animation.git
cd Ulam-spiral-animation
pip install -r requirements.txt
```

## Rendering Video
You can then render the video in **low quality** using the following command:
```bash
manim -pql main.py PlayWithPositions --disable_caching
```

or in **high quality** using this command:
```bash
manim -pqh main.py PlayWithPositions --disable_caching
```

I've got the disable caching flag set as to make the  rendering process faster, but you may want to remove it (that's at least what the warning errors said to do).

## Additional Resources
- [Install FFMPEG](https://phoenixnap.com/kb/ffmpeg-windows)
- [Wiki Page - Ulam Spiral](https://en.wikipedia.org/wiki/Ulam_spiral)
- [The Coding Train: Coding Challenge 167](https://youtu.be/a35KWEjRvc0?si=c1GOMYKF7JGVoQZU)
- [Mathematical Games - The remarkable lore of the prime numbers ](https://www.scientificamerican.com/article/mathematical-games-1964-03/)
- [Original Article by M. Stein and S. M. Ulam](https://www.jstor.org/stable/2314055?origin=crossref&seq=1)