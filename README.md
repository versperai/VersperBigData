# Quick Start

## 1. Start Docker Compose

### 1.1 Mirror
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

### 1.2 Start Images

```bash
# NameNode + DataNode + Hive Metastore + HiveServer2 + Beeline JDBC + Hive SQL
# docker compose down -v
# docker logs namenode --tail 100
# docker logs datanode --tail 100
# docker compose up -d
# docker compose ps
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

## 2. Check Hive Server Beeline

```bash
docker exec -it hiveserver2 bash
show databases;
show tables;
```

<table align="center">
  <tr>
    <td><img src="assets/beeline_hive_server"></td>
  </tr>
</table>

# Hive SQL & Data Pipeline

## 1. Copy Data to Hive Volume
```bash
docker cp /home/yuki/Code/BigData/bigdata_analyse/UserBehavior.csv hiveserver2:/tmp/UserBehavior.csv
```

## 2. In Volume run beeline
```bash
# in running volume - hiveserver2
# start hive userport and run beeline
docker exec -it hiveserver2 beeline -u jdbc:hive2://localhost:10000
```

## 3. Create Table and Load Table
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

## 4. Quary Table

```bash
docker exec hiveserver2 beeline -u jdbc:hive2://localhost:10000 -e "select count(*) from user_behavior;"
```

<table align="center">
  <tr>
    <td><img src="assets/query_hive_1"></td>
  </tr>
</table>

<table align="center">
  <tr>
    <td><img src="assets/query_hive_2"></td>
  </tr>
</table>

## 5. Data Clean

### 5.1 Data Deduplication
```bash
insert overwrite table user_behavior
select user_id, item_id, category_id, behavior_type, `timestamp`, datetime
from user_behavior
group by user_id, item_id, category_id, behavior_type, `timestamp`, datetime;
```

### 5.2 Timestamp swap
```bash
insert overwrite table user_behavior
select user_id, item_id, category_id, behavior_type, `timestamp`, from_unixtime(`timestamp`, 'yyyy-MM-dd HH:mm:ss')
from user_behavior;
```

### 5.3 Remove Abnormal Time Data
```bash
insert overwrite table user_behavior
select user_id, item_id, category_id, behavior_type, `timestamp`, datetime
from user_behavior
where cast(datetime as date) between '2017-11-25' and '2017-12-03';
```
