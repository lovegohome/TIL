# Big Data 3V

![image-20210810213337102](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810213337102.png) 



## 3V  = Volume + Velocity + Variety 

| NO   | Data Volume                                                  | Data Velocity                                                | Data Variety                                                 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | <img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810222039333.png" alt="image-20210810222039333"  /> | ![image-20210810222057879](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810222057879.png) | ![image-20210810222110360](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810222110360.png) |
| 2    | Lake                                                         | Waterfall<br />엄청 빠르고 큰 데이터가 폭포수처럼 내려오는 것 | Recreation <br />휴양지 다양한 사람들                        |



## Big Data 3V - Issue

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810213654751.png" alt="image-20210810213654751" style="zoom: 33%;" /> 

- 전송
  빅데이터 생성 ->  한 군데로 모으기 or 어디로 보낼 때
  (너무 크고 빠른 양 : 어떤 기술을 써서 전송해서 어떻게 안전하게 받을 수 있을까?)
- 저장
  들어올 때, 받을 때, 빠르고 큰 데이터를 어떻게 저장해야 할까.
- 처리
  다양한 형태의 데이터: 오디오, 이미지, 텍스트 
  서로 다른 형태로 들어옴. 
  어떻게 가공해서 어떻게 처리할지 고민도 필요.
- 관리
  어딘가에 저장해서 계속해서 활용이 될텐데, 
  사실 데이터도 유통기한이라는 게 있다.
  최신의 데이터는 언제까지 보관을 해야 하고 
  그 이후의 데이터는 언제까지 보관할지
  : 우리의 실제 저장소의 사이즈를 보고 리텐션, 유효기간에 대한 전략 가져가기.



## Big Data 처리 기술 아키텍처

- Big Data 처리기술은 
  Hadoop을 중심으로 여러 생태계가 꾸며져 있음

  ![image-20210810214432966](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810214432966.png) 
   

- 지금은 hadoop보다 유명하게 알려진 제품들이 나오고 있다. 
  But. hadoop을 이해하는 것이 나머지 hadoop의 생태계를 이끌어 나가는 
  hadoop ecosystem 들을 이해하는데 굉장히 도움이 될 것 같다. 

- 몇 가지 ecosystem 

  - Apache Hbase: NoSQL 제품
  - Hive : Data Warehouse 제품
  - Flume : 빅데이터 수집 및 전송
  - Oozie
    이런 부분들을 work flow를 통해서 처리(수집-전송 받고- 저장-처리)하는
     work flow를 만드는 Oozie
  - Apache Spark
    hadoop이 batch처리 부분으로 느린 부분 있는데 
    이런 걸 memory 기반 하에 빠르게 처리할 수 있게 다양한 솔루션들을 통합
    - 일괄 처리(**batch** processing)란 컴퓨터 프로그램 흐름에 따라 순차적으로 자료를 처리하는 방식을 뜻한다.
  - Pig
    데이터에서 인사이트를 얻기 위해 중간에 처리하고 가공할 때 
    높은 비용이 발생하는데 이런 Big Data에 대한 ETL을 할 때 Pig을 하는 solution으로 많은 도움을 얻을 수 있는 pig 
    - ETL = 추출(Extract), 변환(Transform), 적재(Load) 
      (추출-변환-가공: 전처리 - 가공)
  - Apache Sqoop
    RDBMS에서 HDFS(hadoop 분산파일 시스템)으로 데이터를 옮기거나
    hadoop 분산파일 시스템에서 RDBMS로 데이터를 옮기고 싶을 때
    실제 그 전송 간에 중간에 Gate way 역할을 해주는 Apache Sqoop 이라는 solution이 있음. 
    - RDBMS(전통적으로 많이 쓰고 있는 관계형 Data Base)

![image-20210810220558586](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810220558586.png) 



- 여러 ecosystem들이 있고, 이를 바탕으로 Hadoop은 계속 발전 중. 





## Solutions

![image-20210810221115154](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810221115154.png)  

