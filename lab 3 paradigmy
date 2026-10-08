import unittest


def validate_achievement(achievement):
    """Проверяет правильность одного достижения."""

    if not isinstance(achievement, dict):
        raise TypeError("Достижение должно быть словарём.")

    required_fields = {"name", "category", "score"}

    if not required_fields.issubset(achievement):
        raise ValueError("Не хватает обязательных полей.")

    if not isinstance(achievement["name"], str) or not achievement["name"].strip():
        raise ValueError("Название достижения не может быть пустым.")

    if not isinstance(achievement["category"], str) or not achievement["category"].strip():
        raise ValueError("Категория не может быть пустой.")

    if isinstance(achievement["score"], bool) or not isinstance(
        achievement["score"], (int, float)
    ):
        raise TypeError("Баллы должны быть числом.")

    if achievement["score"] < 0:
        raise ValueError("Баллы не могут быть отрицательными.")

    return True


def validate_all_achievements(achievements):
    """Проверяет список достижений."""

    if not isinstance(achievements, list):
        raise TypeError("Достижения должны быть списком.")

    if not achievements:
        raise ValueError("Список достижений не должен быть пустым.")

    for achievement in achievements:
        validate_achievement(achievement)

    return True


def group_scores(achievements):
    """Группирует баллы по категориям."""

    validate_all_achievements(achievements)

    grouped = {}

    for achievement in achievements:
        category = achievement["category"]
        score = achievement["score"]

        if category not in grouped:
            grouped[category] = 0

        grouped[category] += score

    return grouped


def total_score(category_scores):
    """Вычисляет общую сумму баллов."""

    if not isinstance(category_scores, dict):
        raise TypeError("Баллы должны быть словарём.")

    return sum(category_scores.values())


def calculate_category_limit(raw_total, limit=0.40):
    """Рассчитывает максимальный вклад одной категории."""

    if raw_total < 0:
        raise ValueError("Общая сумма не может быть отрицательной.")

    if not 0 < limit <= 1:
        raise ValueError("Ограничение должно быть от 0 до 1.")

    return raw_total * limit


def apply_category_limit(category_scores, raw_total, limit=0.40):
    """Ограничивает вклад каждой категории 40%."""

    category_limit = calculate_category_limit(raw_total, limit)

    limited_scores = {}

    for category, score in category_scores.items():
        limited_scores[category] = min(score, category_limit)

    return limited_scores


def build_rating(category_scores):
    """Создаёт рейтинг категорий по убыванию баллов."""

    if not isinstance(category_scores, dict):
        raise TypeError("Баллы должны быть словарём.")

    return sorted(
        category_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )


def format_report(raw_scores, limited_scores, raw_total, final_total):
    """Формирует итоговый отчёт."""

    rating = build_rating(limited_scores)

    lines = []

    lines.append("=== ПОРТФОЛИО СТУДЕНТА ===")
    lines.append("")
    lines.append(f"Исходная сумма баллов: {raw_total:.2f}")
    lines.append(
        f"Максимальный вклад одной категории (40%): "
        f"{raw_total * 0.40:.2f}"
    )
    lines.append(f"Итоговый рейтинг: {final_total:.2f}")
    lines.append("")
    lines.append("Рейтинг категорий:")

    for position, (category, score) in enumerate(rating, start=1):
        lines.append(
            f"{position}. {category}: {score:.2f} баллов"
        )

    return "\n".join(lines)


def main():
    """Основная программа."""

    achievements = [
        {
            "name": "Олимпиада по программированию",
            "category": "Учёба",
            "score": 90
        },
        {
            "name": "Научная конференция",
            "category": "Учёба",
            "score": 70
        },
        {
            "name": "Участие в хакатоне",
            "category": "Проекты",
            "score": 80
        },
        {
            "name": "Волонтёрство",
            "category": "Общественная деятельность",
            "score": 60
        },
        {
            "name": "Спортивные соревнования",
            "category": "Спорт",
            "score": 50
        },
        {
            "name": "Студенческий конкурс",
            "category": "Конкурсы",
            "score": 40
        }
    ]

    # Проверяем данные
    validate_all_achievements(achievements)

    # Группируем баллы
    grouped_scores = group_scores(achievements)

    # Считаем исходную сумму
    raw_total = total_score(grouped_scores)

    # Ограничиваем вклад категории 40%
    limited_scores = apply_category_limit(
        grouped_scores,
        raw_total
    )

    # Считаем итоговый рейтинг
    final_total = total_score(limited_scores)

    # Выводим результат
    print(
        format_report(
            grouped_scores,
            limited_scores,
            raw_total,
            final_total
        )
    )


# =========================
# АВТОМАТИЧЕСКИЕ ТЕСТЫ
# =========================

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.achievements = [
            {
                "name": "Олимпиада",
                "category": "Учёба",
                "score": 90
            },
            {
                "name": "Хакатон",
                "category": "Проекты",
                "score": 60
            },
            {
                "name": "Волонтёрство",
                "category": "Общество",
                "score": 30
            }
        ]

    # Тест 1
    def test_validate_achievement(self):
        self.assertTrue(
            validate_achievement(self.achievements[0])
        )

    # Тест 2
    def test_invalid_score(self):
        achievement = {
            "name": "Олимпиада",
            "category": "Учёба",
            "score": -10
        }

        with self.assertRaises(ValueError):
            validate_achievement(achievement)

    # Тест 3
    def test_group_scores(self):
        result = group_scores(self.achievements)

        expected = {
            "Учёба": 90,
            "Проекты": 60,
            "Общество": 30
        }

        self.assertEqual(result, expected)

    # Тест 4
    def test_total_score(self):
        scores = {
            "Учёба": 90,
            "Проекты": 60,
            "Общество": 30
        }

        self.assertEqual(total_score(scores), 180)

    # Тест 5
    def test_category_limit(self):
        scores = {
            "Учёба": 150,
            "Проекты": 30
        }

        limited = apply_category_limit(
            scores,
            raw_total=180
        )

        # 40% от 180 = 72
        self.assertEqual(limited["Учёба"], 72)
        self.assertEqual(limited["Проекты"], 30)

    # Тест 6
    def test_build_rating(self):
        scores = {
            "Учёба": 50,
            "Проекты": 90,
            "Спорт": 30
        }

        rating = build_rating(scores)

        expected = [
            ("Проекты", 90),
            ("Учёба", 50),
            ("Спорт", 30)
        ]

        self.assertEqual(rating, expected)

    # Тест 7
    def test_category_limit_calculation(self):
        self.assertEqual(
            calculate_category_limit(200),
            80
        )

    # Тест 8
    def test_invalid_empty_list(self):
        with self.assertRaises(ValueError):
            validate_all_achievements([])


# =========================
# ЗАПУСК
# =========================

if __name__ == "__main__":

    main()

    print("\n=== ЗАПУСК ТЕСТОВ ===")

    unittest.main(
        argv=["first-arg-is-ignored"],
        exit=False
    )
    
