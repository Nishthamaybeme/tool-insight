from transformers import pipeline

# Load pre-trained Named Entity Recognition (NER) model
nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Define the input prompt describing a tool
prompt = "This vernier caliper tool is used to measure the diameter of pipes and tubes."

# Process the text using the NER model
entities = nlp(prompt)

# Print out all recognized entities for debugging
print("All recognized entities:")
for entity in entities:
    print(f"Entity: {entity['word']}, Label: {entity['entity']}, Score: {entity['score']}")

# Find a recognized tool name
recognized_tool = None
for entity in entities:
    # You can modify the entity labels based on what you expect
    if entity['entity'] in ['I-ORG', 'I-MISC']:  # Checking for organizations or miscellaneous entities
        recognized_tool = entity['word']
        break

if recognized_tool:
    print(f"Recognized Tool: {recognized_tool}")
else:
    print("No tool recognized in the prompt.")
