
# Musical Matrix
Code for an LED matrix that visualizes the music playing on a Linux system. Uses CAVA.

## Demo
Here's a brief demonstration of the matrix in action (imagine Mercy by Kanye West playing in the background)

![Demo](https://raw.githubusercontent.com/josephnormandev/musicalmatrix/main/images/demo.gif)

## Hardware
The LEDs are running off of my **Raspberry Pi 3** connected to a 10x15 matrix of WS281x LEDs.

![The wiring of my Matrix](https://raw.githubusercontent.com/josephnormandev/musicalmatrix/main/images/Wiring.jpg)

The music is playing on an Ubuntu 20.04 system

## CAVA Installation
The real backbone to this project was the Fast Fourier transform code written in the CAVA library. CAVA takes care of ripping the audio off of the audio sources on my system.

To install it in Ubuntu 20.04, type:

	sudo add-apt-repository ppa:tehtotalpwnage/ppa
	sudo apt-get update
	sudo apt-get install cava

Copy leds.py to your Raspberry Pi.

Copy cava.conf to your home directory on your Ubuntu system.

Then run the command on Ubuntu:

	unbuffer cava -p PATH_TO_YOUR_CAVA.conf | ssh pi@IP_OF_RASPBERRYPI sudo python PATH_TO_LEDS.py

## Credits

I used this guy's great CAVA library: https://github.com/karlstav/cava

I took inspiration from this guy's code that turned his strip into a visualizer: https://github.com/nvbn/soundlights

