# %%

import os
import pandas as pd
import sys
import jupyterlab as jp
import glob
import graphs as gr
'''
my_folder_path = "C:\\data_analysis_neiro"


def create_csv(folder_path=os.path.dirname(os.path.realpath(sys.argv[0])),
               name="combined_data"):
    """ создание нового csv файла с именем name на основе всех найденных
    csv-файлов в директории folder_path с сохранением в папку, где лежит
    данный код по  умолчанию поиск в паке, где лежит данный код """

    file_paths = []
    merged_frame = None

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    print(file_paths)

    merged_frame = pd.concat([merged_frame, [pd.read_csv(f, delimiter=",") for f in file_paths]], ignore_index=True)
    merged_frame.to_csv(name + ".csv", index=False)
    return merged_frame


create_csv(folder_path=my_folder_path)
# добавить линейный график (ф1, ф2)
'''
gr.correlation_map()
'''# line_plot()
subplots(["AF3", "AF4"])
subplots(["F3", "F4"])
subplots(["FC5", "FC6"])
subplots(["F7", "F8"])
subplots(["T7", "T8"])
subplots(["P7", "P8"])
subplots(["O1", "O2"])

column_names.insert(0, 'iter')
column_names.insert(0, 'class')
for i in range(len(column_names)):
    scatter_plots(column_names[i+2], column_names[15-i], data)


all_in_one_lineplot()'''
