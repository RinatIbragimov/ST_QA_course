import os

current_dir = os.path.abspath(os.path.dirname("lesson2_step7_os_path.py")) # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file_for_lesson2_steps7_8.txt') # добавляем к этому пути имя файла
#вместо "lesson2_step7_os_path.py" или "__lesson2_step7.py__" можно указывать __file__
# __file__ - это название вашего скрипта. Это текущий исполняемый файл, в котором написан этот код.
#element.send_keys(file_path)
print(current_dir)
print(file_path)
