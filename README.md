# 2022 클라우드 컴퓨팅 기능경기대회 제 2과제 Kinesis Data Analytics (Flink) 예제 코드

## Document
- <a href="https://docs.aws.amazon.com/ko_kr/kinesisanalytics/latest/java/examples-s3.html">Amazon Kinesis Data Analytics Docs</a>

## Pre-requisites
- You have to create Amazon Kinesis Data Stream name as `ExampleInputStream` in `us-east-1` region
- You have to create S3 Bucket name as `ka-app-pmj` in `us-east-1` region 

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
private static final String s3SinkPath = "s3a://ka-app-pmj/data";
```

## Compile the Application Source Code
```
mvn package -Dflink.version=1.13.2
```

## How to Run by Using AWS Console



