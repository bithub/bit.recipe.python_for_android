import logging
import os
import pkg_resources
import commands


class Recipe:

    def __init__(self, buildout, name, options):
        self.name = name
        self.options = options
        self.logger = logging.getLogger(name)

    def _update(self):
        install = pkg_resources.resource_filename(
            __name__, 'python_for_android')
        path = os.getcwd()
        target_install = os.path.join('bin', self.name)
        sdk = os.path.join(path, self.options['sdk'])
        ndk = os.path.join(path, self.options['ndk'])
        api = self.options['api']
        ndk_version = self.options['ndk_version']
        if self.name in os.listdir('bin'):
            os.unlink(target_install)
        o = self.options
        bash = '#!/bin/bash\n'
        env_vars = {'ANDROIDSDK': sdk,
                    'ANDROIDNDK': ndk,
                    'ANDROIDNDKVER': ndk_version,
                    'ANDROIDAPI': api,
                    }
        bash += '\n'.join(['export %s=%s' % (k, v)
                          for k, v in env_vars.items()])
        bash += '\n'
        env_vars = {'BUILDOUT': path,
                    'GIT_SRC': o['src'],
                    'RECIPES': '"%s"' % o['recipes'],
                    'PROJECT': self.name,
                    'PACKAGE': o['package'],
                    'APPNAME': self.name,
                    'VERSION': o['version'],
                    'ORIENTATION': o['orientation'],
                    'PERMISSIONS': o['permissions'],
                    'PRIVATE': os.path.realpath(o['private']),
                    'PUBLIC': os.path.realpath(o['public']),
                    }
        bash += '\n'.join(['%s=%s' % (k, v)
                          for k, v in env_vars.items()])
        open(target_install, 'w').write(bash + open(install).read())
        commands.getoutput('chmod +x %s' % target_install)

    def _install(self):
        path = os.getcwd()
        target_install = os.path.join(path, 'bin', self.name)
        print commands.getoutput('%s install' % target_install)

    def install(self):
        self._update()
        self._install()
        return ['bin/%s' % self.name]

    def update(self):
        self._install()
        self._update()
