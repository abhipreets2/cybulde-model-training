import os

def get_local_rank() -> int:
    return int(os.getenv("LOCAL_RANK", -1))
