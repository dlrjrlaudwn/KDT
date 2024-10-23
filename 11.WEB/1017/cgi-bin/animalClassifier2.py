import os
import cgi
import cgitb
import torch
from PIL import Image
import sys
import codecs
from animalmodel import VGG16WithFC, joo_preprocessing_img,joo_predict_value  # Adjust based on your model's definition

# Enable CGI error reporting
cgitb.enable()

# Global Variables
SCRIPT_MODE = True
model_file = None

# Load models at the start of the script
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())  # Set stdout to utf-8

# Load the model from disk
model_path = os.path.join(os.path.dirname(__file__), 'models', 'lion_model.pth')

# Initialize the model and load the state dict
try:
    model_file = VGG16WithFC()  # Instantiate your model class
    model_file.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model_file.eval()  # Set the model to evaluation mode
    print(f"Model loaded successfully from: {model_path}")
except Exception as e:
    print(f"Error loading model from {model_path}: {e}")

# Function to show HTML response
def showHTML(msg):
    print("Content-Type: text/html; charset=utf-8")
    print("""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
        <meta charset="UTF-8">
        <title> 🦁 사자 판별 🦁 </title>
        <style>
            body { background-color: #f2f5f8; }
            /* Other styles here... */
        </style>
        </head>
        <body>
        <form enctype="multipart/form-data" method="post">
        """)
    print(f"""
            <div class='wrap'>
                <div class='wrap_inner'>
                    <div class='title'> 사자 판별 모델 </div>
                    <div class='u-list'>
                        <ul>
                            <li><input type='file' name='file1' accept='image/*' onchange='previewImage(event)' required></li>
                            <li><input type="submit" value="검사"></li>
                        </ul>
                    </div>
                    <div class='animal'>{msg}</div>
                </div>
            </div>
        </form>
    """)
    print("""
         <script>
            function previewImage(event) {
                const file = event.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        // Set the image preview here if needed
                    }
                    reader.readAsDataURL(file);
                }
            }
        </script>
        </body>
        </html>
    """)

# Handle form input
form = cgi.FieldStorage()
msg = ""

if 'file1' not in form:
    msg = "<p>파일을 선택하지 않았습니다.</p>"
else:
    file_field = form['file1']
    if file_field.filename:
        try:
            image = Image.open(file_field.file)
            preprocessed_image = joo_preprocessing_img(image)  # Process the image for the model
            result = joo_predict_value(preprocessed_image, model_file)  # Predict using the model
            
            # Assuming your model outputs a binary result (1 for lion, 0 for not lion)
            if result == 1:
                msg = "<p>이 동물은 사자입니다.</p>"
            else:
                msg = "<p>이 동물은 사자가 아닙니다.</p>"
        except Exception as e:
            msg = f"<p>이미지 처리 중 오류가 발생했습니다: {e}</p>"
    else:
        msg = '<p>올바른 파일을 업로드하세요.<p>'

# Show the HTML response
showHTML(msg)
