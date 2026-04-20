# Docker Settings

## Mirror

```bash
sudo vim /etc/docker/daemon.json

{
  "registry-mirrors": [
    "https://docker.m.daocloud.io",
    "https://docker.1panel.live/",
    "https://1ms.run/",
    "https://docker.xuanyuan.me/",
    "https://dev.xuanyuan.dev/",
    "https://dytt.online/",
    "https://docker.zyjs8.com/",
    "https://lispy.org/",
    "https://docker-0.unsee.tech/",
    "https://gh.123822.xyz",
    "https://docker.m.daocloud.io",
    "https://dockerproxy.net",
    "https://demo.52013120.xyz",
    "https://proxy.vvvv.ee",
    "https://xdark.top/",
    "https://registry.cyou/",
    "https://mirror.ccs.tencentyun.com"
  ]
}
# image add docker.m.daocloud.io in docker-compose.yml
```

```bash
# docker compose down -v
# docker logs namenode --tail 100
# docker logs datanode --tail 100
docker compose up -d
docker compose ps
```

## Start

```bash
mkdir -p ./data/namenode ./data/datanode ./data/warehouse
ls data/
datanode  namenode  warehouse
docker compose up -d
[+] up 5/5
 ✔ Network docker_hive-net Created                                                                                                                                                                                                                                              0.0s
 ✔ Container namenode      Started                                                                                                                                                                                                                                              0.4s
 ✔ Container datanode      Started                                                                                                                                                                                                                                              0.5s
 ✔ Container metastore     Started                                                                                                                                                                                                                                              0.5s
 ✔ Container hiveserver2   Started                                                                                                                                                                                                                                              0.6s
docker compose ps
NAME          IMAGE                                             COMMAND                  SERVICE       CREATED          STATUS                             PORTS
datanode      bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8   "/entrypoint.sh /run…"   datanode      14 seconds ago   Up 13 seconds (health: starting)   9864/tcp
hiveserver2   docker.m.daocloud.io/apache/hive:4.1.0            "sh -c /entrypoint.sh"   hiveserver2   14 seconds ago   Up 13 seconds                      0.0.0.0:10000->10000/tcp, [::]:10000->10000/tcp, 9083/tcp, 0.0.0.0:10002->10002/tcp, [::]:10002->10002/tcp
metastore     docker.m.daocloud.io/apache/hive:4.1.0            "sh -c /entrypoint.sh"   metastore     14 seconds ago   Up 13 seconds                      10000/tcp, 0.0.0.0:9083->9083/tcp, [::]:9083->9083/tcp, 10002/tcp
namenode      bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8   "/entrypoint.sh /run…"   namenode      14 seconds ago   Up 13 seconds (health: starting)   0.0.0.0:9870->9870/tcp, [::]:9870->9870/tcp, 0.0.0.0:9001->9000/tcp, [::]:9001->9000/tcp

# wait namenode and datanode are ok
docker compose ps
NAME          IMAGE                                             COMMAND                  SERVICE       CREATED              STATUS                        PORTS
datanode      bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8   "/entrypoint.sh /run…"   datanode      About a minute ago   Up About a minute (healthy)   9864/tcp
hiveserver2   docker.m.daocloud.io/apache/hive:4.1.0            "sh -c /entrypoint.sh"   hiveserver2   About a minute ago   Up About a minute             0.0.0.0:10000->10000/tcp, [::]:10000->10000/tcp, 9083/tcp, 0.0.0.0:10002->10002/tcp, [::]:10002->10002/tcp
metastore     docker.m.daocloud.io/apache/hive:4.1.0            "sh -c /entrypoint.sh"   metastore     About a minute ago   Up About a minute             10000/tcp, 0.0.0.0:9083->9083/tcp, [::]:9083->9083/tcp, 10002/tcp
namenode      bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8   "/entrypoint.sh /run…"   namenode      About a minute ago   Up About a minute (healthy)   0.0.0.0:9870->9870/tcp, [::]:9870->9870/tcp, 0.0.0.0:9001->9000/tcp, [::]:9001->9000/tcp
```

## Hive Sql

