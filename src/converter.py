from ascii_image import Ascii_image


class Converter:
    def __init__(self) -> None:
        images = []
        current = None

    def load(self, filename, alias="") -> None:
        pass

    def render(self, image="", current=False, file_path="") -> None:
        pass

    def info(self) -> None:
        pass

    def set_width(self, image, width) -> None:
        pass

    def set_height(self, image, height) -> None:
        pass

    def set_brightness(self, image, brightness) -> None:
        pass

    def set_contrast(self, image, contrast) -> None:
        pass

    def save(self, image, file_path) -> None:
        pass

    def load_session(self, filename) -> None:
        pass