from utils import get_input


def mix_prune(secret: int, value: int):
    # 16777216 is 2**24, equivalent to a bitmask of 0xFFFFFF
    return secret ^ value & 0xFFFFFF


def next_secret(secret: int):
    secret = mix_prune(secret, secret * 64)
    secret = mix_prune(secret, secret // 32)
    secret = mix_prune(secret, secret * 2048)
    return secret


def secrets(secret: int):
    return [secret, *(secret := next_secret(secret) for _ in range(2000))]


if __name__ == "__main__":
    all_secrets = [secrets(int(secret)) for secret in get_input(22).splitlines()]
    print(sum(secrets[-1] for secrets in all_secrets))
