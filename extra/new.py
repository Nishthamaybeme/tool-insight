# from google import genai

# def text_to_description(text):
#     client = genai.Client(api_key="AIzaSyCKObDUccEduVBBBm1z49Fcf7dRvbMWlOU")
#     response = client.models.generate_content(
#         model="gemini-2.0-flash-exp",
#         contents=[f"Give me details about: {text}"]
#     )
#     return response.text

# description_query = "Describe a hinge"
# description_result = text_to_description(description_query)
# print("Gemini API Output:", description_result)
import google.generativeai as genai
import PIL.Image

# Configure API Key
genai.configure(api_key="AIzaSyCKObDUccEduVBBBm1z49Fcf7dRvbMWlOU")  # Replace with your actual API key

# Load image
image_path = "61HR6kgbCLL.jpg"  # Update with correct path
image = PIL.Image.open(image_path)

# Initialize the latest Gemini Vision model
model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Use updated model

prompt = """
Identify the object in this image and provide a detailed description.
Include:
1. Object name and category
2. Its primary function and how it is used
3. Variants or types of this object
4. Design and material details
5. Applications in different fields
6. Any historical or cultural significance
7. Advantages and disadvantages

Make the response **informative and well-structured**.
"""

# Generate response with image
response = model.generate_content([prompt, image])


# Print response
print(response.text)
