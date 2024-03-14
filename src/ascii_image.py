from PIL import Image


class Ascii_image:
    def __init__(self, filename, alias="") -> None:
        self.filename = filename
        self.alias = alias
        self.actual_width = None
        self.actual_height = None
        self.width = 50 # Default width is 50
        self.height = None
        self.brightness = 1 # Default brightness is 1
        self.contrast = 1 # Default contrast is 1
        self.image = None
        self.pixelated = None

        self.load()

    def load(self) -> None:
        with Image.open(f"../images/{self.filename}") as img:
            self.image = img.convert("L")
            self.actual_width, self.actual_height = img.size
            self.calc_ratio()
             
    def pixelate(self) -> None:
        """Converts the image into a 2D-list size: height x width
        where each element is the average number value of the pixels
        in the corresponding area of the original image."""
        self.pixelated = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                x1 = int(j * (self.actual_width / self.width))
                x2 = int((j + 1) * (self.actual_width / self.width))
                y1 = int(i * (self.actual_height / self.height))
                y2 = int((i + 1) * (self.actual_height / self.height))
                area = self.image.crop((x1, y1, x2, y2))
                self.pixelated[i][j] = int(sum(area.getdata()) / len(area.getdata()))
    
    def render(self) -> None:
        """Renders the pixelated image."""
        if not self.pixelated:
            self.pixelate()
        for row in self.pixelated:
            for pixel in row:
                print(self.get_char(pixel), end="")
            print()

    def get_char(self, pixel) -> str:
        """Returns a character based on the pixel value."""
        chars = "@%#*+=-:. "
        return chars[int(pixel / 255 * len(chars))-1]

    def calc_ratio(self) -> None:
        ratio = self.actual_width / self.actual_height
        self.height = int(self.width / ratio)

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
