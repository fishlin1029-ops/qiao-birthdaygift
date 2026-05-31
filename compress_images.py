import os
from PIL import Image

asset_dir = '/Users/linyuping/Desktop/BBDBB/asset'

png_files = [
    'id3B.png', 'id1Bcat.png', 'id4Atravel.png', 'id2Btravel.png',
    'id1Amusic.png', 'id5Bcat.png', 'id7Btravel.png', 'id3Ahealth.png',
    'id6Ahealth.png', 'id7Amusic.png', 'id5Ahealth.png',
]

for name in png_files:
    path = os.path.join(asset_dir, name)
    if not os.path.exists(path):
        print(f'SKIP: {name} not found')
        continue

    orig_size = os.path.getsize(path)
    img = Image.open(path)

    out_name = name.rsplit('.', 1)[0] + '.webp'
    out_path = os.path.join(asset_dir, out_name)

    if img.mode in ('RGBA', 'LA', 'P'):
        img.save(out_path, 'WEBP', quality=80, method=4)
    else:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(out_path, 'WEBP', quality=80, method=4)

    new_size = os.path.getsize(out_path)
    ratio = (1 - new_size / orig_size) * 100
    print(f'{name}: {orig_size/1024:.0f}KB -> {out_name}: {new_size/1024:.0f}KB (-{ratio:.0f}%)')

room_path = os.path.join(asset_dir, 'room.jpeg')
if os.path.exists(room_path):
    orig_size = os.path.getsize(room_path)
    img = Image.open(room_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    out_path = os.path.join(asset_dir, 'room.webp')
    img.save(out_path, 'WEBP', quality=82, method=4)
    new_size = os.path.getsize(out_path)
    ratio = (1 - new_size / orig_size) * 100
    print(f'room.jpeg: {orig_size/1024:.0f}KB -> room.webp: {new_size/1024:.0f}KB (-{ratio:.0f}%)')
