# Dotconf
A simple script to copy configuration files from any location to `$HOME/.config/dotfiles` and replaces the original file with a symlink. 

Useful for adding config files to one directory for version control backups and tracking changes. 

## Getting Started

Simply copy the script to `$HOME/bin` or wherever your local binaries are stored. 

### Tip
If you do not currently have a directory for local binaries, simply create `$HOME/bin` and add the following line to your `.bashrc` file: 
 
```
export PATH="$HOME/bin:$PATH"
```

*As this is a work in progress, please ensure you make a backup of your existing config files before executing this script.*

### Prerequisites

Requires Python 3. 

## Usage

Simply execute the following command: 

```
$ cnf.py ~/.vim
```

A new file `$HOME/.config/dotfiles/.vim` will be created and the original file replaced with a symlink. 

### Additional Options (Currently in development)

Additional command-line arguments: 

* `--input-file` Specify a file containing a list of config files/directories for writing to `$HOME/.config/dotfiles` in bulk. 

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
