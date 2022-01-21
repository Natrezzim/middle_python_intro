"""Генератор приветствий."""
import pprint


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия

    """
    pprint.pformat(name.lower())
    return 'Привет, {0}'.format(name).title()
