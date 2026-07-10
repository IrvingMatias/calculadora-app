[buildozer]
title = Calculadora Veterinaria
package.name = calculadoraveterinaria
package.domain = com.tuveterinaria
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy,kivymd,plyer,pyjnius,android

android.permissions = INTERNET
android.orientation = portrait
android.api = 30
android.minapi = 21
android.package_name = com.tuveterinaria.calculadoraveterinaria

- name: Build APK
      run: |
        yes | buildozer android debug
