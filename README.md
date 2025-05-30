# 벽돌 깨기 게임 (Brick Breaker Game)

이 프로젝트는 Python과 Pygame 라이브러리를 사용하여 개발된 간단한 벽돌 깨기 게임입니다. 플레이어는 패들을 움직여 공을 튕기며 벽돌을 부수는 방식으로 게임을 진행합니다.

---

## 게임 설명

- **목표**: 모든 벽돌을 부수고 점수를 획득하세요.
- **조작 방법**:
  - **왼쪽 화살표 키**: 패들을 왼쪽으로 이동
  - **오른쪽 화살표 키**: 패들을 오른쪽으로 이동
- **게임 종료 조건**:
  - 공이 바닥에 떨어지면 목숨이 감소합니다.
  - 목숨이 0이 되면 게임 오버입니다.
- **승리 조건**:
  - 모든 벽돌을 부수면 승리 메시지가 표시됩니다.

---

## 주요 기능

1. **공과 패들**:
   - 공은 노란색에 약간 주황빛이 도는 색 `(255, 200, 100)`으로 설정되어 있습니다.
   - 패들은 녹색 `(0, 255, 0)`으로 설정되어 있습니다.

2. **벽돌**:
   - 벽돌은 여러 줄로 배치되며, 공이 충돌하면 제거됩니다.

3. **배경색**:
   - 배경은 밝은 하늘색 `(220, 240, 255)`으로 설정되어 있습니다.

4. **점수 및 목숨 표시**:
   - 화면 왼쪽 상단에 점수와 남은 목숨이 검정색으로 표시됩니다.

5. **게임 오버 및 승리 화면**:
   - 게임 오버 시 "Game Over" 메시지가 표시됩니다.
   - 승리 시 "You Win!" 메시지가 표시됩니다.

---

## 설치 및 실행 방법

1. **Python 설치**:
   - Python 3.8 이상이 설치되어 있어야 합니다.
   - [Python 공식 웹사이트](https://www.python.org/)에서 Python을 다운로드하고 설치하세요.

2. **Pygame 설치**:
   - 아래 명령어를 사용하여 Pygame을 설치하세요:
     ```bash
     pip install pygame
     ```

3. **게임 실행**:
   - 터미널에서 프로젝트 디렉토리로 이동한 후, 아래 명령어를 실행하세요:
     ```bash
     python src/main.py
     ```

---

## 파일 구조

```
brick_breaker_game/
├── src/
│   ├── main.py               # 게임 실행 파일
│   ├── game/
│   │   ├── game_logic.py     # 게임 로직
│   │   ├── paddle.py         # 패들 클래스
│   │   ├── ball.py           # 공 클래스
│   │   ├── brick.py          # 벽돌 클래스
├── README.md                 # 프로젝트 설명 파일
```