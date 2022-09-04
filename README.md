# py-folder2ImageEncoderDecoder
Simple python folder to image encoder and decoder.

Usage
-----
folder2ImageEncoder.py
-----
```python
if __name__ == '__main__':
    # ./files is the name of the folder you want to encrypt
    encode_folder(folder=Path(r'./files'))
```
-----
image2FilesDecoder.py
-----
```python
if __name__ == '__main__':
    # ./encryptedImagesFolder is the name of the enrypted folder
    decode_encrypted_images(folder=Path(r"./encryptedImagesFolder"))
```

