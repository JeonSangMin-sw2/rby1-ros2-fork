# rby1_moveit packege
- 이 문서는 rby1 로봇을 moveit 환경에서 사용해보기 위한 패키지.
- rby1_description 패키지에서 모델을 불러와 moveit 환경에서 사용.
- docker 시뮬레이션과도 연동 가능
- moveit 사용에 대한 번거로움을 줄이기 위해 bashrc에서 항상 moveit관련 패키지를 source하도록 설정
  ```bash
  sudo nano ~/.bashrc
  #파일 아래에 해당 문구를 삽입
  source ~/ws_moveit2/install/setup.bash
  ```

## 모델구성
1. A 모델
- rby1a_v1_0
- rby1a_v1_1
- rby1a_v1_2

2. M 모델
- rby1m_v1_0
- rby1m_v1_1
- rby1m_v1_2
- rby1m_v1_3

## demo 실행방법

```bash
ros2 launch rby1a_v1_1_moveit demo.launch.py
```



