#!/bin/bash

RASPIS_LIST_FILE=raspis.lst
RASPI_REPO_PATH="/home/pi/scirocco-pyclient"

function raspis_copy_id (){

    for r in $(cat $RASPIS_LIST_FILE); do ssh-copy-id pi@$r ; done

}

function raspis_send_to_all (){

    for r in $(cat $RASPIS_LIST_FILE); do ssh pi@$r "$1" ; done

}

function raspis_update_repo (){
    raspis_send_to_all "cd $RASPI_REPO_PATH && git checkout develop && git pull && python3 setup.py install"
}

function raspis_install_repo () {
    raspis_send_to_all "git clone https://github.com/eloylp/scirocco-pyclient.git $RASPI_REPO_PATH"
}