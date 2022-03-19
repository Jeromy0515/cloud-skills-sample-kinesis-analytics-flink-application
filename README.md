# 2022 클라우드 컴퓨팅 기능경기대회 제 2과제 Kinesis Data Analytics (Flink) 예제 코드

## Document
- <a href="https://docs.aws.amazon.com/ko_kr/kinesisanalytics/latest/java/examples-s3.html">Amazon Kinesis Data Analytics Docs</a>

## Pre-requisites
- You have to create Amazon Kinesis Data Stream name as `ExampleInputStream` in `us-east-1` region
- You have to create S3 Bucket name as `ka-app-<username>` in `us-east-1` region 

## Flink Application Source Code
#### From
```
git clone https://github.com/aws-samples/amazon-kinesis-data-analytics-java-examples
```

## Modify Source Code
#### Region
```
private static final String region = "us-east-1";
```
#### S3 Sink Path
```
private static final String s3SinkPath = "s3a://ka-app-<username>/data";
```

## Compile the Application Source Code
```
mvn package -Dflink.version=1.13.2
```

## Upload JAF File to S3 Bucket
1. Create S3 Bucket with any name
2. Upload JAR File to S3 Bucket

## How to Run Kinesis Data Analytics by Using AWS Console
1. Login to AWS Console
2. Create Kinesis Data Analytics Application as follows
   
   2-1. Select Apache Flink Runtime version = `1.13`
3. Click on Configure

   3-1. S3 Bucket = Choose the bucket you uploaded jar file above
   
   3-2. Path to Amazon S3 object = `aws-kinesis-analytics-java-apps-1.0.jar`
   
   3-3. Monitoring log level = `Info`
   
   3-4. Monitoring metrics level with CloudWatch = `Application`

   3-5. Click Save Change 

   3-6. Attach Role in `kinesis-analytics-YourApplicationName-us-east-1`
      1. `AmazonS3FullAccess`
      2. `AmazonKinesisFullAccess`
      3. `CloudWatchFullAccess`
      4. `CloudWatchLogsFullAccess`