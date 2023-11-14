# 로그 생성기 기획

## 가설

* 인원의 삭제, 변동에 따른 변경사항은 고려하지 않는다.
  *  퇴직자나 보직이 완전히 바뀐 직원이 이전 파일을 보는 것은 간단한 규칙으로 잡아낼 수 있음으로 고려하지 않는다.
  * 하지만 확장성을 위해 부서 내 인원 변경에 쓰이는 메소드는 구현하도록 한다.
* ''중앙 파일 서버''가 존재하고 "endpont monitoring"이 이루어지는 상황을 가정한다.
  * 중앙 파일 서버가 존재하여 로그에 남을 수 있는 형태로 ''파일 공유 요청''과 해당 요청의 처리가 이루어지는 상황을 가정한다.
  *  "endpont monitoring"이 존재하여 직원의 행위 로그가 정상적으로 수집되는 상황 가정한다.
* 일반적인 상황에서는 타 부서 사이에서 파일의 공유 전송이 잘 일어나지 않을 것으로 가정한다.
  * 다만 여러 부서가 협업을 하거나, 파일 자체가 타 부서에게 공유용으로 생성된 파일이라면 공유 요청이나 전달이 이루어질 수 있다고 가정한다.
* 직원들의 행동은 일반 상태 시 패턴과 부서 내 이벤트가 존재할 시 패턴이 따로 존재하여 로그 생성기에서는 이를 반영해야 한다고 가정한다.
  * 통상 업무 진행 시와 부서 프로젝트 진행 같은 부서 내 이벤트 존재 시의 업무 행동 패턴은 다를 것으로 예상된다.



## 주요 요소 기획안

### 파일

* DB에 파일 정보를 기록하여 "중앙 파일 서버"의 역활 구현
* 필요 정보
  * 파일 이름
  * 파일 등급
  * 관련 부서
  * 소유자(세부 정의 필요)
    * 읽기 권한 소유자
    * 쓰기 권한 소유자
    * 실행 권한 소유자
  * 최초 등록 시간
  * 최종 갱신 시간
* 직원의 로컬 PC에 저장하는 상황을 가정하기 위해 class의 형태로 구현 또한 필요 



### 부서

* 직원들의 집합
* 타 부서간 협업 이벤트나 부서 내 협업 이벤트 관련한 제어가 이루어짐
* 구성 요소
  * 부서명
  * 부서내 직원 등급별 직원들의 일반 상태 시의 행동이 정의된 dictionary
  * 부서내 직원들의 부서 이벤트 시 행동이 정의된(또는 뼈대가 되는 정보가 있는) dictionary
    * 해당 정보를 통해 부서 이벤트중 수행하는 행동 패턴을 랜덤하게 생성하여 직원들에게 부여하도록 설계하면 어떨까함
  * 직원 객체 리스트
  * 부서 이벤트 관리 메소드
  * 부서 이벤트 관련 행동 패턴 관리 메소드
  * 부서 인원 추가 관리 메소드
  * 부서 인원 삭제 관리 메소드
  * 부서 인원 변경 관리 메소드



### 직원

* 작업을 수행하는 가장 작은 단위

* 부서에서 받은 행동 패턴을 기본으로 사용하나, 별도로 선언된 패턴이 있다면 해당 패턴 사용

* 구성 요소

  * 이름
  * 등급
  * 부서
  * 부서 이벤트 관련 플래그 및 제어 값들 (협업 이벤트 시 어떤 부서들끼리 협업중인지 등...)
  * 로컬 파일 리스트 
    * 로컬 파일 서버 등록 여부는 로컬 파일 클래스 내부에서 관리
  * 행동 패턴 값(dictionary)
  * 사이클 내 작업 수행 여부 랜덤 결정 관련 메소드
  * 행동 패턴 갱신 관련 메소드
  * 행동 랜덤 결정 관련 메소드
  * 행동 타겟 랜덤 지정 관리 메소드
  * 로컬 파일 관리 관련 메소드

  ### 잠재적 악성 직원

  * 직원 class를 상속받아서 선언되는 class이며, 실질적으로 사용될 class이다.
  * 랜덤한 경우 일반 직원이 악성 직원이 되어 지정된 시나리오 대로 악성 행위를 수행
  * 한명 또는 여려명이 악성 행위의 협업자가 될 수 있음
  * 시나리오에 따른 행동 패턴과 악성 발현 여부와 관련 플래그 및 제어 값들이 추가로 필요



### 행동

