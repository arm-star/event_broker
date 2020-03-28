import logging
import os
import sys
from shutil import copyfile
import win32file
import win32con
import difflib

FILE_LIST_DIRECTORY = 0x0001
PATH_TO_WATCH = r'.\Data_files'

FILES_LIST = os.listdir(PATH_TO_WATCH)

HDIR = win32file.CreateFile(
    PATH_TO_WATCH, FILE_LIST_DIRECTORY, win32con.FILE_SHARE_READ
    | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE, None,
    win32con.OPEN_EXISTING, win32con.FILE_FLAG_BACKUP_SEMANTICS, None)


ACTIONS = {
    1: "Created",
    2: "Deleted",
    3: "Updated",
    4: "Renamed from something",
    5: "Renamed to something"
}


