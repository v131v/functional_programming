import tkinter
import unittest
import asyncio
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from tkinter import Tk
from client import (
    ChatClient,
)


class TestChatClient(unittest.IsolatedAsyncioTestCase):
    async def test_send_message(self):
        root = Tk()
        loop = asyncio.get_event_loop()
        client = ChatClient(root, loop)

        with patch.object(client, "writer") as mock_writer:
            with patch.object(client, "entry", create=True) as mock_entry:
                mock_entry.get.return_value = "Test message"
                await client.send(None)

        # Проверка, что write был вызван с правильными аргументами
        mock_writer.write.assert_called_once_with(
            f"{client.name}: Test message\n".encode()
        )

    async def test_receive_message(self):
        root = Tk()
        loop = asyncio.get_event_loop()
        client = ChatClient(root, loop)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch.object(client.reader, "read") as mock_reader:
                mock_reader.return_value = asyncio.Future()
                mock_reader.return_value.set_result("Server message".encode())
                await client.start_receive()

        # Проверка, что текстовая область была обновлена с правильным сообщением
        self.assertIn("Server message", client.text_area.get("1.0", tkinter.END))

    async def test_connect(self):
        root = Tk()
        loop = asyncio.get_event_loop()
        client = ChatClient(root, loop)

        with patch("asyncio.open_connection") as mock_open_connection:
            with patch.object(client.writer, "write") as mock_write:
                await client.connect()

        # Проверка, что open_connection вызывается с правильными аргументами
        mock_open_connection.assert_called_once_with("127.0.0.1", 8888)

        # Проверка, что write вызывается с правильным аргументом
        mock_write.assert_called_once_with(client.room.encode())


if __name__ == "__main__":
    unittest.main()
