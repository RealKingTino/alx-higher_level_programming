#!/bin/bash
# Get bytes and display the count
curl -s "$1" | wc -c
