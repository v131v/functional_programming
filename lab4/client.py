import asyncio
import tkinter as tk
from tkinter import scrolledtext, simpledialog


class ChatClient:
    def __init__(self, root, loop):
        self.root = root
        self.loop = loop
        self.name = simpledialog.askstring("Name", "Enter name:")
        self.room = simpledialog.askstring("Room", "Enter room name:")
        self.writer: asyncio.StreamWriter = None
        self.reader: asyncio.StreamReader = None
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title(f"Чат - {self.name}")
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.entry = tk.Entry(self.root)
        self.entry.pack(expand=True, fill=tk.X)
        self.entry.bind("<Return>", self.send)

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection("127.0.0.1", 8888)

        self.writer.write(self.room.encode())
        await self.writer.drain()

        self.loop.create_task(self.start_receive())

    async def start_receive(self):
        while True:
            data = await self.reader.read(100)
            message = data.decode()
            print(message, self.name)
            self.text_area.insert(tk.END, message)

    def send(self, event):
        message = self.entry.get()
        if message:
            self.writer.write(f"{self.name}: {message}\n".encode())
            self.entry.delete(0, tk.END)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    root = tk.Tk()
    client = ChatClient(root, loop)

    async def tkUpdate():
        while True:
            root.update()
            await asyncio.sleep(0.05)

    try:
        loop.run_until_complete(
            asyncio.gather(
                loop.create_task(tkUpdate()),
                loop.create_task(client.connect()),
            )
        )
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
