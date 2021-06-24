pyrcc5 -o font_rc.py resource/font.qrc
pyrcc5 -o image_rc.py resource/image.qrc
pyuic5 -o ui_main_window.py resource/terminal.ui
pyuic5 -o ui_settings_window.py resource/settings.ui
pause