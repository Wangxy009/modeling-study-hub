from PIL import Image, ImageDraw, ImageFont

W,H=1000,760
im=Image.new("RGB",(W,H),(28,54,58));d=ImageDraw.Draw(im)
colors=[(240,199,94),(204,226,220),(183,76,62),(39,93,120),(255,255,255)]
for x in range(70,940,95): d.line((x,80,x,680),fill=(55,83,86),width=1)
for y in range(80,681,75): d.line((70,y,930,y),fill=(55,83,86),width=1)
nodes=[(125,150,245,235,0),(390,95,560,205,1),(680,165,875,275,3),(265,390,440,505,2),(590,420,820,555,0)]
for idx,(x1,y1,x2,y2,c) in enumerate(nodes):
    d.rectangle((x1,y1,x2,y2),fill=colors[c])
    d.text((x1+16,y1+13),f"0{idx+1}",fill=(24,40,42),font=ImageFont.load_default(size=24))
for a,b in [((245,193),(390,150)),((560,150),(680,220)),((780,275),(705,420)),((590,487),(440,447)),((350,390),(225,235))]:
    d.line((*a,*b),fill=(229,238,234),width=5)
d.text((72,625),"PROBLEM  >  MODEL  >  EVIDENCE  >  PAPER",fill=(240,199,94),font=ImageFont.load_default(size=24))
im.save("/Users/wangxiaoya/Documents/Codex/modeling-study-hub/assets/writer-map.png")
