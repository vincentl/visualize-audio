![Image of sound waves](https://github.com/vincentl/visualize-audio/blob/main/readme.png)

# Description

Create a visual representation of an audio clip using `librosa` to decompose the time series into harmonic (drawing in rainbow) and percussive (drawn in gray) components.

## Brief Details

Used ChatGPT to develop `visualize.py`. Made a few modifications to customize line size and transparent background and then from the original audio file `original.m4a`, executed

```bash
ffmpeg -i original.m4a -c:v copy -c:a libmp3lame -q:a 4 song.mp3
ffmpeg -ss 8 -t 32 -i song.mp3 segment.mp3
python3 visualize.py
```

This extracted the segment from 8 seconds to 32 and produced the visualization in an PNG file. Then used Gimp to overlay the visualization on the background color and to add the song name with band name.
