from simple_image_download import simple_image_download as simp 

response = simp.simple_image_download
keyword = ["johny deep jack", "jack sparrow"]

for kw in keyword :
    response().download(kw, 300)
