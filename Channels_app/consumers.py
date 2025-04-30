from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):
     def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

     def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text":"hello i got your message",
        })

     def webscoket_disconnect(self):
         self.send({
              "type": "websocket.close"
         })