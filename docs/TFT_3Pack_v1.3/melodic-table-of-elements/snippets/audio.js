document.addEventListener('DOMContentLoaded', () => {
    // Check if DOM is fully loaded
    console.log('DOM fully loaded and parsed');

    // Get the enable sound button
    const enableSoundButton = document.getElementById('enable-sound-button');
    let soundEnabled = false;
    let currentlyPlayingSound = null; // Track currently playing sound

    function updateButtonText() {
        enableSoundButton.innerHTML = soundEnabled ? '<i class="fas fa-volume-up"></i>' : '<i class="fas fa-volume-mute"></i>';
    }

    // Enable or disable sound
    enableSoundButton.addEventListener('click', () => {
        soundEnabled = !soundEnabled; // Toggle sound enabled state
        updateButtonText(); // Update button text based on new state

        // Stop any currently playing sound if sound is disabled
        if (!soundEnabled && currentlyPlayingSound) {
            fadeOutSound(currentlyPlayingSound, 1000); // Use 50 ms for the small fade-out
            currentlyPlayingSound = null; // Reset currently playing sound
        }
    });

    // Store audio elements in an array
    const sounds = [];
    for (let i = 1; i <= 118; i++) {
        const soundElement = document.getElementById(`sound-${i}`);
        if (soundElement) {
            sounds.push(soundElement);
        }
    }

    function fadeOutSound(sound, duration) {
        const fadeOutDuration = duration || 1000; // in milliseconds, default to 10 ms if no duration provided
        const fadeOutSteps = 1000; // Number of steps to fade out
        const fadeOutStepDuration = fadeOutDuration / fadeOutSteps; // Duration of each step
        const volumeStep = sound.volume / fadeOutSteps; // Volume decrement in each step

        const fadeOutInterval = setInterval(() => {
            if (sound.volume > volumeStep) {
                sound.volume -= volumeStep;
            } else {
                sound.volume = 0;
                sound.pause();
                sound.currentTime = 0; // Reset the audio to the beginning
                clearInterval(fadeOutInterval); // Clear the interval
            }
        }, fadeOutStepDuration);
    }

    // Object to keep track of timeouts for each sound
    const timeouts = {};

    for (let i = 1; i <= 118; i++) {
        const hoverElement = document.querySelector(`#n${i}`);
        const hoverSound = document.getElementById(`sound-${i}`);

        if (hoverElement && hoverSound) {
            hoverElement.addEventListener('mouseenter', () => {
                if (soundEnabled) {
                    console.log(`Mouse entered element-${i}`);
                    clearTimeout(timeouts[i]); // Clear any existing timeout for this sound
                    hoverSound.pause(); // Pause the sound
                    hoverSound.currentTime = 0; // Reset the sound to the beginning
                    hoverSound.volume = 1; // Reset volume
                    hoverSound.play().catch(error => {
                        console.error('Error playing sound:', error);
                    });
                    currentlyPlayingSound = hoverSound; // Track currently playing sound
                }
            });

            hoverElement.addEventListener('mouseleave', () => {
                if (soundEnabled) {
                    console.log(`Mouse left element-${i}`);
                    if (currentlyPlayingSound === hoverSound) {
                        // Apply small fade-out effect over 50 milliseconds
                        fadeOutSound(hoverSound, 1000); // Use 50 ms for the small fade-out
                        currentlyPlayingSound = null; // Reset currently playing sound
                    }
                }
            });
        } else {
            console.error(`Element or sound not found for index ${i}`);
        }
    }

    // Initialize button text
    updateButtonText();
});
