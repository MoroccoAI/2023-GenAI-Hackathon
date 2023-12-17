from weasyprint import HTML
import base64

def generate_report(patient_info):
  # Define the width for the medical image (adjust as needed)
  medical_image_width = "180px"
  # Define the HTML template as a string
  html_template = f"""
  <!DOCTYPE html>
  <html>
  <head>
  <style>
  /* CSS styles go here */
  body {{
    font-family: Oswald, sans-serif;
    margin: 20px;
    color: #282c35; /* Set text color */
  }}
  .header {{
    display: flex;
    justify-content: center; /* Horizontally center the content */
    align-items: center; /* Vertically center the content */
    text-align: center;
    margin-bottom: 20px; /* Optional margin for spacing */
  }}
  .header-content {{
    display: flex;
    flex-direction: column; /* Stack the elements vertically */
    align-items: center;
    max-width: 100%;
    max-height: 40px; /* Adjust the height as needed */
    height: auto;
    margin-top: 20px; /* Add margin to separate the logo and text */
  }}
  /* Add your other CSS styles here */
  .medical-image {{
    width: {medical_image_width};
    height: auto;
    display: inline-block; /* This ensures the image is centered */
    margin-top: 20px;
    margin-bottom: 20px;
  }}
  .medical-image-container {{
    text-align: center; /* Center-align the image */
  }}
  .section-title {{
    background-color: #E5E4E2; /* Set the background color */
    padding: 5px 10px; /* Add padding to the section title */
    color: #282c35; /* Set text color */
    margin-bottom: 10px;
    margin: 0;
    text-align: center; /* Center-align the text */
  }}
  .main-title {{
    text-align: center; /* Center-align the text */
    margin-bottom: 20px; /* Add margin for spacing */
    color: #56575a;
  }}
  </style>
  </head>
  <body>
  <!-- Header Section -->
  <div class="header">
    <div class="header-content">
      <img src="data:image/jpeg;base64,{patient_info['header_image']}" alt="Header Image">
    </div>
  </div>
  <div class="main-title"><h1>Medical Report</h1></div>
  <!-- Personal Information Section -->
  <div class="section-container">
    <div class="section-title">Personal Information</div>
    <div class="personal-info">
    <ul class="info-list">
      <li><strong>Name:</strong> {patient_info['name']}</li>
      <li><strong>Age:</strong> {patient_info['age']}</li>
      <li><strong>Gender:</strong> {patient_info['gender']}</li>
      </ul>
      <!-- Add more personal information here -->
    </div>
  </div>

  <!-- Medical Image Section (always displayed) -->
  <div class="section-container">
    <div class="section-title">Medical Image</div>
    <div class="medical-info">
      <div class="medical-image-container">
        <img src="data:image/jpeg;base64,{patient_info['medical_image']}" alt="Medical Image" class="medical-image">
      </div>
    </div>
  </div>

  <!-- Medical Information Section -->
  <div class="section-container">
    <div class="section-title">Medical Information</div>
    <div class="medical-info">
      <ul class="info-list">
        <li><strong>Symptoms:</strong> {patient_info['symptoms']}</li>
        <li><strong>Medications:</strong> {patient_info['medications']}</li>
        <li><strong>Current Medical Conditions or Allergies:</strong> {patient_info['conditions_allergies']}</li>
        <li><strong>Changes in Lifestyle:</strong> {patient_info['lifestyle_changes']}</li>
      </ul>
    </div>
  </div>
  </body>
  </html>
  """

  # Create an HTML object from the modified HTML content
  html = HTML(string=html_template)

  # Generate the PDF
  html.write_pdf("output.pdf")
  return html_template


