
bit.recipe.python_for_android
=============================

This package allows you to build python-based android packages from a buildout environment

You will need a copy of the android sdk and ndks for your project environments

These can be installed using bit.recipe.android_sdk and bit.recipe.android_ndk

A complete buildout example might be:

[buildout]
parts = my_android_sdk
      my_android_ndk
      my_kivy

[my_android_sdk]
recipe = bit.recipe.android_sdk
apis = 8
sdk = http://dl.google.com/android/android-sdk_r14-linux.tgz

[my_android_ndk]
recipe = bit.recipe.android_ndk
version = r7
ndk = http://dl.google.com/android/ndk/android-ndk-r7-linux-x86.tar.bz2

[my_kivy]
recipe = bit.recipe.python_for_android
package = org.bitfoundation.my_kivy
src = git@github.com:kivy/python-for-android
sdk = parts/my_android_sdk
ndk = parts/my_android_ndk
ndk_version = ${my_android_ndk:version}
api = 8
recipes = kivy
version = 0.0.1
public = var/my_kivy/public
private = var/my_kivy/private
orientation = portrait
permissions = INTERNET


This can then be installed as follows

./bin/buildout


Once you have done this you can create your distribution

./bin/my_kivy dist


You can do a clean install or pass other arguments to the distribute.sh script, ie:

./bin/my_kivy dist -f


Place your public/private resources into the folders specified ie: var/my_kivy/public, and build and install your android package

./bin/my_kivy build debug installd

