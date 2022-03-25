# Usage Flink Stream SQL
### [ ] ⬅ 생략 가능
## Create Table
```
CREATE TABLE <table-name> (
    column1 type,
    column2 type,
    .
    .
    .
)
[COMMENT table_comment]
[PARTITIONED BY (partition_column_name1, partition_column_name2, ...)]
WITH (
    key1 = val1,
    key2 = val2,
    .
    .
    .
)
```

## WATERMARK
테이블에 데이터가 들어온 시간을 표시함

문법 - `WATERMARK FOR rowtime_column_name AS watermark_strategy_expression`
```
CREATE TABLE Orders (
    `user` BIGINT,
    product STRING,
    order_time TIMESTAMP(3),
    WATERMARK FOR order_time AS order_time - INTERVAL '5' SECOND
) WITH ( . . . );
```
`- INTERVAL '5' SECOND` : 딜레이(5초)를 제거한 타임스탬프를 찍기 위함 

## PARTITIONED BY
Partition the created table by the specified columns. A directory is created for each partition if this table is used as a filesystem sink

## WITH OPTIONS
### [Formats](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/formats/overview/#formats)

### Amazon Kinesis Data Streams
[Amazon Kinesis Data Streams Connector Options](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/kinesis/#connector-options)

#### required options
- 'connector' = `'kinesis'`
- 'stream' = `'<stream-name>'`
- 'format' = `'...'`

```
CREATE TABLE <table-name> (
    .
    .
    .
)
WITH (
  'connector' = 'kinesis',
  'stream' = '<stream-name>',
  'aws.region' = '<region-name>',
  'scan.stream.initpos' = 'LATEST',
  'format' = '...'
)
```

### FileSystem(S3)
[File Formats](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/filesystem/#file-formats)

[Streaming Sink](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/filesystem/#streaming-sink)

#### required options
- 'connector' = `'filesystem''`
- 'path' = `'s3://path/to/whatever'`
- 'format' = `'...'`
```
CREATE TABLE <table-name> (
    .
    .
    .
)
WITH (
  'connector' = 'filesystem',           
  'path' = 's3://path/to/whatever',     
  'format' = '...',                    
)
```