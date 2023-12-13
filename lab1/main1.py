import vk_api


def get_latest_posts(group_ids, access_token):
    vk_session = vk_api.VkApi(token=access_token)
    vk = vk_session.get_api()

    all_posts = []

    for group_id in group_ids:
        try:
            # Получаем информацию о группе
            group_info = vk.groups.getById(group_id=group_id)[0]

            # Получаем последние 100 записей со стены группы
            wall_posts = vk.wall.get(owner_id=-group_info["id"], count=100)["items"]

            # Добавляем информацию о группе к каждому посту
            for post in wall_posts:
                post["group_info"] = group_info

            all_posts.extend(wall_posts)

        except vk_api.exceptions.ApiError as e:
            print(f"Error fetching posts for group {group_id}: {e}")

    return all_posts


# Пример использования функции
group_ids = ["25380626", "112510789", "15722194"]  # Замените на реальные group_id
access_token = "vk1.a.SqqiRCJ7weMx1t3_GjG1T-b4NuscOYq2OGuGVtwAo1Pg3uBfyGO5HyzM5S_RIw2QCYZMJzdTTrFokSaGOAn7hoNn8eDKZDbuVjOZs1K5Bmiqbt4QQSbd9lF4hk-aMvllG4Rtq5Y0MG-BLoZdlSG-8HfRGMJopm5_fZuCDBbbwMqnhiyFZ9iJJkXDrezd8HVdlsN2ZaNH6zTm-EM2HiI76A"  # Замените на свой токен

latest_posts = get_latest_posts(group_ids, access_token)
for post in latest_posts:
    print(
        f"Group: {post['group_info']['name']}, Post Text: {post.get('text', 'No text available')}"
    )
