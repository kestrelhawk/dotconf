# Dotconf
A simple script to copy configuration files from any location to `$HOME/.config/dotfiles` and replaces the original file with a symlink. 

Useful for adding a 

## Getting Started

Simply copy the script to `$HOME/bin` or wherever your local binaries are stored. 

### Tip
If you do not currently have a directory for local binaries, simply create `$HOME/bin` and add the following line to your `.bashrc` file: 
 
```
export PATH="$HOME/bin:$PATH"
```

### Prerequisites

Requires Python 3. 

## Built With

* Python 3 using the following libraries: 
    * os
    * argparse
    * shutil
    * json

## Contributing

Feel free to contribute or fork and tailor it to your own needs. 

## Authors

* Kevin Sanderson

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
