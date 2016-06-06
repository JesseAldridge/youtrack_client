#!/usr/bin/python
import os, subprocess, shutil, glob

script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.expanduser('~')
proj_name = 'youtrack_tracker'
plist_filename = 'com.jca.{}.plist'.format(proj_name)
plist_path = os.path.expanduser(os.path.join('~/Library/LaunchAgents/', plist_filename))

with open('template.plist') as f:
    template_str = f.read()
out_str = template_str.format(**locals())
with open(plist_filename, 'w') as f:
    f.write(out_str)

if os.path.exists(plist_path):
    os.remove(plist_path)
shutil.copy(plist_filename, plist_path)
subprocess.Popen(['launchctl', 'unload', plist_path], stderr=subprocess.PIPE)
subprocess.call(['launchctl', 'load', plist_path])
