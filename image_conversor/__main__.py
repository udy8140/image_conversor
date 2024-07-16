from PIL import Image
import os

if __name__ == "__main__":
    _SOURCE_PATH_ = ""
    _DESTINATION_PATH_ = ""
    files = os.listdir(_SOURCE_PATH_)

    for img in [m for m in files if m.lower().endswith(".cr2")]:
        print(img)
        _ = Image.open(_SOURCE_PATH_ + img)
        _.convert("RGB")
        _.save(_DESTINATION_PATH_ + img.replace("CR2", "JPG"))
        continue