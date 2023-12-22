import unittest
from unittest.mock import patch
from io import StringIO
import asyncio
import tkinter as tk
from tkinter import scrolledtext, simpledialog

from client import Client  # Замените "your_module" на реальное имя вашего модуля


class TestClient(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.get_event_loop()
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    @patch("asyncio.open_connection")
    def test_connect(self, mock_open_connection):
        client = Client(self.root, self.loop)
        self.assertIsNone(client.writer)
        self.assertIsNone(client.reader)

        mock_open_connection.return_value = (
            asyncio.StreamReader(),
            asyncio.StreamWriter(None, None, None, None),
        )
        self.loop.run_until_complete(client.connect())

        self.assertIsNotNone(client.writer)
        self.assertIsNotNone(client.reader)

    def test_start_receive(self):
        client = Client(self.root, self.loop)
        client.reader = asyncio.StreamReader()
        client.writer = asyncio.StreamWriter(None, None, None, None)

        # Redirect stdout to capture print output
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.loop.run_until_complete(client.start_receive())

        # Here, you can check the content of mock_stdout to see if the expected messages are printed

    def test_send(self):
        client = Client(self.root, self.loop)
        client.writer = asyncio.StreamWriter(None, None, None, None)

        # Redirect stdout to capture print output
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            client.send(None)  # Simulate send on Enter key press

        # Here, you can check the content of mock_stdout to see if the expected messages are printed


if __name__ == "__main__":
    unittest.main()
