

## Linux 기초 및 활용



1. Linux - 배포판 종류 多

![image-20210811213905657](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811213905657.png) 

- 서버용 운영체제로 많이 사용

- Linux 구조 

  - 커널: 리눅스의 핵심

  - 쉘: 사용자 인터페이스

  - 응용프로그램: 각종 도구 

    ![image-20210811214142264](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811214142264.png)  

- Linux 프롬프트

  - 사용자의 명령 입력을 기다리는 표시 
    - 쉘에 따라 다르게 나타남.
    - Bash 쉘의 경우 $로 표시

- Linux 홈 디렉터리

  - 사용자 계정이 만들어질 때마다 자기 자신의 Home directory(~)를 같이 만듦
    user1@localhose:~
    [사용자명]@[사용하는 호스트 서버명]:[여기가 사용자의 홈 디렉터리이다를 표시]

- Linux 디렉터리 구조 
  ![image-20210811214819079](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811214819079.png) 

  - bin: 기본적으로 명령어들이 포함

  - etc: 기타 설정 파일들이 들어감

  - usr: application을 설치할 때 주로 사용

    ​		기본 실행파일과 라이브러리 파일, 헤더 파일 등 많은 파일이 있음.
    ​		usr = Unix System Resource 

  - Home: 사용자 계정, 실제 사용하게 되는 Data

    ​		사용자 홈 디렉터리가 생성되는 디렉터리

  - tmp: 임시적으로 사용하거나 지웠다 썼다하는 temp 디렉터리

    -----

  - opt or usr: 
    Windows에서 프로그램 설치할 때 Program Files, Program Files(x86) 디렉터리 같다고 생각하면 됨, 패키지 설치할 때 이 안에 설치.

  - etc 디렉터리
    리눅스 설정을 위한 각종 파일을 가짐 

    ---------

    ![image-20210811215415201](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811215415201.png) 

     ![image-20210811215935060](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811215935060.png) 

  - 빅데이터 처리 기술을 리눅스 위에서 운영하다 보면 많은 로그가 발생 됨.

    - **var / log / app별 생성**
      에러 확인 위해 접근하는 디렉터리
    - proc, run
      프로세스, 실행 관련 정보는 proc, run 밑에 생성
    - mnt
      파일 시스템을 임시로 마운팅할 때 mnt 폴더 밑에 마운팅한 폴더가 보여짐
      - 마운트(mount): 
        컴퓨터 과학에서 저장 장치에 접근할 수 있는 경로를 디렉터리 구조에 편입시키는 작업을 말한다





![image-20210811220730404](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811220730404.png) 

- 실습: virtual box 솔루션
  virtual box 솔루션 - CentOS 설치 - 그 위에서 간단 명령어 - 간단 실습 진행 예정



![image-20210811220945724](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811220945724.png) 

- 구글 - Oracle VirtualBox - 다운로드 - Windows Architecture에 맞는 버전으로 설치

- CentOS 설치 위해 관련 이미지 받기 

  - 현장에서 서버를 운영할 때 GUI 형태로 된 이미지를 설치해서 사용하진 않음

  - CentOS의 최소 버전인 minimal version 받아서 설치
    ![image-20210811221349825](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811221349825.png) 

    

    - 가상머신 메모리 : 4G (테스트용)

    - 하드디스크 추가: VDI(버철박스에서 사용하는 이미지 형태로)

      ![image-20210811221618835](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811221618835.png)  ![image-20210811221435647](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811221435647.png) 

      

    - 동적할당 (실질적으로 내 하드디스크에 용량을 고정으로 잡지 않고, 내가 쓴 만큼 늘려가면서 하드디스크에 저장하겠다는 것, 20G 충분할 듯)
      ![image-20210811221509164](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811221509164.png) ![image-20210811221735605](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811221735605.png) 



​					![image-20210811221816162](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811221816162.png) 



​					![image-20210811221855856](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811221855856.png) 

​					OS 지정 안 된 가상 머신이기 때문에 CentOS를 설치 위해 이미지 넣는 작업![image-20210811222036043](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811222036043.png) 

![image-20210811222205389](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811222205389.png) 

그러면 이렇게까지 뜨는데, 본 과정에선 CentOS 설치하지는 않음.
대신 설치가 진행되어 있는 VirtualBox를 통해 간단히 실습 함. 





![image-20210811222443560](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811222443560.png) 

-  설정-네트워크-어댑터2: 호스트 전용 어댑터
  : 호스트 전용 어댑터를 통해서 Windows PC와 가상머신이 통신할 수 있는 IP를 부여



![image-20210811223122687](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811223122687.png) 

- 시작하게 되면 사용자 계정을 물어보는 화면 출력
- but 가상머신 내에서 작업하는 건 많이 불편할 수 있어서 
  Putty라는 응용 프로그램을 통해서 이 가상머신에 접속하자.
- Putty: 
  ssh를 통해서 머신에 접속할 수 있는 응용프로그램
  가상머신을 ssh application인 Putty 어플에 등록 후 접속



![image-20210811223731441](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811223731441.png) 

