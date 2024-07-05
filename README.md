# Wingwalker Inkscape Extension

This repository houses the setup and code for Wingwalker utilities in Inkscape.

This extension provides utility functions and menu controls for working airfoil data files
from raw specs into usable drawings.  Those drawings can then be the basis for 3D models.

## Contributing

This started as a personal mad science fair project.  The goal is to make it as possible to 
digest, use, and transform airfoil specs into usable models and components.  Even if there is
ultimately not much demand for this in the world, merely working on this provides a lot of practice and
enjoyment.

Because of this, any ideas or contributions are welcome.  Expertise in Inkscape, extension development,
aeronautical engineering, 3D modeling and printing, or just good old-fashioned UI/UX and documentation is always
welcome.  Because this is a collection of utilities, rather than a monolithic setup, there are always ways to fold in
new ideas.

For anyone who wishes to get into Inkscape extension development, this could be a good project to review, as well as 
a fun place to practice changes, updates, or new ideas.  Because it's a "mad science fair" project, you're free to have 
as much fun as you want:  If everything breaks, the world won't end--we'll just fix it up and keep moving on.

### Setup

This section lays out one possible way to set up development.  This is not the only way, nor required, but 
should get most users off the ground quickly.

The basic steps are fairly straightforward:

 - Fork the project
 - Clone the repository locally
 - Run Inkscape with the wingwalker extension to develop/test/try
 - Work the changes you wish to contribute
 - Commit and submit a PR

For most developers, you can simply clone the git repo into your Inkscape extensions folder.
  On Fedora, this is `~/.config/inkscape/extensions`.  If you clone it in there, the extensions latest 
setup and state will be loaded up when you restart Inkscape.  

Alternatively, if you prefer to be able to quickly go back to vanilla Inkscape, you can clone in a development directory
and just create a symlink to the extensions folder.  My setup goes as follows:

```bash
david@tanngrisnir /home/david/pythondev
$ git clone git@github.com:david-days/wingwalker-inkex.git

david@tanngrisnir /home/david/pythondev
$ ln -s /home/david/pythondev/wingwalker-inkex $HOME/.config/inkscape/extensions/wingwalker
```

Removing the symlink does the job of taking out the extension (in case I'm in the middle of development and need to do some 
separate Inkscape work), and adding it back in is as simple as rerunning the `ln -s` command again.

## License

Just like the core Wingwalker python package, this extension is under the MIT license.  ou are free to use, abuse, modify, 
or ridicule the software, its products, and its processes in any way you see fit.


