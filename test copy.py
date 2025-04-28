import time
from DDS_boardcast import DDS_Client, DDC_Subscriber

receiver = DDC_Subscriber("test_topic")

receiver.start_listening()
time.sleep(11)
receiver.stop_listening()
print("测试结束")