* 직원들의 행동은 단일 행동과 복합 행동으로 구분할 수 있음

  ### 단일 행동

  * 파일과 관련돤 행동 중 실제로 로깅이 되는 가장 작은 단위의 행동
  * 파일과 상호작용과 관련된 행동
    * 파일 생성
    * 파일 읽기
      * "중앙 파일 서버"에 있는 파일을 다시 가져오는 경우도 읽기로 해야 하는지 다른 행동으로 정의해야하는지는 고려 필요
    * 파일 쓰기 - 갱신
      * 소유자가 "중앙 파일 서버"에 등록된 파일을 수정한 경우 갱신또한 진행된다고 가정한다.
    * 파일 실행
    * 파일 등록
  * 파일의 공유와 관련된 행동
    * 파일 전송
    * 파일 공유 요청
    * 파일 공유 요청 수락
    * 파일 공유 요청 거부

  

  ### 복합 행동

  * 여러 단일 행동의 묶음으로 정의되는 행동이 복합행동

  * 복합행동 그 자체는 로깅되지 않으나 복합행동을 수행하는 과정에서 수행하는 단일행동들이 로깅됨

  * XX 작업을 한 후 YY를 한다 같은 패턴 때문에 사전에 정의할 필요성이 존재하였음

  * 하드코딩이 아닌 다른 방법으로 선언, 관리될 수 있으면 확장성 측면에서 도움이 될 것으로 보이나 어려워보임

  * 복합행동의 예시

    * 하위 직원이 파일을 만들고 상위 직원이 산출물들을 취합되는 과정

      * 복합 행동1: 파일 취합 및 정리

        * 상위 직원이 하위 부서원이 생성한 파일을 일정량 수집하여 정리 파일을 생성함
        * 충분한 파일이 모일떄까지 대기를 하다가, 파일이 모인 후 상위 단계 파일(정리 파일)을 생성

      * 복합 행동2: 파일 상신

        * 파일을 생성, 수정한 후 최종 작업물을 상위 직원에게 전송

      * 해당 행동에 관련된 계층은 2단계 이상이 될 것("파일 취합 및 정리"와 "파일 상신"을 같이 수행하는 직원이 존재할 수 있음)

        

    * 부서간 협업을 위해 자료를 공유 받고 공유받은 자료를 통해서 파일을 생성, 수정하는 경우

      * 복합 행동1: 타 부서 문서 수집 후 정리
        * 일정량의 타 부서 파일을 전송받거나 공유 요청후 공유받은 후 파일 생성, 수정하여 최종 작업물 생성
        * 부서 간 협업시 수행되는 복합행동
      * 복합 행동2: 부서 문서 전송
        * 부서간 협업에 필요한 문서들을 일부 또는 전부 전송
        * 부서 간 협업시 수행되는 복합행동



## 사이클 별 로그 생성 과정

### 악의적인 직원을 고려하지 않는 경우의 흐름

1. #### 부서 이벤트 결정

   * 부서 이벤트 여부 결정 및 관련 행동 패턴 관리

2. #### 모든 직원 객체들에게 질의하여 해당 사이클에 참가 여부와 행동 횟수 수집

   * 직원들은 상황에 따라 랜덤하게 사이클 참가 여부와 참가 시 행동 횟수을 결정함

3. #### 수집한 정보를 토대로 랜덤한 순서의 작업 큐 생성

   * 직원들의 작업 순서가 객체 질의 순서 그대로 고정되는 것을 방지하기 위해 순서를 섞음

4. #### 작업 큐 순서로 각 직원 객체에게 행동 요구



### 악의적인 직원이 존재하는 경우

최상위 단계에 아래의 작업추가

0. #### 악의적인 직원 활성화

   * 단순히 어떤 직원(들)이 악의적인 직원이 될지 사이클 초반에 선택하는 과정이 추가되면 된다.



## 기타 사항

1. 전역 설정 후보: 사이클당 시간, 최대 로컬 파일 수

2. 부서원 행동 패턴 등의 모든 config는  json 형태로 저장되어 관리되어야 함

   (xml이 안될 이유는 없지만 json을 사용할 예정)

3. 악성 행위 시나리오 중 해커가 취약점을 이용해 파일을 수집하는 경우의 패턴은...

   - 어러 컴퓨터/계정에서 사칭한 계정으로 파일을 전송하는 형태로 나타날 것으로 추정중

4. 사이클 내 행동 간의 시간 간격을 어떤 방식으로 정할지는 추가적인 고려가 필요



