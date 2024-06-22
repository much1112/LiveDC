from pypresence import Presence
import time

rpc = Presence("1131127607719628830")
rpc.connect()
while 1:
    rpc.update(
        state="到底為甚麼有作業",
        details="寫作業",
        large_image="penguin-1",
    )
    time.sleep(1)
