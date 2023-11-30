import importlib.resources
from playsound import playsound


class SoundsManager:
    @classmethod
    def play_sound(cls, path):
        playsound(path)

    @classmethod
    def _play_static_sound(cls, filename):
        sound_path = importlib.resources.path(
            "toolbox.managers.static.sounds",
            filename,
        )
        with sound_path as path:
            cls.play_sound(path)

    @classmethod
    def play_beep(cls):
        cls._play_static_sound("beep.wav")

    @classmethod
    def play_success(cls):
        cls._play_static_sound("success.wav")
