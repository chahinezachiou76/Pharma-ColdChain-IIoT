output "s3_bucket_name" {
  value = aws_s3_bucket.iot_bucket.bucket
}

output "firehose_name" {
  value = aws_kinesis_firehose_delivery_stream.vaccine_firehose.name
}

output "iot_rule_name" {
  value = aws_iot_topic_rule.iot_to_firehose_rule.name
}