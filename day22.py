from collections.abc import Iterator

from utils import get_input


def mix_prune(secret: int, value: int) -> int:
    return (secret ^ value) % 16777216


def next_secret(secret: int):
    first = mix_prune(secret, secret * 64)
    second = mix_prune(first, first // 32)
    third = mix_prune(second, second * 2048)
    return third


def iter_secrets(secret: int) -> Iterator[int]:
    for _ in range(2000):
        secret = next_secret(secret)
        yield secret


def last[T](it: Iterator[T]):
    *_, last = it
    return last


if __name__ == "__main__":
    secrets = [int(secret) for secret in get_input(22).splitlines()]
    print(sum(last(iter_secrets(secret)) for secret in secrets))
