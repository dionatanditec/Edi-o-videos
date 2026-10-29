import sys, subprocess, numpy as np, cv2
import mediapipe as mp
from mediapipe.tasks import python as mpp
from mediapipe.tasks.python import vision
src, model, out = sys.argv[1:4]
W,H,FPS=576,864,30
dec=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-vf",f"fps={FPS}","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
enc=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","gray","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","ffv1",out],stdin=subprocess.PIPE)
opts=vision.ImageSegmenterOptions(base_options=mpp.BaseOptions(model_asset_path=model),output_confidence_masks=True,output_category_mask=False)
prev=None; n=0
with vision.ImageSegmenter.create_from_options(opts) as seg:
    while True:
        buf=dec.stdout.read(W*H*3)
        if len(buf)<W*H*3: break
        rgb=np.frombuffer(buf,np.uint8).reshape(H,W,3).copy()
        m=seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB,data=rgb)).confidence_masks[0].numpy_view().reshape(H,W).astype(np.float32)
        if m.mean()>0.5: m=1-m   # garante que 1 = pessoa
        prev=m if prev is None else 0.55*m+0.45*prev   # suaviza no tempo
        b=(prev>0.5).astype(np.uint8)
        k,lab,st,_=cv2.connectedComponentsWithStats(b)
        if k>1:
            keep=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); b=(lab==keep).astype(np.uint8)
        soft=cv2.GaussianBlur(cv2.erode(b,np.ones((3,3),np.uint8)).astype(np.float32),(0,0),1.2)
        enc.stdin.write((np.clip(soft,0,1)*255).astype(np.uint8).tobytes()); n+=1
enc.stdin.close(); enc.wait(); print("frames",n)
