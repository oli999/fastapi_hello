from fastapi import FastAPI

# 1. FastAPI 인스턴스 생성
app = FastAPI()

# 2. 경로 데코레이터 설정 (GET 방식, 루트 경로)
@app.get("/")
async def root():
    # 3. JSON 형태로 리턴
    return {"message": "Hello World"}

# 4. 특정 경로 추가 테스트
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}!"}