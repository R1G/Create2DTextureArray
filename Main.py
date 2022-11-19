import sys
import os
import json
import cv2 as cv

import CreateTexArray as CTA
import GetFromPrefixes as GFP

if __name__ == "__main__":
    f = open('prefixes.json')
    prefixes = json.load(f)
    f.close()

    textureGroups = GFP.GetFromPrefixes('GQ/', prefixes)
    for i in range(len(prefixes)):
        array = CTA.create2DImageArray(textureGroups[i])
        filename = prefixes[i] + '.jpg'
        cv.imwrite(filename, array)

    





