import boto3
import datetime

def lambda_handler(event, context):
    bucket_name = "imagens-2025"
    retention_days = 30  # Quantidade de dias antes de excluir o arquivo
    
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in objects:
        for obj in objects['Contents']:
            last_modified = obj['LastModified']
            file_age = (datetime.datetime.now(datetime.timezone.utc) - last_modified).days
            
            if file_age > retention_days:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted {obj['Key']} (age: {file_age} days)")
    else:
        print("No objects to clean.")
