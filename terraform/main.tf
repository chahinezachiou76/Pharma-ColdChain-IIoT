provider "aws" {
  region                      = var.aws_region
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    iot      = "http://localhost:4566"
    s3       = "http://s3.localhost.localstack.cloud:4566"
    iam      = "http://localhost:4566"
    firehose = "http://localhost:4566"
    sts      = "http://localhost:4566"
  }
}

# 1. S3 Bucket for final storage
resource "aws_s3_bucket" "iot_bucket" {
  bucket = var.bucket_name
}

# 2. IAM Role for Kinesis Firehose
resource "aws_iam_role" "firehose_role" {
  name = "firehose_local_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "firehose.amazonaws.com" }
    }]
  })
}

## 3. Kinesis Firehose Delivery Stream
resource "aws_kinesis_firehose_delivery_stream" "vaccine_firehose" {
  name        = "vaccine-data-stream"
  destination = "extended_s3"

  extended_s3_configuration {
    role_arn   = aws_iam_role.firehose_role.arn
    bucket_arn = aws_s3_bucket.iot_bucket.arn
    
    processing_configuration {
      enabled = false
    }

    # FIX: Use 'buffering_size' and 'buffering_interval'
    buffering_size     = 5 
    buffering_interval = 60
  }
}

# 4. IAM Role for IoT Rule
resource "aws_iam_role" "iot_role" {
  name = "iot_to_firehose_local_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "iot.amazonaws.com" }
    }]
  })
}

# 5. IoT Topic Rule (Routes data to Firehose)
resource "aws_iot_topic_rule" "iot_to_firehose_rule" {
  name        = "iot_to_firehose"
  enabled     = true
  sql         = "SELECT * FROM 'vaccine/fridge/data'"
  sql_version = "2016-03-23"

  firehose {
    delivery_stream_name = aws_kinesis_firehose_delivery_stream.vaccine_firehose.name
    role_arn             = aws_iam_role.iot_role.arn
  }
}