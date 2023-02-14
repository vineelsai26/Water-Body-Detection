import os

for i in os.listdir("."):
    if os.path.exists(i) and i.endswith("_B3.TIF"):
        folderName = i.replace("_B3.TIF", "")
        os.mkdir(folderName)
        os.rename(i, folderName + "/" + i)

        i = i.replace("_B3.TIF", "_B5.TIF")
        os.rename(
            i,
            folderName + "/" + i
        )

        i = i.replace("_B5.TIF", "_B6.TIF")
        os.rename(
            i,
            folderName + "/" + i
        )

        i = i.replace("_B6.TIF", "_B7.TIF")
        os.rename(
            i,
            folderName + "/" + i
        )
