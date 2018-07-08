#!/usr/bin/python

import os
import argparse
import shutil

# Parse command-line arguments
parser = argparse.ArgumentParser( description = 'A script that to create config file backups' )
parser.add_argument( 'configfile', help = 'current path to the config file' )
args = parser.parse_args()

# Get the user's home directory
HOME_DIR    = os.path.expanduser( '~' )

## TODO make 'config' path flexible and 'git init'
CONFIGS_DIR = os.path.join( HOME_DIR, '.config', 'dotfiles', '' )

# Determine if CONFIGS_DIR exists
if not os.path.exists( CONFIGS_DIR ):
    os.makedirs( CONFIGS_DIR )

if os.path.exists( args.configfile ) and not os.path.islink( args.configfile ):
    moveDir = shutil.move( args.configfile, CONFIGS_DIR )
    os.symlink( moveDir, args.configfile )
