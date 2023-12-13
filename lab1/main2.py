from pyrogram import Client


def get_latest_messages_from_channels(
    channel_usernames, api_id, api_hash, phone_number
):
    messages = []

    with Client(phone_number, api_id, api_hash) as client:
        for username in channel_usernames:
            try:
                # Получаем информацию о канале
                channel_info = client.get_chat(username)

                # Получаем последние 100 сообщений из канала
                channel_messages = client.get_chat_history(channel_info.id, limit=100)

                # Добавляем информацию о канале к каждому сообщению
                for message in channel_messages:
                    message["channel_info"] = {
                        "id": channel_info.id,
                        "username": username,
                    }

                messages.extend(channel_messages)

            except Exception as e:
                print(f"Error fetching messages for channel {username}: {e}")

    return messages


# Пример использования функции
channel_usernames = [
    "@channel_username_1",
    "@channel_username_2",
    "@channel_username_3",
]
api_id = "your_api_id"  # Замените на свой API ID
api_hash = "your_api_hash"  # Замените на свой API Hash
phone_number = "your_phone_number"  # Замените на свой номер телефона

latest_messages = get_latest_messages_from_channels(
    channel_usernames, api_id, api_hash, phone_number
)
for message in latest_messages:
    print(
        f"Channel: {message['channel_info']['username']}, Message Text: {message.get('text', 'No text available')}"
    )
