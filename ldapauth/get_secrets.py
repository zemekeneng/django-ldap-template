# extracts a secrets dict from a .secret file

def get_secrets(filename):
    secrets = {}
    with open(filename) as f:
        for line in f.readlines():
            key_value = line.split('=')
            key, value = key_value[0].strip(), key_value[1].strip()
            secrets[key] = value
    return secrets
