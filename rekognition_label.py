import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    # Get bucket and image key from event instead of input()
    bucket = event.get("bucket", "rekognition-labels-sahana")  # Default bucket
    photo = event.get("key", "default-image.jpg")  # Default image name

    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10
    )

    labels = {label['Name']: f"{label['Confidence']:.2f}%" for label in response['Labels']}
    
    return {
        "status": "Success",
        "processed_image": photo,
        "labels": labels
    }