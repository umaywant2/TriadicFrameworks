@echo off
echo Creating...
md scientific_instrument_review
cd scientific_instrument_review
copy con README.md
md 00_overview
cd 00_overview
copy con purpose.md
copy con method.md
copy con glossary_links.md
cd..
md 01_green_zone
cd 01_green_zone
copy con accelerometer.md
copy con ammeter.md
copy con anemometer.md
copy con caliper.md
copy con calorimeter.md
copy con electrometer.md
copy con gravimeter.md
copy con interferometer.md
copy con microscope.md
copy con seismometer.md
copy con spectrometer.md
copy con telescope.md
copy con thermometer.md
cd..
md 02_yellow_zone
cd 02_yellow_zone
copy con DNA_sequencer.md
copy con dynamometer.md
copy con ellipsometer.md
copy con hydrometer.md
copy con inclinometer.md
copy con magnetometer.md
copy con manometer.md
copy con mass_spectrometer.md
copy con NMR_spectrometer.md
copy con oscilloscope.md
copy con photometer.md
copy con spectrogram.md
copy con theodolite.md
cd..
md 03_red_zone
cd 03_red_zone
copy con electrostatic_analyzer.md
copy con eudiometer.md
copy con magnetic_tweezers.md
copy con magnetograph.md
copy con optical_tweezers.md
copy con thermocouple.md
copy con voltmeter.md
copy con Xray_scattering.md
cd..
md 99_appendix
cd 99_appendix
copy con instrument_list_raw.md
copy con notes_on_alignment.md
copy con regime_notes.md
cd..