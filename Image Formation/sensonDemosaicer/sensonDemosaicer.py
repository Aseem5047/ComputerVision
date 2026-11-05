import cv2, numpy as np, matplotlib.pyplot as plt
img = cv2.cvtColor(cv2.imread("photo.jpg"), cv2.COLOR_BGR2RGB).astype(np.float32) / 255
img = img[: img.shape[0]//2*2, : img.shape[1]//2*2]                  # even H and W
raw = np.zeros(img.shape[:2], np.float32)                             # one value per pixel
raw[0::2, 0::2] = img[0::2, 0::2, 0]                                  # R
raw[0::2, 1::2] = img[0::2, 1::2, 1]; raw[1::2, 0::2] = img[1::2, 0::2, 1]   # G, G
raw[1::2, 1::2] = img[1::2, 1::2, 2]                                  # B
demo = np.dstack([raw[0::2, 0::2], (raw[0::2, 1::2] + raw[1::2, 0::2]) / 2, raw[1::2, 1::2]])
for i, (im, t) in enumerate([(img, "original"), (raw, "raw mosaic"), (demo, "superpixel demosaic")]):
    plt.subplot(1, 3, i + 1); plt.imshow(im, cmap="gray"); plt.title(t); plt.axis("off")
plt.show()