__author__ = 'peppe'


from django.core.files.storage import get_storage_class
from storages.backends.ftp import FTPStorage
from storages.backends.sftpstorage import SFTPStorage

class CachedFTPStorage(FTPStorage):
    """
    FTP storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        super(CachedFTPStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedFTPStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name


class CachedSFTPStorage(SFTPStorage):
    """
    SFTP storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        super(CachedSFTPStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedSFTPStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name

#    def path(self, name):
#        return None
#        print self.local_storage.path(name)
#        return self.local_storage.path(name)

    def _mkdir(self, path):
        """Create directory, recursing up to create parent dirs if
        necessary."""

        print 'path', path
        parent = self._pathmod.dirname(path)
        print 'parent', parent
        if not self.exists(parent):
            self._mkdir(parent)
        self.sftp.mkdir(path)

        if self._dir_mode is not None:
            self.sftp.chmod(path, self._dir_mode)

        if self._uid or self._gid:
            self._chown(path, uid=self._uid, gid=self._gid)



#
from storages.backends.s3boto import S3BotoStorage

class CachedS3BotoStorage(S3BotoStorage):
    """
    S3 storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        name = super(CachedS3BotoStorage, self).save(name, content)
        self.local_storage._save(name, content)
        return name

    def path(self, name):
#        return None
        return self.local_storage.path(name)