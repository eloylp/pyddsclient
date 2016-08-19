#!/bin/bash

RASPIS_LIST_FILE=raspis.lst
RASPI_REPO_PATH="/home/pi/scirocco-pyclient"

function to_all_raspis (){

    for r in $(cat $RASPIS_LIST_FILE); do ssh pi@$r "$1" ; done

}

function update_repo (){
    to_all_raspis "cd $RASPI_REPO_PATH && git checkout develop && git pull"
}

function install_repo () {
    to_all_raspis "git clone https://github.com/eloylp/scirocco-pyclient.git $RASPI_REPO_PATH"
}