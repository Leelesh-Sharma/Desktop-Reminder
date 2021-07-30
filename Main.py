import time
from plyer import notification
while True:
    notification.notify(
        title = 'TITLE',
        message = 'MESSAGE BITCH!!!!!!!!!!',
        app_icon = 'D:\Projects Pyhton\Desktop Reminder\Oxygen-Icons.org-Oxygen-Places-mail-message.ico',
        timeout = 1
    )

time.sleep(5)