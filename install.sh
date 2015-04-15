#!/usr/bin/env bash

#################################################################
# Jupyter (Ipython) notebook custom CSS theme installation
#
# Copyright © 2015 Leon Chen <lchen3@gmail.com>
# MIT License
#


#################################################################

THEME=$1

IPYTHON_PATH=$(ipython locate)

if [ $THEME = "default" ]
then

    echo "Reverting back to default CSS theme."
    cp $IPYTHON_PATH/profile_default/static/custom/custom_default.css $IPYTHON_PATH/profile_default/static/custom/custom.css

else

    # temporarily save default custom CSS
    if [ -e $IPYTHON_PATH/profile_default/static/custom/custom_default.css ]
    then
        echo "Default CSS theme saved."
    else
        echo "Saving default CSS theme..."
        cp $IPYTHON_PATH/profile_default/static/custom/custom.css $IPYTHON_PATH/profile_default/static/custom/custom_default.css
    fi

    # copy new CSS
    cp ./$THEME/custom.css $IPYTHON_PATH/profile_default/static/custom/custom.css 
    echo "CSS themed installed: $THEME"

fi