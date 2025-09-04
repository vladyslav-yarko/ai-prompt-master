from src.bot.utils.text import Text


s_authorize_hand_text = Text("""
*🔐 Авторизація*

Для збереження твоїх результатів і досягнень потрібна авторизація.

✅ Авторизація пройшла успішно!
""")


e_authorize_hand_text = Text("""
❗ Ви вже авторизовані.

Якщо хочете почати спочатку — скористайтесь командою */delete*
""")


s_delete_command_hand_text = Text("""
⚠️ Ви впевнені, що хочете *видалити акаунт*?

Це призведе до *повного видалення всіх даних*. Повернення буде неможливим.
""")


e_delete_command_hand_text = Text("""
❗ Ви ще *не створили акаунт*.

Спершу скористайтесь командою */authorize*
""")


s_delete_hand_text = Text("""
✅ Ваш акаунт було *успішно видалено*.

Ви можете почати заново, використавши команду */authorize*
""")


s_profile_hand_text = Text("""
👤 *Профіль користувача*

{% if username %}
📛 Ім'я: {{ username }}
{% endif %}

🏆 Досягнення: 
{% if achievements %}
{% for achievement in achievements %}
{{ achievement.emoji }} *{{ achievement.title }}*:
{{ achievement.description }}
{% endfor %}
{% else %}
🕸️ Тут поки порожньо... Відкрий свої перші досягнення!
{% endif %}

📚 Ігор зіграно: *{{ statistics.totalGamesPlayed }}*

📊 Рейтинг: *{{ statistics.totalScore }}*

📶 Рівень: {{ level.title }}
""")


e_profile_hand_text = Text("""
❗ Ви ще не авторизовані. 
Використайте команду */authorize*, щоб створити акаунт.
""")
