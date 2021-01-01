import os
import random
import requests
from io import BytesIO
import numpy as np
import datetime as dt
from uuid import uuid4
from PIL import Image as pil
from django.core.files import File
from django.utils import timezone


def get_object_or_false(model, **kwargs):

    try:
        return model.objects.get(**kwargs)

    except model.DoesNotExist:
        return False


def filter_object_or_false(model, **kwargs):
    filter = model.objects.filter(**kwargs)

    if filter:
        return filter

    else:
        return False


def filter_instance_or_false(instance, **kwargs):
    filter = instance.filter(**kwargs)

    if filter:
        return filter

    return False


def get_upload_path(instance, filename):
    path = os.path.join(
        instance._meta.app_label,
        instance._meta.model_name,
        timezone.now().strftime('%Y'),
        timezone.now().strftime('%m'),
        uuid4().hex,
        filename
    )

    return path


def get_resize_image_or_none(image, size, prefix, format=None):

    try:
        im = pil.open(image)
        im.thumbnail(size, pil.ANTIALIAS)

        filename = os.path.basename(image.name)
        basename = os.path.splitext(filename)[0]

        if format in ['jpeg', 'png', 'bmp'] and format != im.format:
            im = im.convert('RGB')
        else:
            format = im.format.lower()

        thumb_io = BytesIO()
        im.save(thumb_io, format)

        return File(thumb_io, name=prefix + basename + '.' + format)

    except:
       return None


def strp_dt_or_nan(x, fmt):

    try:
        return dt.datetime.strptime(x, fmt)

    except:
        return np.nan


def strp_time_or_nan(x, fmt):

    try:
        return dt.datetime.strptime(x, fmt).time()

    except:
        return np.nan


def check_url_exists_or_false(path):
    exists = False

    req = requests.head(path, timeout=5)

    if req.status_code == requests.codes.ok:
        exists = True

    return exists


def get_random_agent_or_false():
    agent_list = "user_agent_list.txt"

    agent = False

    if os.path.exists(agent_list):

        with open(agent_list, 'r') as f:
            content = f.read(1)

            if content:
                lines = f.readlines()
                agent = str(random.choice(lines)).replace('\n', '')

    return agent


def get_request_head():
    head = {
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    agent = get_random_agent_or_false()

    if agent:
        head['User-Agent'] = agent

    return head


def get_url_as_file_or_false(url):
    head = get_request_head()

    req = requests.get(url, stream=True, headers=head, timeout=10)
    req.raw.decode_content = True

    file = False

    if req.status_code == 200:
        image_io = BytesIO()
        image_io.write(req.content)

        file_name = url.split('/')[-1]

        file = File(image_io, name=file_name)

    return file