# recortar_tiles_vb.py
from PIL import Image
import math
import os

def split_image_to_tiles(input_path, out_dir, rows, cols, output_format='WEBP', quality=60, max_side=None):
    os.makedirs(out_dir, exist_ok=True)
    im = Image.open(input_path).convert('RGB')
    w, h = im.size
    tw = math.ceil(w / cols)
    th = math.ceil(h / rows)
    for r in range(rows):
        for c in range(cols):
            left = c*tw
            upper = r*th
            right = min(left+tw, w)
            lower = min(upper+th, h)
            tile = im.crop((left, upper, right, lower))
            if max_side:
                mw = max(tile.size)
                if mw > max_side:
                    scale = max_side / mw
                    tile = tile.resize((int(tile.size[0]*scale), int(tile.size[1]*scale)), Image.LANCZOS)
            out_name = f"tile_r{r}_c{c}.{output_format.lower()}"
            out_path = os.path.join(out_dir, out_name)
            save_kwargs = {}
            if output_format.upper() in ('JPEG','WEBP'):
                save_kwargs['quality'] = quality
                save_kwargs['optimize'] = True
            tile.save(out_path, format=output_format, **save_kwargs)
    print("Tiles gerados em", out_dir)

if __name__ == '__main__':
    split_image_to_tiles(
        input_path='map_vila_bethania.png',  # sua imagem de mapa
        out_dir='tiles_vb',
        rows=5, cols=5,
        output_format='WEBP',
        quality=50,
        max_side=600
    )
