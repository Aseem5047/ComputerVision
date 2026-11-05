# part 1 - quality sweep

import cv2, numpy as np
img = cv2.imread("photo.jpg")
for q in (95, 50, 10, 2):
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, q])   # compress in memory
    dec = cv2.imdecode(buf, cv2.IMREAD_COLOR)                             # decompress
    mse = np.mean((img.astype(np.float32) - dec) ** 2)
    print(f"q={q:3d}  size={buf.size/1024:7.1f} KB  PSNR={10*np.log10(255**2/mse):5.1f} dB")
    cv2.imwrite(f"q{q}.png", dec)                                         # lossless copy to inspect

# part 2 - inside a block

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
block = gray[100:108, 100:108] - 128          # one 8×8 block, centred around 0
np.set_printoptions(precision=0, suppress=True)
print(cv2.dct(block))                          # 64 pattern weights