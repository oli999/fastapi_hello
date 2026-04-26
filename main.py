from fastapi import FastAPI, requests

# 1. FastAPI 인스턴스 생성
app = FastAPI()

# 2. 경로 데코레이터 설정 (GET 방식, 루트 경로)
@app.get("/")
async def root():
    # 3. JSON 형태로 리턴
    return {"message": "Hello World"}

# 3. health 체크용
@app.get("/health")
async def health():
    try:
        # DB ping (예시)
        # redis ping 등
        return {"status": "ok"}
    except:
        return {"status": "error"}

# 4. EC2 식별용 endpoint
import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/whoami")
async def whoami():
    # 현재 서버의 호스트 이름(컴퓨터 이름) 가져오기
    hostname = socket.gethostname()
    
    # 호스트 이름을 기반으로 사설 IP 주소 알아내기
    local_ip = socket.gethostbyname(hostname)
    
    return {
        "local_ip": local_ip
    }