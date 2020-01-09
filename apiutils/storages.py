# encoding: utf-8

from django.core.files.storage import FileSystemStorage


class EnableUrlFileSystemStorage(FileSystemStorage):
    def url(self, name):
        if name.startswith("https://") or name.startswith("http://"):
            return name
        return super(EnableUrlFileSystemStorage, self).url(name)
