#!/bin/bash

URL="https://adventofcode.com/2021/day/"

echo "Getting the input for the following number of days: $1"

for i in {0..$1}; do wget -qq -- $URL/$i$/input; done