```bash
docker exec -it hiveserver2 bash
bash-5.1$ beeline -u jdbc:hive2://localhost:10000
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/hive/lib/log4j-slf4j-impl-2.24.3.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/hive/lib/log4j-slf4j-impl-2.24.3.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]
2026-04-20T07:48:01.236204908Z main WARN The use of package scanning to locate Log4j plugins is deprecated.
Please remove the `packages` attribute from your configuration file.
See https://logging.apache.org/log4j/2.x/faq.html#package-scanning for details.
2026-04-20T07:48:01.302440581Z main INFO Starting configuration org.apache.logging.log4j.core.config.properties.PropertiesConfiguration@436c81a3...
2026-04-20T07:48:01.302564261Z main INFO Start watching for changes to jar:file:/opt/hive/lib/hive-beeline-4.1.0.jar!/beeline-log4j2.properties every 0 seconds
2026-04-20T07:48:01.302667493Z main INFO Configuration org.apache.logging.log4j.core.config.properties.PropertiesConfiguration@436c81a3 started.
2026-04-20T07:48:01.303756394Z main INFO Stopping configuration org.apache.logging.log4j.core.config.DefaultConfiguration@2df9b86...
2026-04-20T07:48:01.303950696Z main INFO Configuration org.apache.logging.log4j.core.config.DefaultConfiguration@2df9b86 stopped.
Connecting to jdbc:hive2://localhost:10000
Connected to: Apache Hive (version 4.1.0)
Driver: Hive JDBC (version 4.1.0)
Transaction isolation: TRANSACTION_REPEATABLE_READ
Beeline version 4.1.0 by Apache Hive
0: jdbc:hive2://localhost:10000> show databases;
INFO  : Compiling command(queryId=hive_20260420074808_86e66971-04b5-4ccd-aa39-f8df93017a4b): show databases
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Created Hive schema: Schema(fieldSchemas:[FieldSchema(name:database_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20260420074808_86e66971-04b5-4ccd-aa39-f8df93017a4b); Time taken: 0.501 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20260420074808_86e66971-04b5-4ccd-aa39-f8df93017a4b): show databases
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20260420074808_86e66971-04b5-4ccd-aa39-f8df93017a4b); Time taken: 0.045 seconds
+----------------+
| database_name  |
+----------------+
| default        |
+----------------+
1 row selected (0.754 seconds)
0: jdbc:hive2://localhost:10000>


0: jdbc:hive2://localhost:10000> show tables;
INFO  : Compiling command(queryId=hive_20260420083454_02511791-80b0-462b-9a4b-8bffb931e913): show tables
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Created Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20260420083454_02511791-80b0-462b-9a4b-8bffb931e913); Time taken: 0.006 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20260420083454_02511791-80b0-462b-9a4b-8bffb931e913): show tables
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20260420083454_02511791-80b0-462b-9a4b-8bffb931e913); Time taken: 0.051 seconds
+----------------+
|    tab_name    |
+----------------+
| user_behavior  |
+----------------+
1 row selected (0.074 seconds)
0: jdbc:hive2://localhost:10000>
```

## Technical Stack

> NameNode + DataNode + Hive Metastore + HiveServer2 + Beeline JDBC + Hive SQL

```bash
# NameNode UI
http://localhost:9870
```

