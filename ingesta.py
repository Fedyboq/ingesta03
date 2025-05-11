import boto3

ficheroUpload = "facturas.json"
nombreBucket = "facturas-cloud-pp"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, "facturas/facturas.json")

print("Ingesta completada")
