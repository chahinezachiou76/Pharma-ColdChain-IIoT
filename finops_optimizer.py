import boto3

REGION = 'eu-west-1'
BUCKET = 'vaccine-iot-bucket'

s3 = boto3.client('s3', region_name=REGION)

response = s3.list_objects_v2(Bucket=BUCKET)

total_size = 0

if 'Contents' in response:
    for obj in response['Contents']:
        total_size += obj['Size']

size_mb = total_size / (1024 * 1024)

print(f"S3 Usage: {size_mb:.2f} MB")

if size_mb > 100:
    print("[FINOPS ALERT] High storage usage detected!")
    print("Recommendation: Archive or delete old IoT data.")
else:
    print("Infrastructure is cost-optimized.")