- 이후에 소스로 된 Hadoop app이나, Hive, Spark(Hadoop ecosystem) 등을 
  Linux 환경 위에 설치할 때 소스로 된 버전들을 설치하게 된다. 

  - 그 때 설치하게 될 경로는 기본적으로 opt 라는 경로로 설치하게 될 거다.

  - mkdir -p /opt/hadoop  ... 폴더 디렉토리 만들기

    - **-p 옵션**: 상위 디렉토리가 만들어져 있지 않으면 만들면서 
      하위 디렉터리도 같이 만들어달라는 명령어

    cd /opt/hadoop/ 
    pwd 
    ls - la

  - mkdir hadoop
    cd hadoop
    rmdir hadoop

-  clear 

- 파일의 실제 내용을 확인해보는 명령어 
  cat /etc/hosts

  - cat cctv_utf8.csv
    ctrl + c (내용 너무 많아서 멈춤)
  - cat: 내용 출력 



- 빅데이터 다룰 때, 
  로컬에 있는 실제 데이터들을 어떤 저장소로 옮기기 전에 
  데이터 내용을 간략히 확인, 탐색 과정 필요 

  - **cat**을 사용하면 500메가 or 1G 그 이상 되는 데이터들이 
    실질적으로 메모리에 다 올라가기 때문에 
    화면에 리스트 다 보기 힘들다.

  - 그래서 cat을 사용하기 보다, 
    위에서 몇 번째, 맨 끝에서 몇 번째처럼 지정해서 내용 확인 

  - cd /var/log
    로그들이 쌓이는 곳 

    ![image-20210811225546389](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811225546389.png) 

  - message: 로그 파일 
    ![image-20210811230117345](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811230117345.png) 

    ![image-20210811230203331](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811230203331.png) 

  - cat으로 보기 어려움 
    그래서 앞에서 5줄
    head -n 20 /폴더명/파일
    ![image-20210811230413395](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811230413395.png) 

  - 끝에서부터 보려면

    tail -n 5 /폴더명/파일

  - **실시간**으로 들어오는 로그를 바로바로 확인하고 싶을 때
    **tail -f** /폴더명/파일
    **-f 옵션**을 줘서 봄 / 빠져나올 땐 ctrl + c 

  - 파일을 생성, 복사, 이동, 삭제 명령어 참고

    touch file1, cp /폴더/파일, mv 파일 폴더, rm -r /data

  - 검색
    **find** / -name 이름
    root 밑에 어떤 이름을 가진 것들을 찾고 싶다. 

  - **grep** root /etc/passwd
    etc 밑에 passwd라는 파일 안에 
    계정에 대한 id, directory 등 설명 정보들이 들어가 있는데 
    root라는 걸 가진 것들만 출력해줘

  - **find, grep**은 많이 쓰는 명령어 
    옵션도 많이 찾아보고 활용도 해보자.





## 권한

읽기, 쓰기, 실행 

![image-20210811232113617](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811232113617.png) 

![image-20210811232131620](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811232131620.png) ![image-20210811232238641](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811232238641.png) 

- 접근 권한 설정 명령어 많이 활용함

  - 소유자를 명시하는 chown
    $ chown -R hadoop:hadoop /opt/hadoop 
    - 리눅스에 하둡을 설치한다는 가정 하에 opt 밑에 하둡을 설치하고
      그 밑에 아무나 접근할 수 있는 게 아니라 
      소유자는 hadoop이라는 계정이라고 설정 원하면 -R
      opt 밑에 hadoop 디렉터리는 hadoop의 소유로 들어감
  - 접근 권한을 변경할 수 있는 chmod
    $ chmod 0700 ~/.ssh/authorized_keys
    - ~/.ssh/ 위치의 authorized_keys 파일을 이 권한으로 바꿔달라는 명령어

  ![image-20210811232545954](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811232545954.png) 



vi, vim 

![image-20210811232939791](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811232939791.png) 



![image-20210811233030940](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811233030940.png) 



- vi 실습이 필요
- vi 편집기에 익숙해야 이후 Linux 환경에 설치할 hadoop이나 BigData 처리 기술 쪽에
  설정 파일들을 편집할 때 도움이 될 듯 하다. 



---------

- vi testfile
  vi 편집기 모드로 변경 
  - 기본은 명령 모드, 그래서 편집 모드로 이동하기 위해 a 누르기
  - --INSERT-- 나오고 편집 모드 됨
  - esc 누르면 처음의 명령 모드로 이동
  - :wq! [저장하고 빠져 나오겠다]
  - 나온 후 다시 vi testfile 입력하면 이제까지 입력한 게 보임 
  - 명령모드에서 yy[복사] p[붙여넣기]
    v[원하는 부분 선택] delete[지우기]

--------------

![image-20210811234151577](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210811234151577.png)  

리눅스에서 처리 기술 응용프로그램을 다룰 때 
많은 프로세스들이 생성 됨, 많은 데몬들이 동작하게 될 거다.
어떤 부분은 동작이 잘 될 거고, 어떤 부분은 동작을 잘 안할 수 있다. 

