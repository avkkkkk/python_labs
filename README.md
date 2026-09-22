**Описание работы:**

Реализован скрипт для сборки информации о системе, в которой он запускается. 

Собираемые параметры:
1. platform.platform() - операционная система и ее версия в обобщенном виде
2. platform.release() - версия операционной системы
3. platform.version() - более детальная версия ОС
4. platform.node() - сетевое имя компьютера
5. platform.python_version() - используемая версия интерпретатора python
6. sys.executable - полный путь до исполняемого файла python, который запустил скрипт
7. os.cpu_count() - количество логических процессоров (ядер/потоков)
8. getpass.username() - имя текущего пользователя, от имени которого запущен скрипт

**Пример работы программы в разных операционных системах:**
1. Windows 11
<img width="1273" height="395" alt="изображение" src="https://github.com/user-attachments/assets/627c82ce-6e48-4fc3-ad46-7bb940bd653a" />

2. Kali Linux
<img width="1041" height="355" alt="изображение" src="https://github.com/user-attachments/assets/a2cac4a2-274e-43dd-a921-d5f6d1104d19" />
