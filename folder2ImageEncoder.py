from PIL import Image
from pathlib import Path

encryptedImagesFolder = 'encryptedImagesFolder'

Path(f"./{encryptedImagesFolder}").mkdir(parents=True, exist_ok=True)
newLine = b'\new\n\rL'

def encode_data_to_image(data: bytes, imagePath: str):
    data += b'FINISH_OF_DATA'

    data = str(
        {
            'path': imagePath,
            'data': data
        }
    )
    data = data.encode()
    n = int((len(data)/3)**0.5) + 1
    print(n, len(data))

    img = Image.new('RGB', (n, n))
    encryptedPixelsList = []
    pixel = []

    if len(data) % 3 != 0:
        data += (3 - (len(data) % 3)) * b'\x00'
    for i, Byte in enumerate(data):
        if i % 3 == 2:
            pixel.append(Byte)
            encryptedPixelsList.append(tuple(pixel))
            pixel = []
        else:
            pixel.append(Byte)
    
    for _ in range(len(encryptedPixelsList), n**2):
        encryptedPixelsList.append((0, 0, 0))

    img.putdata(encryptedPixelsList)
    imagePath = imagePath.replace('\\', '_')
    img.save(f'./{encryptedImagesFolder}/{imagePath}.png')

def encode_folder(folder: Path):

    for file in folder.iterdir():
        if not file.is_dir():
            with open(str(file), 'rb') as rb:
                data = rb.readlines()
                encode_data_to_image(
                    data=newLine.join(data),
                    imagePath=str(file)
                )
        else:
            encode_folder(folder=file)


if __name__ == '__main__':
    # ./files is the name of the folder you want to encrypt
    encode_folder(folder=Path(r'./files'))