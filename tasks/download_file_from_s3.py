def download_file_from_s3(
    s3_endpoint_url      : str,
    s3_access_key_id     : str,
    s3_secret_access_key : str,
    s3_region_name       : str,
    s3_bucket            : str,
    s3_filename          : str,
    local_filename       : str
):
    """
    Downloads a file from an S3-compatible object storage service.

    Parameters:
        - s3_endpoint_url      (str) : The endpoint URL of the S3 service.
        - s3_access_key_id     (str) : The access key ID for authentication.
        - s3_secret_access_key (str) : The secret access key for authentication.
        - s3_region_name       (str) : The region name of the S3 service.
        - s3_bucket            (str) : The name of the S3 bucket where the file is located.
        - s3_filename          (str) : The name of the file to be downloaded.
        - local_filename       (str) : The local name of the file to save the downloaded file as.

    Returns:
        - None.
    """

    from boto3 import client

    s3_client = client(
        service_name          = 's3',
        endpoint_url          = s3_endpoint_url,
        aws_access_key_id     = s3_access_key_id,
        aws_secret_access_key = s3_secret_access_key,
        region_name           = s3_region_name
    )

    s3_client.download_file(s3_bucket, s3_filename, local_filename)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    from os import getenv

    download_file_from_s3(
        s3_endpoint_url      = getenv('s3_endpoint_url'),
        s3_access_key_id     = getenv('s3_access_key_id'),
        s3_secret_access_key = getenv('s3_secret_access_key'),
        s3_region_name       = getenv('s3_region_name'),
        s3_bucket            = getenv('s3_bucket'),
        s3_filename          = getenv('s3_filename'),
        local_filename       = getenv('local_filename')
    )
