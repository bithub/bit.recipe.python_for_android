import logging
import os
import shutil
import pkg_resources
import commands

class Recipe:
    def __init__(self, buildout, name, options):
        self.options = options
        self.logger = logging.getLogger(name)

    def _update(self):
        apis = self.options['apis'].split('\n')        
        sdk = pkg_resources.resource_filename(__name__, 'install_python_for_android')
        path = os.getcwd()
        if 'install_python_for_android' in os.listdir('bin'):
            os.unlink('bin/install_python_for_android')
        target_install_python_for_android = os.path.join('bin','install_python_for_android')
        open(target_install_python_for_android,'w').write('#/bin/bash\nAPIS=%s\n' %(apis)+open(install_python_for_android).read())
        commands.getoutput('chmod +x %s' %target_install_python_for_android)

    def install(self):
        self.logger.info("Setting up %s install_python_for_android" % install_python_for_android_type)
        self._update()
        commands.getoutput('./bin/install_python_for_android')
        return ['bin/install_python_for_android']

    def update(self):
        command = self.options.get('update-command')
        self._update()
        if command is not None:
            self.logger.info("Running %s" % command)

