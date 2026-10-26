'''
Image  → a grid of pixels             (e.g. 1920 × 1080)
Pixel  → 3 colour numbers             (B, G, R)
Number → 8 bits, value 0–255          (e.g. 200 = 11001000)
Bit    → we use only the last one     (1100100[0])

'H' = 0 1 0 0 1 0 0 0
      ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
      B G R B G R B G   ← last bit of each value
      px 0  px 1  px 2

'''

import cv2, numpy as np

# Encode

img = cv2.imread("photo.jpg") # read image
flat = img.flatten() # copy as 1-D uint8 array thus now it will have pixels in a single line not in a grid 
bits = np.unpackbits(np.frombuffer(b"Hello CV", dtype=np.uint8)) # convert "Hello CV" to 0s and 1s  
flat[:len(bits)] = (flat[:len(bits)] & 0b11111110) | bits   # replace last bit with message's bits
secret = flat.reshape(img.shape) # reshape the array to the original shape of the image
cv2.imwrite("secret.png", secret) # save the image with the hidden message
print(np.abs(secret.astype(int) - img.astype(int)).max())   # expect 1

# Decode

flat = cv2.imread("secret.png").flatten() # read image and flatten it 
print(np.packbits(flat[:64] & 1).tobytes().decode()) # extract the hidden message by taking the last bit of each pixel and converting it to bytes and then decoding it 