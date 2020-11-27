import os
import sys
import eel
import re
eel.init('web')

WORKING_FOLDER = os.path.dirname(sys.argv[0])


@eel.expose
def create_board(board_name):
    if board_name != "":
        if bool(re.match("^(?!^(PRN|AUX|CLOCK\$|NUL|CON|COM\d|LPT\d|\..*)(\..+)?$)[^\x00-\x1f\\?*:\";|/]+$", board_name)):
            eel.create_error("")
            if not os.path.isfile(os.path.join(WORKING_FOLDER, "boards", board_name+".board")):
                with open(os.path.join(WORKING_FOLDER, "boards", board_name+".board"), "w+") as new_board_file:
                    new_board_file.write("")
        else:
            eel.create_error("Name ist nicht gültig!")
    else:
        eel.create_error("Name darf nicht leer sein!")


try:
    eel.start('app.html', port=443, cmdline_args=["--incognito", "--disable-pinch", "--overscroll-history-navigation=0"])
except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("Exiting...")
