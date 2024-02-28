


class Image:
    def __init__(self, filename, alias="") -> None:
        self.filename = filename
        self.alias = alias
        self.actual_width = None
        self.actual_height = None
        self.width = 50 # Default width is 50
        self.height = None
        self.brightness = 1 # Default brightness is 1
        self.contrast = 1 # Default contrast is 1 

    def set_width(self, width) -> None:
        self.width = width
    
    def set_height(self, height) -> None:
        self.height = height
    
    def set_brightness(self, brightness) -> None:
        self.brightness = brightness
    
    def set_contrast(self, contrast) -> None:
        self.contrast = contrast

    def info(self) -> None:
        print(f"Image: {self.filename}")
        print(f"Alias: {self.alias}")
        print(f"Size: {self.width}")
        print(f"Target Size: {self.height}")
        print(f"Brightness: {self.brightness}")
        print(f"Contrast: {self.contrast}")