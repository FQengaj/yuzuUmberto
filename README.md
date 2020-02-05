# Umberto for Yuzu
Yuzu is a Emulator the Nintendo Switch Konsole. As the Emulator is Developed some Games work better then others for this Emulator. Luckily the Devs of the Yuzu-Emulator provide a Website to Check the Compatibility of every Game.

Umberto is a CLI-Program written in Pyhton that lets you create a Watchlist and gets only the Information for these Games with a click of a Button. 

## Getting Started

You can find and Download Umberto from the dist Folder. 
Thats it you are good to Go.

## Useage
After the Download just double click the .exe file to Run it. A Comandline window will open up and Show you your Options:

 1. Create new Watchlist( c)
 2. Add new Game to Watchlist(a)
 3. Show Watchlist(s)
 4. Load Watchlist(L)
 5. Show Compatibility Definitions(d)
 6. Help(h)
 7. Quit(q)

Connection to the internet is needed for this to work. Umberto does not store any Data except for the Gametitles in the Watchlist.


### 1. Create a new Watchlist
First thing you want to do is setting up a Watchlist. Todo so you press c or 1. Keep in mind that doing so will overwrite the existing Watchlist. Umberto will ask to Type the Gametitles you want to add to your Watchlist. The Gametitles do not need to match perfectly, it is better to think of it like the *CTRL*+*F* search on a Website. To Close the Input type he letter q or just press the Enterkey without any input.

### 2. Add new Game to Watchlist
If you wish to add a Gametitle to your Watchlist you can do so by inputting a or 2. Umberto will not Check your Input. So make sure you check your Spelling and avoid dubplicates in your Watchlist. Just like when your first set up your Wachlist, you can give multiple inputs by pressing the enter-key. To close the input loop either give the input q or a empty input.

### 3. Show Watchlist
By Typing s or 3 Umberto will print out all your Gametitle currently on the Watchlist.

### 4. Load Watchlist
This will Load the Gametitles off your Watchlist and Start the Search for the Game Availability. If you have not set up a Watchlist yet Umberto will ask you to do so and use it immediately.

Keep in mind that this is the Default Option, so pressing the enterkey on an emty input will default to Loading the Watchlist and Starting the Search.

### 5. Show Compatibility Definitions
The Yuzu Website has a definition for the Status of a Game so e.g. what it means if a Game has the title 'Bad'. By typing d or 5 Umberto will show just these definitions.

### 6. Help
Typting h or 6 Umberto will show you the Options again.

## Author

* [**Florian Qengaj**](https://github.com/FQengaj)

## License

This project is licensed under the GNU Lesser General Public License v3.0 - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* If you wish to Download and use the Yuzu-Emulator for Nintendo Switch you can find them [here](https://yuzu-emu.org)

