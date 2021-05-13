from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import streamlit as st 
from PIL import ImageDraw
from PIL import ImageFont

KEY = "a06caf9814cc40e198ca077918c78d33"
ENDPOINT = "https://20210513.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
#ComputerVisionClient オブジェクトを作成します。

#物体検出用関数
def detected_objects(filepath):
    local_image = open(filepath, "rb")
    detected_objects_result = computervision_client.detect_objects_in_stream(local_image)
    objects =detected_objects_result.objects
    return objects

#タグ取得用関数
def get_tags(filepath):
    local_image = open(filepath, "rb")
    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags
    tags_name=[]
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name

st.title('Object detection App')
uploaded_image=st.file_uploader('Choose an image...',type=['jpeg','jpg','png'])

if uploaded_image is not None:
    img=Image.open(uploaded_image)
    img_path=f'folder/{uploaded_image.name}'
    img.save(img_path) #fileパスの表示

    objects = detected_objects(img_path)
    
    draw = ImageDraw.Draw(img)
    for object in objects:
        x=object.rectangle.x
        y=object.rectangle.y
        w=object.rectangle.w
        h=object.rectangle.h
        capt=object.object_property

        font=ImageFont.truetype(font='./Helvetica 400.ttf', size=50) #font情報
        text_w, text_h = draw.textsize(capt,font=font)

        draw.rectangle([(x,y),(x+w),(y+h)],fill=None, outline='green',width=4)
        draw.rectangle([(x,y),(x+text_w),(y+text_h)],fill='green')
        draw.text((x,y),capt,fill='white',font=font)
    st.image(img) #画像の表示


    tags_name=get_tags(img_path)
    tags_name=', '.join(tags_name)
    st.markdown('**recognized tags**')
    st.markdown(f'>{tags_name}')
