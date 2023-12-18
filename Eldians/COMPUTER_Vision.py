from transformers import DetrImageProcessor, DetrForObjectDetection
from transformers import GLPNImageProcessor, GLPNForDepthEstimation
import torch
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def reduce_image_quality(image_path):
    # Open the image
    image = Image.open(image_path)
    if image.size[0]<512 :
        return image_path
    else :
        # Calculate the new size by reducing dimensions
        new_size = (512,512)

        # Reduce the image size
        reduced_image = image.resize(new_size, Image.LANCZOS)

        # Save the reduced quality image
        reduced_image.save("reduced_quality_image.jpg", quality=50)  # Adjust quality as needed

    return "reduced_quality_image.jpg"  # Return the path to the reduced quality image



def object_detection(url):
    # Load the image
    image = Image.open(url)

    # Initialize the object detection model
    processor_detection = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    model_detection = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

    # Initialize the depth estimation model
    processor_depth = GLPNImageProcessor.from_pretrained("vinvino02/glpn-nyu")
    model_depth = GLPNForDepthEstimation.from_pretrained("vinvino02/glpn-nyu")

    # Get object detections
    inputs_detection = processor_detection(images=image, return_tensors="pt")
    outputs_detection = model_detection(**inputs_detection)

    # Convert detections to COCO format
    target_sizes = torch.tensor([image.size[::-1]])
    results_detection = processor_detection.post_process_object_detection(outputs_detection, target_sizes=target_sizes, threshold=0.5)[0]

    # Retrieve bounding box coordinates for each detected object
    boxes = results_detection["boxes"]

    # Retrieve predicted depth matrix
    inputs_depth = processor_depth(images=image, return_tensors="pt")
    outputs_depth = model_depth(**inputs_depth)
    predicted_depth = outputs_depth.predicted_depth.squeeze().detach().cpu().numpy()  # Detach the gradient here

    # Prepare the display of results on the image
    plt.imshow(image)
    ax = plt.gca()

    # List to store printed messages
    print_messages = []

    # Calculate average depth for each detected object and display bounding boxes
    for score, label, box in zip(results_detection["scores"], results_detection["labels"], boxes):
        box = [round(i, 2) for i in box.tolist()]
        label_str = model_detection.config.id2label[label.item()]

        # Bounding box coordinates
        x_min, y_min, x_max, y_max = int(box[0]), int(box[1]), int(box[2]), int(box[3])
        image_dim = image_size(url)
        x_object = (x_min + x_max-image_dim[0])
        y_object = (y_min + y_max-image_dim[1])

        # Extract depth values inside the bounding box
        depth_values = predicted_depth[y_min:y_max, x_min:x_max]

        # Calculate average depth
        z_object = np.min(depth_values)

        # Draw bounding boxes on the image
        rect = plt.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

        # Display label, confidence, and average depth near the box
        message = f"Detected object {label_str} with confidence {round(score.item(), 3)} at position {(x_object,y_object,z_object)} "
        print_messages.append(message)
        ax.text(x_object,y_object, f"{label_str} {round(score.item(), 3)} Depth: {round(z_object, 3)}", bbox=dict(facecolor='red', alpha=0.5))

    # Combine printed messages and predicted depth into a summary text
    summary_text = '\n'.join(print_messages) + f"\nPredicted Depth:\n{predicted_depth}"
    
    return summary_text, predicted_depth

def dimension_reducing(predicted_depth):
        # Déterminer les dimensions de la matrice initiale
        n, m = predicted_depth.shape

        # Redimensionner la matrice à une taille compatible avec 8 * 8
        new_n = 8
        new_m = 8

        # Calculer les indices de découpage pour réduire la matrice à 8 * 8
        step_n = n // new_n
        step_m = m // new_m

        # Calculer la matrice réduite en prenant la moyenne des blocs de valeurs
        reduced_matrix = np.zeros((new_n, new_m))

        for i in range(new_n):
            for j in range(new_m):
                block = predicted_depth[i * step_n:(i + 1) * step_n, j * step_m:(j + 1) * step_m]
                reduced_matrix[i, j] = np.mean(block)
        return reduced_matrix
def image_size(url):
    image = Image.open(url)
    return image.size
def propmpt(size,summary_text,predicted_depth, talk):
     return f'''image size :{size} Simplified matrices of the depth :{predicted_depth} The detected objects and their positions :{summary_text} Request :{talk}
     note that : 
-you should answer directly with the response without details the information given before are just to help you understand the environement
-Summarize your answer in 2 to 4 sentences at max
-if the question is not related to the given data try to answer him kindly and maintain a proper conversation especially that the user is a blind person but keep your answers short ( max 5 sentences) 
-use an easy vocabulary that can be understandable by an average person (a person that doesn't understand technical words)
-if you couldn't answer say it clearly
-give the answer directly(as you are an assistant to a blind person)'''