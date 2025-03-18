#!/bin/bash

MODEL_FILE="en_us_cmuartic_jets_cpu.addon"
MODEL_DIR="assets/models"
MODEL_PATH="${MODEL_DIR}/${MODEL_FILE}"

if [ ! -f "${MODEL_PATH}" ]; then
    
    echo "Downloading model..."
    
    wget -q --show-progress https://huggingface.co/balacoon/tts/resolve/main/${MODEL_FILE} -O "${MODEL_PATH}"
    
    if [ $? -ne 0 ]; then
    
        echo "Error downloading model. Exiting."
        exit 1
    
    fi
    
    echo "Model downloaded successfully."

else

    echo "Model already exists."

fi

echo "Script completed."

python app.py &