import subprocess


class Converter:
    def __init__(self, input, output, type):
        self.input = input
        self.output = output
        self.type = type

    def start(self):
        if self.type == 'MPEG':
            command = 'ffmpeg -i {0} -vcodec mpeg1video  {1}'.format(self.input, self.output)

        elif self.type == 'MJPEG':
            command = 'ffmpeg -i {0}  -vcodec mjpeg  {1}'.format(self.input, self.output)

        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output, error


if __name__ == "__main__":
    a = Converter("../data/airhorse.avi", "../data/airhourse.mpg", "MPEG")
    a = Converter("../data/airhorse.avi", "../data/airhourse.mp4", "MJPEG")
    a.start()