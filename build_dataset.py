from cancernet import config
print("Check 1")

from imutils import paths
print("Check 2")
import random, shutil, os
print("Check 3")
originalPaths=list(paths.list_images(config.INPUT_DATASET))
random.seed(7)
random.shuffle(originalPaths)
index=int(len(originalPaths)*config.TRAIN_SPLIT)
trainPaths=originalPaths[:index]
testPaths=originalPaths[index:]
index=int(len(trainPaths)*config.VAL_SPLIT)
valPaths=trainPaths[:index]
trainPaths=trainPaths[index:]
datasets=[("training", trainPaths, config.TRAIN_PATH),
          ("validation", valPaths, config.VAL_PATH),
          ("testing", testPaths, config.TEST_PATH)
]
print("Check 4")

for (setType, originalPaths, basePath) in datasets:
        print(f'Building {setType} set')
        if not os.path.exists(basePath):
                print(f'Building directory {basePath}')
                os.makedirs(basePath)
        for path in originalPaths:
                file=path.split(os.path.sep)[-1]
                label=file[-5:-4]
                labelPath=os.path.sep.join([basePath,label])
                if not os.path.exists(labelPath):
                        print(f'Building directory {labelPath}')
                        os.makedirs(labelPath)
                newPath=os.path.sep.join([labelPath, file])
                shutil.copy2(path,newPath)
