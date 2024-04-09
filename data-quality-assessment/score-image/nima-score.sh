#!/bin/bash

# Script to run prediction

./predict \
  --docker-image nima-cpu \
  --base-model-name MobileNet \
  --weights-file $(pwd)/models/MobileNet/weights_mobilenet_technical_0.11.hdf5 \
  --image-source $(pwd)/test/extract-cartoon-update > $(pwd)/output/extract-cartoon-update.json

