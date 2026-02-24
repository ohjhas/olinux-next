#!/bin/bash
# because of the current economy, we would basically need to free ram, the cache can consume much ram so we now clean it.
echo This script is made to clean the ram cache, note that this MIGHT do unexpected behaviour when running on a live environment, so

read -n 1 -s -r -p "press any key to continue, otherwise close this terminal window..."

sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches 