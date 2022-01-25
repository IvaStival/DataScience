import xml.etree.ElementTree as Xet
import pandas as pd
import os
import shutil

files_list = os.listdir("../dataset/BCCD/Annotations/")

columns_name = ["filename", "width", "height", "depth", "cell_name", "xmin", "ymin", "xmax", "ymax"]

df = pd.DataFrame(columns=columns_name)

count = 0
for file in files_list:
    if file.endswith(".xml"):

        xml_parse = Xet.parse("../dataset/BCCD/Annotations/"+file)

        root = xml_parse.getroot()
        filename = root.findall('filename')[0].text

        size = []
        for i in root.findall('size')[0]:
            size.append(int(i.text))

        bnd_list = []
        for i in root.findall("object"):
            name = i.findall("name")[0].text

            for bnd in i.findall("bndbox"):
                xmin = bnd.findall("xmin")[0].text
                ymin = bnd.findall("ymin")[0].text
                xmax = bnd.findall("xmax")[0].text
                ymax = bnd.findall("ymax")[0].text

            bnd_list.append((name, xmin, ymin, xmax, ymax))

        for bnd in bnd_list:
            df.loc[count, :] = [filename, size[0], size[1], size[2], bnd[0], bnd[1], bnd[2], bnd[3], bnd[4]]
            count += 1

df = df.sort_values("filename")
df = df.reset_index(drop=True)
df.to_csv("../dataset/data.csv")
