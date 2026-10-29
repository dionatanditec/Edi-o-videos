import random, numpy as np
from PIL import Image, ImageDraw, ImageFilter
random.seed(7); np.random.seed(7)
W,H=1080,1920
def blur(im,r): return im.filter(ImageFilter.GaussianBlur(r))
# parede: gradiente quente + luz vindo da esquerda
y,x=np.mgrid[0:H,0:W].astype(np.float32)
base=np.array([196,176,152],np.float32)
light=np.clip(1.15-(x/W)*0.45-(y/H)*0.25,0.55,1.2)
wall=(base[None,None,:]*light[...,None]).clip(0,255).astype(np.uint8)
bg=Image.fromarray(wall).convert("RGB")
d=ImageDraw.Draw(bg)
wood=(66,44,30)
pal=[(122,64,52),(54,70,84),(176,150,104),(88,96,70),(150,110,80),(60,52,48),(190,170,140),(110,70,90)]
def shelf(x0,x1):
    d.rectangle([x0,230,x1,1400],fill=wood)
    ys=[230,520,810,1100,1400]
    for a,b in zip(ys[:-1],ys[1:]):
        d.rectangle([x0+14,a+14,x1-14,b-14],fill=(34,24,18))
        xx=x0+16
        while xx<x1-40:
            w=random.randint(22,46); h=random.randint(150,235)
            c=random.choice(pal); d.rectangle([xx,b-14-h,xx+w,b-14],fill=c); xx+=w+random.randint(0,4)
            if random.random()<0.12: xx+=random.randint(30,70)
    for yy in ys[1:-1]: d.rectangle([x0,yy-10,x1,yy+4],fill=wood)
shelf(0,330); shelf(750,1080)
# quadro abstrato
d.rectangle([380,300,700,560],fill=(52,38,30)); d.rectangle([392,312,688,548],fill=(205,188,160))
d.ellipse([430,350,600,520],fill=(176,100,78)); d.rectangle([560,400,660,520],fill=(78,104,108))
bg=blur(bg,9)
# luzes quentes (fita de LED sob as prateleiras) e bokeh
glow=Image.new("RGB",(W,H),(0,0,0)); g=ImageDraw.Draw(glow)
for yy in (516,806,1096):
    g.rectangle([16,yy,314,yy+8],fill=(255,190,90)); g.rectangle([766,yy,1064,yy+8],fill=(255,190,90))
for _ in range(14):
    cx,cy=random.randint(640,1060),random.randint(150,1250); r=random.randint(24,60)
    g.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(120,80,30))
glow=blur(glow,14)
bg=Image.fromarray(np.clip(np.asarray(bg,np.float32)+np.asarray(glow,np.float32)*0.9,0,255).astype(np.uint8))
# planta desfocada (esquerda baixo)
pl=Image.new("RGBA",(W,H),(0,0,0,0)); p=ImageDraw.Draw(pl)
for _ in range(26):
    cx=random.randint(-20,260); cy=random.randint(980,1330); rx=random.randint(25,45); ry=random.randint(90,170)
    p.ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=(random.randint(30,50),random.randint(70,100),random.randint(40,60),255))
bg.paste(blur(pl,10),(0,0),blur(pl,10))
# encosto da cadeira (couro escuro) atrás dos ombros
ch=Image.new("RGBA",(W,H),(0,0,0,0)); c=ImageDraw.Draw(ch)
c.rounded_rectangle([130,800,950,1500],radius=230,fill=(38,30,27,255))
c.rounded_rectangle([190,860,890,1500],radius=190,fill=(52,42,38,255))
ch=blur(ch,5); bg.paste(ch,(0,0),ch)
bg=bg.convert("RGB"); bg.save("bg2.png")
# mesa (primeiro plano)
top=1370
desk=np.zeros((H,W,4),np.uint8)
yy=np.arange(top,H)[:,None]
t=(yy-top)/(H-top)
col=np.stack([ (92-40*t), (58-28*t), (38-20*t) ],-1)
grain=np.random.normal(0,5,(H-top,W,1))+np.sin(np.arange(W)*0.05)[None,:,None]*3
desk[top:,:,:3]=np.clip(col+grain,0,255).astype(np.uint8)
desk[top:,:,3]=255
dk=Image.fromarray(desk)
dd=ImageDraw.Draw(dk)
dd.rectangle([0,top,W,top+6],fill=(150,108,76,255))        # brilho da borda
dd.rectangle([0,top+6,W,top+60],fill=(104,70,48,150))
# objetos: caderno e copo desfocados
obj=Image.new("RGBA",(W,H),(0,0,0,0)); o=ImageDraw.Draw(obj)
o.rounded_rectangle([90,1470,470,1640],radius=8,fill=(214,204,186,255)); o.rectangle([90,1470,110,1640],fill=(110,60,50,255))
o.rounded_rectangle([860,1420,940,1560],radius=14,fill=(190,210,214,170))
obj=blur(obj,3)
dk=Image.alpha_composite(dk,obj)
a=dk.getchannel("A").filter(ImageFilter.GaussianBlur(1.5)); dk.putalpha(a)
dk.save("desk2.png")
