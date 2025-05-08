# AWS Rekognition Label Detector using Lambda

This project detects labels from an image stored in an S3 bucket using AWS Rekognition and Lambda.

## How It Works

1. You upload an image to an S3 bucket.
2. AWS Lambda (using boto3) is triggered manually (or can be automated later).
3. Lambda reads the image and uses AWS Rekognition to detect labels.
4. The result includes the name of the object and the confidence score.

## Technologies

- AWS S3
- AWS Lambda
- AWS Rekognition
- Python (boto3)

## Sample Test Event

```json
{
  "bucket": "rekognition-labels-sahana",
  "photo": "squirrel.jpg"
}

📌Note: This project was done for learning and showcasing AWS Rekognition. It is not open for public API access to avoid cost.
