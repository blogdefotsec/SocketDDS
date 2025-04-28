import time
from DDS_boardcast import DDS_Client, DDC_Subscriber

boradcast = DDS_Client("test", ["test_topic", "test_topic2"])
for i in range(10):
    boradcast.broad_cast("test_topic", f"test_message_{i}")
    time.sleep(1)
print("测试结束")