# Alexa-HSU
Using Alexa to controll IOT devices on the HSU campus

Created as part of the 2018 LUMBERHACKS hackathoon(Placed 3rd)

This works by using a AWS queue to controll clicks on a computer. The computer clicks on a debug aplication for controlling a projector.

Going into the future we wish to replace the computer with the debug app with a rasbery pie talking directly to a projector or device via USB, Serial, or over the network.

secrets.py is an .gitignored file that contains our aws conection info, it is secered by the os's file security.

Using Python
    Python Libraries:
        PyAutoGUI, Boto3
