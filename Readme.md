# Компиляция в .exe файл

  -1) Запускаем командную строку из данного каталога
  -2) Набираем в командной строке команду "pyinstaller main.py"
  -3) После успешной выволнении команды перейти в директорию "\sample_face_recognition\dist\main" и в команоной
  строке выполнить команду "main.exe", если при выполнении кманды произойдет ошибка
  " No such file or directory: '...\\sample_face_recognition\\dist\\main\\mtcnn\\data\\mtcnn_weights.npy'
[14812] Failed to execute script main", то необходимо папку "mtcnn", которая находится в директории
    "...\sample_face_recognition", перенести в директорию "...\dist\main"
   -4) еще раз выполнить команду "main.exe" в директории "\sample_face_recognition\dist\main"


  -Замечание: Файл "sample_face_recognition\src\python\application\mian.py" был перенесен в
  ""sample_face_recognition\" для компиляции в .exe
  - Также необходимо добавить свой путь в файле "sample_face_recognition\src\python\facenet\utils\__init__.py",
  нопример так 'C:/Work_space/sample_face_recognition/cascade/haarcascade_frontalface_default.xml