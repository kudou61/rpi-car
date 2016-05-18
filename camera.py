# coding=utf-8
import os
import subprocess
import signal


class Camera(object):

    def __init__(self):
        self.status = 0

    def up(self):
        try:
            subprocess.Popen("/home/pi/mjpg/mjpg-streamer/startup.sh",
                             stdout=subprocess.PIPE, shell=True)
            print('camera_up')
        except Exception as e:
            print(e)

    def down(self):
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            if 'mjpg_streamer' in line:
                pid = int(line.split(None,1)[0])
                os.kill(pid,signal.SIGKILL)

    def turn(self):
        if self.status:
            self.down()
            self.status = 0
        else:
            self.up()
            self.status = 1
