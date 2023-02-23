import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import ipget
import servo_lock as servo_lock


app = FastAPI()
servo = servo_lock.ServoLock()

islocked = True


@app.post("/open")
def open_key():
    global islocked
    try:
        servo.open_key()
        islocked = False
        return JSONResponse(status_code=status.HTTP_200_OK, content="OK")
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="NG")


@app.post("/close")
def close_key():
    global islocked
    try:
        servo.close_key()
        islocked = True
        return JSONResponse(status_code=status.HTTP_200_OK, content="OK")
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="NG")


@app.get("/status")
def check_status():
    global islocked
    ip = ipget.ipget().ipaddr("wlan0")
    lock_status = "close" if islocked else "open"
    body = {"ip": ip, "status": lock_status}
    return JSONResponse(status_code=status.HTTP_200_OK, content=body)


if __name__ == "__main__":
    servo.close_key()
    uvicorn.run(app, host="0.0.0.0", port=8000)
