import gradio as gr
import easyocr
import re


r = easyocr.Reader(['en', 'hi'])

def process_image(image, keyword):
    
    result = r.readtext(image, detail=0)
    extracted_text = " ".join(result)

    
    color = "#228B22" 
    if keyword:
        highlighted_text = re.sub(f"({re.escape(keyword)})", 
                                   f"<mark style='background-color: {color};'>{keyword}</mark>", 
                                   extracted_text, 
                                   flags=re.IGNORECASE)
    else:
        highlighted_text = extracted_text

    
    if keyword and keyword.lower() in extracted_text.lower():
        return f"Keyword '{keyword}' found in the text.", highlighted_text
    else:
        return f"Keyword '{keyword}' not found.", highlighted_text

# Gradio interface
interface = gr.Interface(
    fn=process_image,
    inputs=["image", "text"],
    outputs=["text", "html"],
    title=" 📝 TextFinder OCR 📝",
    description="Input your image, get the text 📜 and search for keywords 🔍.....:)"
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
