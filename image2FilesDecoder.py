from PIL import Image
from pathlib import Path

newLine = b'\new\n\rL'

def decode_encrypted_images(folder: Path):

    for pic in folder.iterdir():
        img = Image.open(str(pic))
        data = img.getdata()
        totalData = []
        for pixel in data:
            totalData.extend(list(pixel))
        decryptedData = bytes(totalData)
        try:
            decryptedData = eval(
                decryptedData[:decryptedData.rfind(b'}')+1].decode())
        except:
            decryptedData.replace(b'\\', '')
            decryptedData = eval(
                decryptedData[:decryptedData.rfind(b'}')+1].decode())
        decryptedData['data'] = decryptedData['data'][:-14]

        filePathObj = Path(decryptedData['path'])
        Path(filePathObj.parent).mkdir(
            parents=True, exist_ok=True)

        writeBytes = decryptedData['data'].split(newLine)
        with open(str(filePathObj), 'wb') as wb:
            wb.writelines(writeBytes)


if __name__ == '__main__':
    # ./encryptedImagesFolder is the name of the enrypted folder
    decode_encrypted_images(folder=Path(r"./encryptedImagesFolder"))
