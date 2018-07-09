#!/usr/bin/python

import os
import argparse
import shutil
import json

# Parse command-line arguments
parser = argparse.ArgumentParser( description = 'A script that to create config file backups' )
parser.add_argument( '--configfile', help = 'path to the config file' )
parser.add_argument( '--inputfile', help = 'accepts a file containing one or more config files paths' )

args = parser.parse_args()

if args.inputfile and args.configfile:
    parser.error( 'Cannot use --inputfile together with --configfile.' )

# Get the user's home directory
HOME_DIR    = os.path.expanduser( '~' )

## TODO make 'config' path flexible and 'git init'
CONFIGS_DIR = os.path.join( HOME_DIR, '.config', 'dotfiles', '' )

configFiles = [ args.configfile ]

if( os.path.isfile( 'data.json' ) ):
    with open( 'data.json' ) as infile:
        output = json.load( infile )
else:
    open( 'data.json', 'w')
    output = {}

if os.path.exists( args.inputfile ) and not args.inputfile is None:
    with open( args.inputfile ) as f:
        configFiles = [ line.rstrip( '\n' ) for line in f ] 

for configFile in configFiles:
    # Determine if CONFIGS_DIR exists
    if not os.path.exists( CONFIGS_DIR ):
        os.makedirs( CONFIGS_DIR )

    if os.path.exists( configFile ) and not os.path.islink( configFile ):
        moveDir = shutil.move( configFile, CONFIGS_DIR )
        os.symlink( moveDir, configFile )
        print( configFile + ' has been stored in ' + moveDir )
        output.update( { 
            'old_path': os.path.abspath( configFile ),
            'new_path': os.path.abspath( moveDir )
        } )

        #with open( 'data.json', 'w' ) as outfile:
        #    json.dump( output, outfile ) 
                   
    else:
        print( 'File "' + configFile + '" does not exist.' )

if output is not None:
    with open( 'data.json', 'w' ) as outfile:
        json.dump( output, outfile )

# TODO Restore function that uses a backup log to restore all symlinks, or to reverse config file physical locations
# TODO Remove config file function
