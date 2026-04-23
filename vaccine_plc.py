from opcua import Server
import paho.mqtt.client as mqtt
import random
import time

# ---------- OPC UA ----------
server = Server()
server.set_endpoint("opc.tcp://127.0.0.1:4840")

uri = "http://chahinez.vaccine.monitoring"
idx = server.register_namespace(uri)
node = server.get_objects_node()

fridge = node.add_object(idx, "Fridge")

temp_top = fridge.add_variable(idx, "Temp_Top", 5.0)
temp_bottom = fridge.add_variable(idx, "Temp_Bottom", 5.0)
door_status = fridge.add_variable(idx, "Door_Status", 0)

temp_top.set_writable()
temp_bottom.set_writable()
door_status.set_writable()

# ---------- MQTT ----------
client = mqtt.Client()
client.connect("localhost", 1883)

server.start()
print("OPC UA + MQTT running...")

try:
    while True:
        door = random.choice([0, 1])
        door_status.set_value(door)

        if door == 1:
            new_top = random.uniform(7.0, 10.0)
            new_bottom = random.uniform(5.0, 8.0)
        else:
            new_top = random.uniform(2.0, 5.0)
            new_bottom = random.uniform(2.0, 5.0)

        temp_top.set_value(new_top)
        temp_bottom.set_value(new_bottom)

        # 🔥 إرسال إلى MQTT
        client.publish("fridge/temp_top", new_top)
        client.publish("fridge/temp_bottom", new_bottom)
        client.publish("fridge/door", door)

        print(f"Porte: {door} | Haut: {new_top:.2f}°C | Bas: {new_bottom:.2f}°C")

        time.sleep(2)

finally:
    server.stop()