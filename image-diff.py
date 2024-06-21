import streamlit as st                                                                                                                               
from PIL import Image                                                                                                                                
from imagehash import average_hash                                                                                                                   
                                                                                                                                                    
st.title("Image Comparison")                                                                                                                         
                                                                                                                                                    
image1 = st.file_uploader("Select Image 1", type=["jpg", "jpeg", "png"])                                                                             
image2 = st.file_uploader("Select Image 2", type=["jpg", "jpeg", "png"])                                                                             
                                                                                                                                                    
if image1 and image2:                                                                                                                                
    hash0 = average_hash(Image.open(image1))                                                                                                         
    hash1 = average_hash(Image.open(image2))                                                                                                         
                                                                                                                                                    
    cutoff = 5                                                                                                                                       
                                                                                                                                                    
    if hash0 - hash1 < cutoff:                                                                                                                       
        st.write("Images are similar")                                                                                                               
    else:                                                                                                                                            
        st.write("Images are not similar")  