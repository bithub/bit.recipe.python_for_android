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
        env_vars = {'BUILDOUT': path,
                    'ANDROIDSDK': sdk,
                    'ANDROIDNDK': ndk,
                    'ANDROIDNDKVER': ndk_version,
                    'ANDROIDAPI': api,
                    'GIT_SRC': o['src'],
                    'RECIPES': o['recipes'],
                    'PROJECT': self.name,
                    'PACKAGE': o['package'],
                    'APPNAME': self.name,
                    'VERSION': o['version'],
                    'ORIENTATION': o['orientation'],
                    'PERMISSIONS': o['permissions'],
                    'PRIVATE': o['private'],
                    'PUBLIC': o['public'],
                    }
        bash = '#/bin/bash\n'
        bash += '\n'.join(['%s=%s' % (k, v)
                          for k, v in env_vars.items()])
        open(target_install, 'w').write(bash + open(install).read())
        commands.getoutput('chmod +x %s' % target_install)

    def install(self):
        self._update()
        return ['bin/%s' % self.name]

    def update(self):
        self._update()
