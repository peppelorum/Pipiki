__author__ = 'peppe'


import os
import paramiko

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

    def _connect(self):
        self._ssh = paramiko.SSHClient()

        if self._known_host_file is not None:
#            print 'sadsad', self._known_host_file
#            path = self._known_host_file.split('/')
#            path_split = self._known_host_file.split('/')
#            path_to_create = '/'.join(path_split[:-1])
#            file_to_create = path_split[-1]

#            if not os.path.exists(path_to_create):
#                os.makedirs(path_to_create)
#                f = file(self._known_host_file, "w")
#                f.close()

            self._ssh.load_host_keys(self._known_host_file)
        else:
            # automatically add host keys from current user.
            self._ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))

        # and automatically add new host keys for hosts we haven't seen before.
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self._ssh.connect(self._host, **self._params)
        except paramiko.AuthenticationException, e:
            if self._interactive and 'password' not in self._params:
                # If authentication has failed, and we haven't already tried
                # username/password, and configuration allows it, then try
                # again with username/password.
                if 'username' not in self._params:
                    self._params['username'] = getpass.getuser()
                self._params['password'] = getpass.getpass()
                self._connect()
            else:
                raise paramiko.AuthenticationException, e
        except Exception, e:
            print e

        if not hasattr(self, '_sftp'):
            self._sftp = self._ssh.open_sftp()

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