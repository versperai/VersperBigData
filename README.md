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
