import google.generativeai as genai
import PIL.Image
import io
import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import os


# Configure API Key
genai.configure(api_key="")

app = Flask(__name__, template_folder='.')

def generate_detailed_description(image_path=None, object_name=None, description=None):
    model = genai.GenerativeModel("gemini-1.5-flash")
    contents = []

    # Check if at least one input is provided
    if not image_path and not object_name and not description:
        return "Error: Please provide an image, object name, or description."

    # Handle image input (Object Identification)
    identified_object = None
    if image_path:
        try:
            image = PIL.Image.open(image_path)
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_bytes = img_byte_arr.getvalue()

            # Identify object in image
            identify_prompt = "Identify the object in this image. Provide only its name."
            response = model.generate_content([{"text": identify_prompt}, {"data": img_bytes, "mime_type": "image/jpeg"}])
            identified_object = response.text.strip() if response else None

            print(f"✅ Image Loaded: Identified as {identified_object}")
        except Exception as e:
            return f"❌ Error loading image: {str(e)}"

    # Check for conflicts
    conflict = False
    if object_name and identified_object and object_name.lower() != identified_object.lower():
        conflict = True

    # Prepare detailed description prompt
    if conflict:
        prompt = f"""
        You provided a text input as '{object_name}' but the image contains a '{identified_object}'.
        Here’s information on both:

        1️⃣ **{object_name}:** Describe in detail, including:
        - Category, Function, Variants, Design, Applications, History, Pros & Cons

        2️⃣ **{identified_object}:** Describe in detail, including:
        - Category, Function, Variants, Design, Applications, History, Pros & Cons
        """
    else:
        final_object = identified_object if identified_object else object_name
        prompt = f"""
        Provide a detailed description of a {final_object}.
        Include:
        1. Object name and category
        2. Its primary function and how it is used
        3. Variants or types of this object
        4. Design and material details
        5. Applications in different fields
        6. Any historical or cultural significance
        7. Advantages and disadvantages

        Additional context: {description if description else 'No extra details provided.'}
        """

    # Generate final response
    try:
        response = model.generate_content([{"text": prompt}])
        return response.text if response else "No response received."
    except Exception as e:
        return f"❌ API Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

# ✅ Serve CSS and other static files from the same directory
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), filename)

@app.route('/analyze', methods=['POST'])
def analyze():
    object_name = request.form.get("object_name")
    image = request.files.get("image")

    # Process and return response
    description = generate_detailed_description(image_path=image, object_name=object_name)
    return jsonify({"description": description})

if __name__ == "__main__":
    app.run(debug=True)
