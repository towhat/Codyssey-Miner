# Codyssey-Miner
# Course 1-2 반달곰 커피를 위한 웹 서버
# "Hello, DevOps!" 메시지 출력 프로그램
# 2025.07.16  Ver.1.0.0  최재호

from flask import Flask

# 변수 선언
app = Flask(__name__)

# 함수 선언
@app.route("/")
def hello_DevOps():
    return "Hello, DevOps~~~!"

# 메인 코드
if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)
    #app.run("localhost", debug=True)