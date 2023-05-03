#!/bin/bash

git clone https://github.com/algorand/sandbox.git

cp config.zk sandbox
cp DevModeNetwork.json sandbox/images/algod/

cd sandbox && ./sandbox up zk