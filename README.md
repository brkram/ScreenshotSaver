# ScreenshotSaver
Quick script to save screenshots

## About The Project
While studying or watching an online lecture I often take screenshots of notes and other presented material so I can later reference it.
I found that this simple task took me longer than I wanted, deciding where to keep the image, and what name to give it interrupted my concentration in the main goal - learning.

So I wrote this quick script to take my mind off of that, all it does is save an image you have in the clipboard to a predefined location, with a unique time based name.

## Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/brkram/screenShotSaver.git
   ```
2. Install the pillow (PIL fork) dependency.
   ```sh
   pip install pillow
   ```
3. Edit the PATH and FOLDERNAME variables.
	```python
	# Example path and foldername
	PATH = "C:/"
	FOLDERNAME = "TempScrennShots/"
	```

## Usage 
Use the Windows shortcut to crop an image from the screen (Win-key + Shift + S), or alternatively screenshot the whole screen using the 'prtscr' key on your keyboard.
(Just make sure you have an image in your clipboard)

I use [SlickRun](https://bayden.com/slickrun/) to run the script, but, you can use whatever interface you like.

and boom, the image is saved in the predefined directory and you can continue reading without any further interruptions.

## Roadmap

- [x] Add time and date to file name (unique)
- [x] error handling - don't crash if I don't have copied picture in my clipboard 
	- [ ] don't just try-except lol
- [ ] Add predefined arguments
	- [ ] name templates
	- [ ] location to save the picture
	- [ ] silent-mode (don't open folder when done)
