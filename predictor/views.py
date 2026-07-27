from django.shortcuts import render
# from .ai_model import model
from .ai_model import get_model
from PIL import Image
import numpy as np
from .models import Prediction
from predictor.gradcam import save_gradcam
import os
from predictor.groq_ai import generate_medical_report

def home(request):

    prediction = None
    confidence = None
    uploaded_image = None
    gradcam_url = None
    report = None

    if request.method == "POST":

        image = request.FILES["image"]

        img = Image.open(image)

        img = img.resize((224, 224))
        img = img.convert("RGB")

        img = np.array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        result = model.predict(img)
        model = get_model()

        probability = float(result[0][0])

        if probability > 0.5:
            prediction = "PNEUMONIA"
            confidence = probability * 100
        else:
            prediction = "NORMAL"
            confidence = (1 - probability) * 100

        prediction_obj = Prediction.objects.create(
            image=image,
            prediction=prediction,
            confidence=round(confidence, 2)
        )


# llm integration
        report = generate_medical_report(
        prediction,
        confidence)

        prediction_obj.ai_report = report
        prediction_obj.save()

# gradcam image in website

        gradcam_folder = os.path.join("media", "gradcam")
        os.makedirs(gradcam_folder, exist_ok=True)

        gradcam_filename = f"gradcam_{prediction_obj.id}.jpg"

        gradcam_path = os.path.join(
            gradcam_folder,
            gradcam_filename
        )

        save_gradcam(
            prediction_obj.image.path,
            img,
            model,
            "Conv_1",
        gradcam_path
        )   

        gradcam_url = "/media/gradcam/" + gradcam_filename
        

    return render(
    request,
    "predictor/home.html",
    {
        "prediction": prediction,
        "confidence": round(confidence, 2) if confidence is not None else None,
        # "uploaded_image": prediction_obj.image.url,
        # "gradcam_image": gradcam_url,
        "uploaded_image": prediction_obj.image.url if request.method == "POST" else None,
        "gradcam_image": gradcam_url if request.method == "POST" else None,
        "ai_report": report,
    }
)


def history(request):
    predictions = Prediction.objects.order_by("-created_at")

    return render(
        request,
        "predictor/history.html",
        {
            "predictions": predictions
        }
    )