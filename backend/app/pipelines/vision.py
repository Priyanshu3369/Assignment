import io, base64
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models
import pytesseract
import os

if os.name == "nt":  # Windows
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Pretrained ResNet18 for classification
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

# Load ImageNet labels
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
imagenet_classes = {i: line.strip() for i, line in enumerate(open("imagenet_classes.txt"))}

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def load_image_from_base64(b64: str) -> Image.Image:
    data = base64.b64decode(b64)
    return Image.open(io.BytesIO(data)).convert("RGB")

def classify_image(image: Image.Image) -> str:
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = outputs.max(1)
    return imagenet_classes[predicted.item()]

def extract_text(image: Image.Image) -> str:
    try:
        return pytesseract.image_to_string(image).strip()
    except Exception as e:
        return f"[OCR Error: {str(e)}]"
