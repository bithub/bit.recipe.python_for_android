import logging
import os
import shutil
import pkg_resources
import commands

class Recipe:
    def __init__(self, buildout, name, options):
        self.name = name
        self.options = options
        self.logger = logging.getLogger(name)

    def _update(self):
        install = pkg_resources.resource_filename(__name__, 'python_for_android')
        path = os.getcwd()
        target_install = os.path.join('bin',self.name)
        sdk = os.path.join(path,self.options['sdk'])
        ndk = os.path.join(path, self.options['ndk'])
        api = self.options['api']
        ndk_version = self.options['ndk_version']
        if self.name in os.listdir('bin'):
            os.unlink(target_install)

        open(target_install,'w').write('#/bin/bash\nexport ANDROIDSDK=%s\nexport ANDROIDNDK=%s\nexport ANDROIDNDKVER=%s\nexport ANDROIDAPI=%s\nexport PATH=$ANDROIDSDK/tools:$ANDROIDNDK:$PATH\nGIT_SRC="%s"\nRECIPES="%s"\nPROJECT=%s' %(sdk,ndk,ndk_version,api,self.options['src'],self.options['recipes'],self.name)+open(install).read())
        commands.getoutput('chmod +x %s' %target_install)        
            
    def install(self):
        self._update()
        return ['bin/%s'%self.name]

    def update(self):
        self._update()

