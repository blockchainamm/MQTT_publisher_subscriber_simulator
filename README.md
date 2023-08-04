# Message Queue Telemetry Transport (MQTT) publisher(IOT sensor) subscriber simulator

This python script simulates a Message Queue Publisher Subscriber model

There are two publishers and subscriber which performs a specific function:
publisher1 IOT device which simulates the logs of Inside temperature
publisher2 IOT device which simulates the logs of outside temperature
The subscriber listens to the temperature logs of both the publisher1 and publisher2 and consolidates these logs.

The example below is an extract of the logs displayed in order frol left to right Subscriber (positioned left), publisher1 (positioned in the middle with Inside temperature IOT sensor), publisher2 (positioned right with Outside temperature IOT sensor)

## Subscriber    Publisher1    Publisher2

<img width="639" alt="MQTT_publisher_subscriber" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/9d233d32-6abc-45c4-8dcf-1b85fba6d021">