| 主题 | 处理方式 | 技术栈  |  数据集下载 |
| ------------ | ------------ | ------------ | ------------ |
| [1 亿条淘宝用户行为数据分析](https://github.com/TurboWay/bigdata_analyse/blob/main/UserBehaviorFromTaobao_Batch/用户行为数据分析.md)       |  离线处理  | 清洗 hive  + 分析 hive + 可视化 echarts | [阿里云](https://tianchi.aliyun.com/dataset/dataDetail?dataId=649&userId=1) |


# Hive SQL & Data Pipeline

## 1. 


## 2. Copy Data to Hive Volume
```bash
docker cp /home/yuki/Code/BigData/bigdata_analyse/UserBehavior.csv hiveserver2:/tmp/UserBehavior.csv
```

## 3. In Volume run beeline
```bash
# in running volume - hiveserver2
# start hive userport and run beeline
docker exec -it hiveserver2 beeline -u jdbc:hive2://localhost:10000
```

## 4. Create Table and Load Table
```bash
# create table
drop table if exists user_behavior;
create table user_behavior (
user_id string,
item_id string,
category_id string,
behavior_type string,
timestamp int,
datetime string)
row format delimited
fields terminated by ','
lines terminated by '\n';

# load data
LOAD DATA LOCAL INPATH '/tmp/UserBehavior.csv' OVERWRITE INTO TABLE user_behavior;
```

## 5. Quary Table 
```bash
~/Code/BigData/bigdata_analyse/docker main* ⇡
❯ docker exec hiveserver2 beeline -u jdbc:hive2://localhost:10000 -e "select count(*) from user_behavior;"
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/hive/lib/log4j-slf4j-impl-2.24.3.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/opt/hive/lib/log4j-slf4j-impl-2.24.3.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/opt/hadoop/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]
2026-04-20T08:17:47.851630187Z main WARN The use of package scanning to locate Log4j plugins is deprecated.
Please remove the `packages` attribute from your configuration file.
See https://logging.apache.org/log4j/2.x/faq.html#package-scanning for details.
2026-04-20T08:17:47.904798657Z main INFO Starting configuration org.apache.logging.log4j.core.config.properties.PropertiesConfiguration@436c81a3...
2026-04-20T08:17:47.904916128Z main INFO Start watching for changes to jar:file:/opt/hive/lib/hive-beeline-4.1.0.jar!/beeline-log4j2.properties every 0 seconds
2026-04-20T08:17:47.905016482Z main INFO Configuration org.apache.logging.log4j.core.config.properties.PropertiesConfiguration@436c81a3 started.
2026-04-20T08:17:47.906330120Z main INFO Stopping configuration org.apache.logging.log4j.core.config.DefaultConfiguration@2df9b86...
2026-04-20T08:17:47.906518420Z main INFO Configuration org.apache.logging.log4j.core.config.DefaultConfiguration@2df9b86 stopped.
Connecting to jdbc:hive2://localhost:10000
Connected to: Apache Hive (version 4.1.0)
Driver: Hive JDBC (version 4.1.0)
Transaction isolation: TRANSACTION_REPEATABLE_READ
INFO  : Compiling command(queryId=hive_20260420081748_4086db62-8d71-41a7-84aa-bd2918d6259d): select count(*) from user_behavior
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Created Hive schema: Schema(fieldSchemas:[FieldSchema(name:_c0, type:bigint, comment:null)], properties:null)
INFO  : Completed compiling command(queryId=hive_20260420081748_4086db62-8d71-41a7-84aa-bd2918d6259d); Time taken: 0.039 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20260420081748_4086db62-8d71-41a7-84aa-bd2918d6259d): select count(*) from user_behavior
INFO  : Query ID = hive_20260420081748_4086db62-8d71-41a7-84aa-bd2918d6259d
INFO  : Total jobs = 1
INFO  : Launching Job 1 out of 1
INFO  : Starting task [Stage-1:MAPRED] in serial mode
INFO  : Subscribed to counters: [] for queryId: hive_20260420081748_4086db62-8d71-41a7-84aa-bd2918d6259d
INFO  : Tez session hasn't been created yet. Opening session
INFO  : Dag name: select count(*) from user_behavior (Stage-1)
INFO  : HS2 Host: [aa5cffb6d749], Query ID: [hive_20260420081748_4086db62-8d71-41a7-84aa-bd2918d6259d], Dag ID: [dag_1776673068370_0001_1], DAG App ID: [application_1776673068370_0001], DAG App address: [aa5cffb6d749]
INFO  : Status: Running (Executing on YARN cluster with App id application_1776673068370_0001)

----------------------------------------------------------------------------------------------
        VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED
----------------------------------------------------------------------------------------------
Map 1 .......... container     SUCCEEDED      7          7        0        0       0       0
Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0
----------------------------------------------------------------------------------------------
VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 38.74 s
----------------------------------------------------------------------------------------------
INFO  : Status: DAG finished successfully in 38.73 seconds
INFO  : DAG ID: dag_1776673068370_0001_1
INFO  :
INFO  : Query Execution Summary
INFO  : ----------------------------------------------------------------------------------------------
INFO  : OPERATION                            DURATION
INFO  : ----------------------------------------------------------------------------------------------
INFO  : Compile Query                           0.04s
INFO  : Prepare Plan                            0.14s
INFO  : Get Query Coordinator (AM)              0.00s
INFO  : Submit Plan                             0.01s
INFO  : Start DAG                               0.02s
INFO  : Run DAG                                38.73s
INFO  : ----------------------------------------------------------------------------------------------
INFO  :
INFO  : Task Execution Summary
INFO  : ----------------------------------------------------------------------------------------------
INFO  :   VERTICES      DURATION(ms)   CPU_TIME(ms)    GC_TIME(ms)   INPUT_RECORDS   OUTPUT_RECORDS
INFO  : ----------------------------------------------------------------------------------------------
INFO  :      Map 1          38153.00              0              0      98,911,960                7
INFO  :  Reducer 2              0.00              0              0               7                0
INFO  : ----------------------------------------------------------------------------------------------
INFO  : FileSystem Counters Summary
INFO  :
INFO  : Scheme: FILE
INFO  : ----------------------------------------------------------------------------------------------
INFO  :   VERTICES      BYTES_READ      READ_OPS     LARGE_READ_OPS      BYTES_WRITTEN     WRITE_OPS
INFO  : ----------------------------------------------------------------------------------------------
INFO  :      Map 1              0B             0                  0                 0B             0
INFO  :  Reducer 2              0B             0                  0                 0B             0
INFO  : ----------------------------------------------------------------------------------------------
INFO  :
INFO  : org.apache.tez.common.counters.DAGCounter:
INFO  :    NUM_SUCCEEDED_TASKS: 8
INFO  :    TOTAL_LAUNCHED_TASKS: 8
INFO  :    DURATION_SUCCEEDED_TASKS_MILLIS: 37552
INFO  :    OTHER_LOCAL_TASKS: 7
INFO  :    AM_CPU_MILLISECONDS: 39960
INFO  :    WALL_CLOCK_MILLIS: 37552
INFO  :    AM_GC_TIME_MILLIS: 86
INFO  :    INITIAL_HELD_CONTAINERS: 0
INFO  :    TOTAL_CONTAINERS_USED: 8
INFO  :    TOTAL_CONTAINER_LAUNCH_COUNT: 8
INFO  :    TOTAL_CONTAINER_RELEASE_COUNT: 8
INFO  :    NODE_USED_COUNT: 1
INFO  :    NODE_TOTAL_COUNT: 1
INFO  : org.apache.tez.common.counters.TaskCounter:
INFO  :    SPILLED_RECORDS: 0
INFO  :    NUM_SHUFFLED_INPUTS: 0
INFO  :    NUM_FAILED_SHUFFLE_INPUTS: 0
INFO  :    INPUT_RECORDS_PROCESSED: 98914491
INFO  :    INPUT_SPLIT_LENGTH_BYTES: 5605314212
INFO  :    OUTPUT_RECORDS: 7
INFO  :    APPROXIMATE_INPUT_RECORDS: 7
INFO  :    OUTPUT_LARGE_RECORDS: 0
INFO  :    OUTPUT_BYTES: 42
INFO  :    OUTPUT_BYTES_WITH_OVERHEAD: 98
INFO  :    OUTPUT_BYTES_PHYSICAL: 294
INFO  :    ADDITIONAL_SPILLS_BYTES_WRITTEN: 0
INFO  :    ADDITIONAL_SPILLS_BYTES_READ: 0
INFO  :    ADDITIONAL_SPILL_COUNT: 0
INFO  :    SHUFFLE_BYTES: 0
INFO  :    SHUFFLE_BYTES_DECOMPRESSED: 0
INFO  :    SHUFFLE_BYTES_TO_MEM: 0
INFO  :    SHUFFLE_BYTES_TO_DISK: 0
INFO  :    SHUFFLE_BYTES_DISK_DIRECT: 0
INFO  :    SHUFFLE_PHASE_TIME: 3
INFO  :    FIRST_EVENT_RECEIVED: 2
INFO  :    LAST_EVENT_RECEIVED: 3
INFO  :    DATA_BYTES_VIA_EVENT: 126
INFO  : HIVE:
INFO  :    CREATED_FILES: 1
INFO  :    DESERIALIZE_ERRORS: 0
INFO  :    RECORDS_IN_Map_1: 98911960
INFO  :    RECORDS_OUT_0: 1
INFO  :    RECORDS_OUT_INTERMEDIATE_Map_1: 7
INFO  :    RECORDS_OUT_INTERMEDIATE_Reducer_2: 0
INFO  :    RECORDS_OUT_OPERATOR_FS_11: 1
INFO  :    RECORDS_OUT_OPERATOR_GBY_10: 1
INFO  :    RECORDS_OUT_OPERATOR_GBY_8: 7
INFO  :    RECORDS_OUT_OPERATOR_MAP_0: 0
INFO  :    RECORDS_OUT_OPERATOR_RS_9: 7
INFO  :    RECORDS_OUT_OPERATOR_SEL_7: 98914484
INFO  :    RECORDS_OUT_OPERATOR_TS_0: 98914484
INFO  : org.apache.hadoop.hive.ql.exec.tez.HiveInputCounters:
INFO  :    GROUPED_INPUT_SPLITS_Map_1: 7
INFO  :    INPUT_DIRECTORIES_Map_1: 1
INFO  :    INPUT_FILES_Map_1: 7
INFO  :    RAW_INPUT_SPLITS_Map_1: 109
INFO  : Completed executing command(queryId=hive_20260420081748_4086db62-8d71-41a7-84aa-bd2918d6259d); Time taken: 38.905 seconds
+-----------+
|    _c0    |
+-----------+
| 98914484  |
+-----------+
1 row selected (38.972 seconds)
Beeline version 4.1.0 by Apache Hive
Closing: 0: jdbc:hive2://localhost:10000
```

## 6. Data Clean

### 6.1 Data Deduplication
```bash
insert overwrite table user_behavior
select user_id, item_id, category_id, behavior_type, `timestamp`, datetime
from user_behavior
group by user_id, item_id, category_id, behavior_type, `timestamp`, datetime;
```

### 6.2 Timestamp swap
```bash
insert overwrite table user_behavior
select user_id, item_id, category_id, behavior_type, `timestamp`, from_unixtime(`timestamp`, 'yyyy-MM-dd HH:mm:ss')
from user_behavior;
```

### 6.3 Remove Abnormal Time Data
```bash
insert overwrite table user_behavior
select user_id, item_id, category_id, behavior_type, `timestamp`, datetime
from user_behavior
where cast(datetime as date) between '2017-11-25' and '2017-12-03';
```
