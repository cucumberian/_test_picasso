import hashlib
from celery import shared_task
from .models import File


@shared_task
def file_process(file_id):
    file = File.objects.get(id=file_id)
    sha1 = get_hash(file.file.path)
    file.processed = True
    file.save()
    return sha1


def get_hash(filename: str) -> str:
    BUF_SIZE = 65536  # 64KiB buffer size
    sha1 = hashlib.sha1()
    with open(filename, "rb") as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()