- 많이 쓰이는 Solutions
  - NoSQL의 솔루션

    1. Hbase - Hadoop의 분산파일시스템을 이용
    2. Cassandra
    3. MongoDB
    4. Neo4j - graph data base

  - Cache - 많은 스타트업에서 사용

    1. Redis
       cache인증 or 사용위해 Redis라는 in memory 제품을 많이 활용함

  - RPC

    - Thrift, Avro, Protocol Buffer(google)

  - Collect (수집)

    - Flume, Logstash, Fluentd
    - Chuckw(이건 윤재님이 말씀해주심)

  - Query

    - 예로 로우 데이터, 빅데이터를 
      빅데이터 저장시스템에 저장을 했을 때 
      거기서 insight를 얻어서 처리를 하려면 program을 만들어야 함
      program logic이 너무나 개발양도 많고 어려운 부분이 있음 

      그런 부분들을 Enterprise에서 많이 사용하는 SQL을 통해서 insight 얻으면 편리, 그런 solution들이 실제로 꽤 많이 나와 있음

    - Hive, Pig, Impala

      - Impala
        좀 더 빠르게 이런 부분을 다루는 MPP engine
        (multi Parallel Processing  engining in impala)
        (The *Impala* service is a distributed, massively *parallel processing* (MPP) database *engine*.)

    - 이런 engien들을 이용해서 query를 통해서 로우데이터에서 insight를 얻을 수 있다.

  - Streaming 

    - batch 처리 못지 않게 실시간 처리가 굉장히 중요해진 시대 
      실시간으로 들어오는 데이터들을 바로바로 처리해서 알람을 준다던가 
      모니터 화면에 뿌려준다던가 관리자에게 insight를 준다던가 
      현실세계에서 중요해졌다.
    - 요즘에는 Spark streaming, Storm
    - S4: 전통적으로 컴플렉스 이벤트 프로세싱을 담당
    - Akka: 비동기처리나 동시성 처리에 강한 solution

  - Search

    - Elastic Search
      제조, 보안, 유통 등 실질 대시보드를 그리기 편하고 저장도 잘 되고 검색도 빠름
    - Apache Solr
      기존 Enterprise에서 open source로 검색엔진에 많이 활용했던 제품

  - File System

    - Hadoop, GlusterFS, Ceph, Swift
      Big data 저장 위해 많이 사용되고 있다. 

  - ETC

    - 머신러닝: 하둡 같은 경우에 Mahout
    - 분산 코디네이터, 중간에서 clusters 관리 등 하는 Zookeeper
    -  중간에 메시지 큐 역할을 해주는 Kafka
    - RDBMS - Hadoop 서로 간의 데이터를 전송해주는 Sqoop
    - 통계 활용할 때 R 언어
    - 위의 일련의 절차들로 수집해서 저장해서 자동적으로 처리 logic에 의해서 처리가 구현되도록 하고 싶을 때 Workflow 처리를 할 수 있는 Oozie  







![image-20210810230825905](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810230825905.png) 

- Hadoop, Hive
  - 클림스트림 분석 가능
  - 기존엔 비싼 고가의 서버를 이용해서 데이터웨어하우스 구축
    이제는 일반 범용서버 이용해서 하둡 구축 그 위에 하이브라는 솔루션에 쿼리를 이용해서 다양하게 모니터링, 알람, 대시보드 등 활용 가능 
  - 하둡 = batch 처리에 적합
    하이브도 Olab, 온라인에서 처리할 수 있게 뭔가 하는데 
    둘 다 안정적이지만 상대적으로 느린 제품들이다. 
    - batch 처리가 한 번에 거대한 양을 처리하기 때문

- 현업에선 MPP - 임팔라, 테즈원하이브 더 활용 
  처리 결과를 좀 더 빠르게 이끄려내려고 함
  - 그런 시도를 다시 sqoop이라는 solution을 통해서 RDB에 넣어서 
    OLTP 같은 온라인에서 실질적으로 빠르게 화면에 보여주고 결과를 받아가는 그런 부분을 좀 추가적으로 활용해 볼 수 있을 거 같다. 
- 현실세계에서는 Hive 뿐만 아니고 MPP 엔진, RDBMS를 같이 활용해서 사용





## Architecture

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810232529153.png" alt="image-20210810232529153" style="zoom: 50%;" /> 

- Lambda Architecture
  Data 처리 frame work architecture

- 실시간 분석을 지원하는 빅데이터 아키텍쳐
  대량의 데이터를 실시간으로 분석하기 어려우니 batch로 미리 만든 데이터와 실시간 데이터를 혼합해서 사용하는 방식이다. 출처: [[Minsub's Blog]](https://gyrfalcon.tistory.com/entry/람다-아키텍처-Lambda-Architecture )

  ![image-20210810233146988](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810233146988.png) 



​	![image-20210810233249108](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210810233249108.png) 

- 이렇게 architecture를 꾸미지 않아도 되지만 
  람다 아키텍처를 꾸민다고 하면 이렇다. 

  1. data 유입
     big data: 빠르고 다양하고 크게 들어오는 데이터
  2. 중간에 (하둡 에코시스템 중) 메시지 queue 역할 담당하는 
     아파치 카프카 솔루션 통해서 받아줌
  3. 아파치 스파크 통해서 batch 처리해서 
     - hadoop의 HDFS에 batch를 위해서 로우데이터를 저장할 수도 있고
     - 바로바로 들어온 데이터를 실시간으로 처리를 하고 싶어서 
       spark streaming이라는 솔루션을 이용해서 
     - 뭔가 처리 결과를 serving layer로 보낼 수도 있음 
  4. Batch Layer / Speed Layer
     새로운 데이터를 통해 들어온 것들이 HDFS에 저장 후 처리하여 
     알람, 화면에 뿌려주기 등등 가능 
     - 그 처리가 가능한 솔루션 많다. 
       mapreduce, pig 등 많은데 지금은 
       Spark(batch도 가능, Streamin도 가능, ML도 가능 = 통합솔루션)
     - Spark
  5. Serving Layer
     결과 보내는데, NoSQL 제품 중 하나인 cassandra, mongoDB 통해서
     - batch 성으로 보여줄 view
     - speed layer에서 실시간으로 바로 처리해서 보여줄 real-time view
     - 이런 걸 구현 가능 

  

