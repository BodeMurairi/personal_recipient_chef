#!/usr/bin/env python3
import os
import base64
from PIL import Image


def encode_image_to_base64(path):
    """Read an image file and encode it in base64 for sending to AI"""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def encode_image_for_AI(image_paths: list):
    """Encode images for AI"""
    images_for_ai = []

    for path in image_paths:
        if os.path.isfile(path):
            images_for_ai.append({
                "type": "image",
                "data": encode_image_to_base64(path),
                "filename": os.path.basename(path)
            })
        else:
            print(f"Warning: {path} does not exist and will be ignored.")

    return images_for_ai

