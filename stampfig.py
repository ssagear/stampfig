from PIL import Image
from PIL.PngImagePlugin import PngInfo
from datetime import datetime as dt

def stamp_fig(figure_path, origin_path, new_path=None, overwrite=True):
    """
    'stamps' saved figure with origin file and date.
    works with ipython notebooks in vscode
    overwrites file by default

    figure_path: path to previously saved figure
    new_path: path to save stamped figure
    """

    targetImage = Image.open(figure_path)

    metadata = PngInfo()
    metadata.add_text("plot_from_file", origin_path)
    metadata.add_text('date_created', str(dt.now()))

    if overwrite==False:
        targetImage.save(new_path, pnginfo=metadata)

    else:
        targetImage.save(figure_path, pnginfo=metadata)

def get_data(path):
    """Returns metadata from saved image."""

    targetImage = Image.open(path)
    return targetImage.text

