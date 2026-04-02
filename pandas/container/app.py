import boto3
import pandas as pd
import matplotlib.pyplot as plt
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'ctorres-general'
    key = 'cities.csv'

    # Download CSV from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    cities = pd.read_csv(obj['Body'])

    # Create pie chart
    cities_2019 = cities[cities['Year'] == 2019]
    fig, ax = plt.subplots(figsize=(6, 6))
    cities_2019.set_index("City")["Population"].plot(
        kind="pie", autopct='%1.1f%%', ax=ax, title="2019 Population Share by City"
    )
    plt.ylabel("")

    # Save image to memory
    buffer = io.BytesIO()
    plt.savefig(buffer, format='jpeg')
    buffer.seek(0)

    # Upload image to S3
    output_key = '2019_population_pie.jpeg'
    s3.put_object(Bucket=bucket, Key=output_key, Body=buffer, ContentType='image/jpeg')

    return {
        'statusCode': 200,
        'body': f'Image saved to s3://{bucket}/{output_key}'
    }
