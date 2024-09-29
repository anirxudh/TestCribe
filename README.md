
# 📝 TextFinder OCR 📝


![Banner](https://github.com/anirxudh/Python/blob/main/ocr.png)

A web-based prototype that demonstrates the ability to perform Optical Character Recognition (OCR) on an uploaded image (in picture format) containing text in both Hindi and English. The web application also implements a basic keyword search functionality based on the extracted text. The prototype is accessible via a live URL.

The website is hosted using Hugging Face Spaces. Try it out [here](https://huggingface.co/spaces/anirxudh/TextFinder_OCR).

## Approach

1. **OCR Functionality**:  
   The application utilizes a hybrid approach for detecting text in both **English** and **Hindi**. The models used are:
   - **EasyOCR**: Primarily used for accurate **Hindi text** detection.
   - **General OCR Theory (GOT)**: This approach was an excellent way to detect and extract both the languages( English and Hindi, but faced the issues of heavy resource consumption inturn slower response.

   These two models complement each other, providing accurate recognition for both languages.

2. **Document Search**:  
   Once the text exttraction is complete users can input a keyword to search within the extracted text. If the keyword is found, it is highlighted in the output ie, extracted text.

3. **Gradio Interface**:  
   A user-friendly, simple, intuitive, and functional interface has been built using **Gradio**, allowing users to upload images and retrieve text effortlessly.

4. **ColPali + Qwen2VL7BInstruct**:  
   An alternative approach using **ColPali** (via the **Byaldi** library) and **Qwen2VL7BInstruct** was tested. This approach initially faced issues with configuration and memory, but after optimization, produced satisfactory results. However, resource limitations (RAM/CUDA) restricted its use in the final deployment. Locally, this implementation can be run using **Qwen2VLForConditionalGeneration** and **AutoProcessor**.

## Technologies and Libraries Used:

- **Python**: Primary programming language used for developing the application.
- **EasyOCR**: For OCR tasks involving Hindi text detection.
- **Hugging Face Transformers**: Used for the General OCR Theory (GOT) model and Qwen2VL for multi-modal processing.
- **Gradio**: For building an easy-to-use web interface.
- **Hugging Face Spaces**: Deployed the application on this platform.

## How to Use:

1. Clone the repository:
    ```sh
    git clone https://github.com/anirxudh/TextFinder-OCR.git
    ```
2. Install the required libraries (for app.py):
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. To execute the `TextFinder OCR using Qwen-2VL.ipynb`, use a platform like Google Colab or any GPU runtime, ensuring that a GPU is connected. Follow the instructions provided within the notebook files.

## Deployment:

The application has been deployed on **Hugging Face Spaces**. To deploy your own instance, follow these steps:

1. **Create a Hugging Face Account**:  
   Sign up on [Hugging Face](https://huggingface.co/join) to create an account.

2. **Create a New Space**:  
   Navigate to the Spaces tab and create a new Space. Select **Gradio** as the interface type.

3. **Upload the Code**:  
   Upload your project files (such as `app.py` and `requirements.txt`) into the Space.

4. **Set Up Dependencies**:  
   In the Space settings, specify the dependencies listed in the `requirements.txt` file.

5. **Run the Application**:  
   Click "Run" to launch your application. If the application requires GPU support (like for GOT), you'll need a premium plan on Hugging Face.

For more details, visit the [Hugging Face Space Documentation](https://huggingface.co/docs/spaces).

## Output

![Sample Interface 1](https://github.com/anirxudh/TextFinder-OCR/blob/main/Output/Screenshot%202024-09-29%20194658.png)
![Sample Interface 2](https://github.com/anirxudh/TextFinder-OCR/blob/main/Output/Screenshot%202024-09-29%20194802.png)
![Sample Interface 3](https://github.com/anirxudh/TextFinder-OCR/blob/main/Output/Screenshot%202024-09-29%20195304.png)
![Sample Interface 4](https://github.com/anirxudh/TextFinder-OCR/blob/main/Output/Screenshot%202024-09-29%20195404.png)



## References:

1. [GOT-OCR2.0 - GitHub](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)
