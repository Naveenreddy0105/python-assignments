'''5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method.
Demonstrate polymorphism by passing different types of media to this function.'''


from abc import ABC,abstractmethod


class Media (ABC) :
    def play (self):
        pass

class Audio(Media):
    def play (self):
        print ("Playing.mp3 file...")

class Video (Media):
    def play (self):
        print ("Playing.mp4 file...")

class Livestream(Media):
    def play(self):
        print("Playing live stream...")

def start_media(media:Media):
    media.play()

audio = Audio()
video = Video()
live_stream =Livestream()

start_media(audio)
start_media(video)
start_media(live_stream)