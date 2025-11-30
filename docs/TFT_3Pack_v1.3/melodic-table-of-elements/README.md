# The interactive periodic table of elements

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Website](https://img.shields.io/website?down_color=red&down_message=offline&up_color=green&up_message=online&url=https%3A%2F%2Fleonard-seydoux.github.io%2Fmelodic-table-of-elements%2F)](https://leonard-seydoux.github.io/melodic-table-of-elements/)
[![GitHub last commit](https://img.shields.io/github/last-commit/leonard-seydoux/melodic-table-of-elements)]()
[![GitHub contributors](https://img.shields.io/github/contributors/leonard-seydoux/melodic-table-of-elements)]()
![GitHub repo size](https://img.shields.io/github/repo-size/leonard-seydoux/melodic-table-of-elements)


This repository is an artistic project that turns the periodic table of elements into an interactive musical instrument. No description needed, just try it at https://leonard-seydoux.github.io/melodic-table-of-elements/. The project aims at evolving, so feel free to contribute! 

## How to sonify the periodic table of elements

Each sound are made from the different features of the periodic table, like the period or the group (see the script [make_sounds.py](make_sounds.py) for more information). 

The sounds are created from a fundamental frequency, and overtones that are multiples of the fundamental frequency. The fundamental frequency f of a given period is obtained from 

    fundamental_frequency = element_period * f0

where f0 is the lowest fundamental frequency. The overtones are obtained from

    overtone = element_group * fundamental_frequency

After sine-wave generation, the sounds are shaped with a Tukey window, and an exponential decay in order to mimick the attack and decay of instruments. The sound is saved as a WAV file, and then converted to an MP3 file using ffmpeg.

Several overtones are added depending on the block of the element. The d-block elements have one overtone, the f-block elements have two overtones, and the p-block elements have three overtones. The amplitude of the overtones is reduced as the overtone number increases.

Finally, the waveform is shaped with a Tukey window, with an exponential decay to reduce the volume over time. The sound is saved as a WAV file, and then converted to an MP3 file using ffmpeg.

## Potential improvements

One notable issue is the click sound that may appear when the pointer leaves and re-enters the element before the fade-out of the sound. This is due to the fact that the sound is stopped and restarted when the pointer leaves and re-enters the element. I tried to have an "emergency" fade-out of the sound when the pointer leaves and re-enters the element, but it did not work. If you have any idea on how to solve this issue, please let me know!
