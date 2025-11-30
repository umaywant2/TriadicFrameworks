"""Create the sounds to be played on hover over the element.

This script creates as many sounds as elements in the periodic table. Each sound are made from the different features of the periodic table, like the period or the group. 

The sounds are created from a fundamental frequency, and overtones that are multiples of the fundamental frequency. The fundamental frequency f of a given period is obtained from 

    fundamental_frequency = element_period * f0

where f0 is the lowest fundamental frequency. The overtones are obtained from

    overtone = element_group * fundamental_frequency

After sine-wave generation, the sounds are shaped with a Tukey window, and an exponential decay in order to mimick the attack and decay of instruments. The sound is saved as a WAV file, and then converted to an MP3 file using ffmpeg.

Several overtones are added depending on the block of the element. The d-block elements have one overtone, the f-block elements have two overtones, and the p-block elements have three overtones. The amplitude of the overtones is reduced as the overtone number increases.

Finally, the waveform is shaped with a Tukey window, with an exponential decay to reduce the volume over time. The sound is saved as a WAV file, and then converted to an MP3 file using ffmpeg.

Notes
-----
The units of the different parameters are as follows:
- Frequencies are in Hz.
- Times are in seconds.

This script requires the following packages:
- numpy
- scipy
- pandas (in elements.py)
- ffmpeg (to convert the WAV files to MP3)
"""

FREQUENCY_LOWEST_FUNDAMENTAL_HZ = 40
FREQUENCY_SAMPLING_HZ = 44100
SAMPLE_DURATION_SECONDS = 2
N_SAMPLES = FREQUENCY_SAMPLING_HZ * SAMPLE_DURATION_SECONDS
SPECTRAL_HARMONIC_DECAY = 0.5, 0.2, 0.1
NUMBER_OF_OVERTONES = {
    "s-block": 0,
    "d-block": 1,
    "f-block": 2,
    "p-block": 3,
}
ENVELOPE_DECAY_SEC = 0.5
ENVELOPE_ATTACK_SEC = 0.2
GENERIC_FILEPATH = "sounds/sound-{}.{}"
OUTPUT_VOLUME = 0.25
FFMGED_COMMAND = (
    "ffmpeg -y -i {} -codec:a libmp3lame -qscale:a 1 -v 0 -af volume={} {}"
)

import subprocess

import numpy as np
from scipy.io import wavfile
from scipy.signal.windows import tukey
from tqdm import tqdm

import elements


def time_vector(duration=SAMPLE_DURATION_SECONDS, samples=N_SAMPLES):
    """Generate a time vector."""
    return np.linspace(0, duration, samples, endpoint=False)


def sine(frequency):
    """Generate a sine wave with a given frequency."""
    return np.sin(2 * np.pi * frequency * time_vector())


def exponential_decay(tau=ENVELOPE_DECAY_SEC):
    """Generate an exponential decay."""
    return np.exp(-time_vector() / tau)


def window(tau=ENVELOPE_ATTACK_SEC):
    """Apply a window to the signal."""
    return tukey(len(time_vector()), tau)


def main():

    # Read the complete periodic table
    periodic_table = elements.read()

    # Iterate over the elements
    for _, element in tqdm(
        periodic_table.iterrows(),
        total=len(periodic_table),
        desc="Creating sounds",
    ):
        # Generate fundamental sound
        fundamental = element["period"] * FREQUENCY_LOWEST_FUNDAMENTAL_HZ
        note = sine(fundamental)

        # Add overtones
        overtone = fundamental * element["group"]
        for block in NUMBER_OF_OVERTONES.keys():
            for i in range(NUMBER_OF_OVERTONES[block]):
                note += SPECTRAL_HARMONIC_DECAY[i] * sine((i + 1) * overtone)

        # Exponential decay
        note *= exponential_decay()
        note *= window()
        note *= OUTPUT_VOLUME

        # Save the sound in wav and mp3 format
        filename_wav = GENERIC_FILEPATH.format(element["atomic_number"], "wav")
        filename_mp3 = GENERIC_FILEPATH.format(element["atomic_number"], "mp3")
        wavfile.write(filename_wav, FREQUENCY_SAMPLING_HZ, note)
        convert_command = FFMGED_COMMAND.format(
            filename_wav, OUTPUT_VOLUME, filename_mp3
        )
        subprocess.run(convert_command, shell=True)

        # Delete the WAV file
        subprocess.run(["rm", filename_wav])


if __name__ == "__main__":
    main()
