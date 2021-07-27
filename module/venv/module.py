#
# Collective Knowledge (CK python virtual environment)
#
# Developer:
#  * Grigori Fursin <grigori@octoml.ai>

cfg = {}  # Will be updated by CK (meta description of this module)
work = {}  # Will be updated by CK (temporal data)
ck = None  # Will be updated by CK (initialized CK kernel)

# Local settings
line = '======================================================================='

ck_repos = 'CK'
ck_tools = 'CK-TOOLS'
ck_template_script = 'script'

##############################################################################
# Initialize module


def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return': 0}

##############################################################################
# activate CK virtual env

def a(i):
    """
    Input:  {
              data_uoa - virtual environment name
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return activate(i)

##############################################################################
# activate CK virtual env

def activate(i):
    """
    Input:  {
              data_uoa - virtual environment name
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    duoa = i.get('data_uoa', '')

    if duoa == '':
        return {'return': 1, 'error': 'virtual alias is not defined'}

    # Check if Windows host
    win = os.name == 'nt'

    # Get environment info
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uoa'],
                  'data_uoa': duoa})
    if r['return'] > 0:
        return r

    d = r['dict']
    p = r['path']

    path_to_activate_all = os.path.join(p, d['ck_activate_all'])
    path_to_repos = os.path.join(p, d['ck_repos'])
    path_to_tools = os.path.join(p, d['ck_tools'])

    # Run shell
    if win:
        s = 'call "' + path_to_activate_all + '" && cmd'
    else:
        s = 'bash --init-file "' + path_to_activate_all + '"'

    ck.out(line)
    ck.out('Command: '+s)
    ck.out('')

    e=('%','%') if win else ('$','')

    ck.out('Path to this virtual environment:  ' + p)
    ck.out('Path to CK repos inside this venv: ' + path_to_repos)
    ck.out('Path to CK tools inside this venv: ' + path_to_tools)
    ck.out('')
    ck.out('Use "cd '+e[0]+'CK_VENV'+e[1]+'" to jump to the venv home directory')
    ck.out('')

    os.system(s)

    return {'return': 0}

##############################################################################
# prepare CK virtual env
def create(i):
    """
    Input:  {
              data_uoa - virtual environment name
              (force_detect) - if 'yes' force to detect installed python again

              (template) - if !='', use scripts from this venv.template entry 
                           at the end of venv creation

              (quiet) - if 'yes', select the first found python and continue
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return prepare(i)

def prepare(i):
    """
    Input:  {
              data_uoa - virtual environment name
              (force_detect) - if 'yes' force to detect installed python again

              (template) - if !='', use scripts from this venv.template entry 
                           at the end of venv creation

              (quiet) - if 'yes', select the first found python and continue
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o = i.get('out', '')

    quiet = i.get('quiet', '')

    duoa = i.get('data_uoa', '')

    if duoa == '':
        return {'return': 1, 'error': 'virtual alias is not defined'}

    fd = i.get('force_detect', '') == 'yes'

    # Check if Windows host
    win = os.name == 'nt'

    # Check template
    template = i.get('template','')
    template_path = ''
    if template != '':
        r = ck.access({'action':'load',
                       'module_uoa':'venv.template',
                       'data_uoa':template})
        if r['return'] > 0:
            return r

        template_path = os.path.join(r['path'], ck_template_script)
        if win:
            template_path += '.bat'
        else:
            template_path += '.sh'

        if not os.path.isfile(template_path):
            return {'return':1, 'error':'template script not found ('+template_path+')'}

    # Search for existing python versions
    request = {'action': 'search',
               'module_uoa': 'env',
               'tags': 'compiler,python',
               'add_meta': 'yes'}

    # First check if python env is detected
    r = ck.access(request)
    if r['return'] > 0:
        return r

    lst = r['lst']

    # If no, attempt to detect
    if fd or len(lst) == 0:
        ck.out(line)
        ck.out('Detecting installed python(s) on your system...')
        ck.out('')

        ii = {'action': 'detect',
              'module_uoa': 'soft',
              'data_uoa': 'compiler.python'}
        if quiet != '':
            ii['quiet'] = quiet
        if o == 'con':
            ii['out'] = 'con'

        r = ck.access(ii)
        if r['return'] > 0:
            return r

        # Check again if python env is detected
        r = ck.access(request)
        if r['return'] > 0:
            return r

        lst = r['lst']

    # Check which ones
    ck.out(line)
    ck.out('You have the following python version(s) registered that you can use for virtual env:')
    ck.out('')

    j = 0
    for l in lst:
        x = l['meta']
        ver = x.get('customize', {}).get('version', '')

        ck.out(str(j)+') '+ver)
        j += 1

    ck.out('')
    if quiet == 'yes':
        x = '0'
    else:
        x = input('Select the version (Press Enter to select 0 and enter -1 to build a specific version you require): ')
        x = x.strip()
        if x == '':
            x = '0'

    y = int(x)

    if y == -1:
        ck.out(line)
        ck.out('Building new python:')
        ck.out('')

        ii = {'action': 'install',
              'module_uoa': 'package',
              'tags': 'compiler,python,source'}
        if o == 'con':
            ii['out'] = 'con'

        r = ck.access(ii)
        if r['return'] > 0:
            return r

        env_uoa = r['env_data_uoa']
    elif y < 0 or y >= j:
        return {'return': 1, 'error': 'selection is not recognized'}
    else:
        env_uoa = lst[y]['data_uoa']

    # Get environment info
    r = ck.access({'action': 'load',
                   'module_uoa': 'env',
                  'data_uoa': env_uoa})
    if r['return'] > 0:
        return r

    d = r['dict']

    # Prepare some paths inside venv
    ck_activate_all = 'env.sh' if not win else 'env.bat'

    path_to_orig_python_env = os.path.join(r['path'], ck_activate_all)

    python_bin = d.get('env', {}).get('CK_ENV_COMPILER_PYTHON_FILE', '')
    if python_bin == '':
        return {'return': 1, 'error': 'python binary file is not found - please contact developers'}

    if win:
        ck_activate = os.path.join('Scripts', 'activate.bat')
        ck_new_python = os.path.join('Scripts', 'python.exe')
    else:
        ck_activate = os.path.join('bin', 'activate')
        ck_new_python = os.path.join('bin','python')

    # Add or reuse CK venv entry
    r = ck.access({'action': 'find',
                   'module_uoa': work['self_module_uoa'],
                   'data_uoa': duoa})
    if r['return'] == 0:
        ck.out(line)
        x = input(
            'It seems that virtual environment "' + duoa + '" already exists. Would you like to remove and reinstall it (y/N): ')
        x = x.strip().lower()

        if x == '' or x == 'n':
            return {'return': 0}

        # Delete entry
        r = ck.access({'action': 'rm',
                       'module_uoa': work['self_module_uoa'],
                       'data_uoa': duoa,
                       'force': 'yes'})
        if r['return'] > 0:
            return r

    # Add venv entry
    dd = {'python_bin': python_bin,
          'python_env_uoa': env_uoa,
          'path_to_orig_python_env': path_to_orig_python_env,
          'ck_repos': ck_repos,
          'ck_tools': ck_tools,
          'ck_activate': ck_activate,
          'ck_new_python': ck_new_python,
          'ck_activate_all': ck_activate_all}

    r = ck.access({'action': 'add',
                   'module_uoa': work['self_module_uoa'],
                   'data_uoa': duoa,
                   'dict': dd})
    if r['return'] > 0:
        return r
    p = os.path.join(r['path'])

    path_ck_repos = os.path.join(p, ck_repos)
    path_ck_tools = os.path.join(p, ck_tools)
    path_ck_activate = os.path.join(p, ck_activate)
    path_ck_new_python = os.path.join(p, ck_new_python)
    path_ck_activate_all = os.path.join(p, ck_activate_all)

    # Create virtual env (load python env to set up env)
    if win:
        s = 'call '+path_to_orig_python_env + ' && virtualenv --python=' + python_bin + ' "' + p + '"'
    else:
        s = 'chmod 755 ' + path_to_orig_python_env + ' ; bash -c "source '+path_to_orig_python_env + \
            ' ; virtualenv --python=' + python_bin + ' ' + p + '"'

    ck.out(line)
    ck.out('Python binary used to set up virtual env: '+python_bin)
    ck.out('Path to the virtual env: '+p)

    ck.out('')
    ck.out('Creating virtual env:')
    ck.out(s)

    ck.out('')
    r = os.system(s)
    if r > 0:
        return {'return': 1, 'error': 'last command failed'}

    # Record environment file with extra vars
    if win:
        script = """@echo off
rem CK generated script

set CK_REPOS=$<ck_repos>$
set CK_TOOLS=$<ck_tools>$
set CK_VENV_PYTHON_BIN=$<ck_vpython_bin>$
set CK_VENV=$<ck_venv>$

rem May need some shared libs from the original python
call $<path_to_orig_python_env>$

rem Allow CK to detect a new compiler in venv
set CK_ENV_COMPILER_PYTHON_SET=0

call $<venv>$
"""
    else:
        script = """#! /bin/bash
# CK generated script

export CK_REPOS=$<ck_repos>$
export CK_TOOLS=$<ck_tools>$
export CK_VENV_PYTHON_BIN=$<ck_vpython_bin>$
export CK_VENV=$<ck_venv>$

# May need some shared libs from the original python
source $<path_to_orig_python_env>$

# Allow CK to detect a new compiler in venv
export CK_ENV_COMPILER_PYTHON_SET=0

source $<venv>$
"""

    script = script.replace('$<ck_repos>$', path_ck_repos)
    script = script.replace('$<ck_tools>$', path_ck_tools)
    script = script.replace('$<path_to_orig_python_env>$', path_to_orig_python_env)
    script = script.replace('$<ck_vpython_bin>$', path_ck_new_python)
    script = script.replace('$<ck_venv>$', p)
    script = script.replace('$<venv>$', path_ck_activate)

    r = ck.save_text_file({'text_file': path_ck_activate_all,
                           'string': script})
    if r['return'] > 0:
        return r

    if not win:
        s = 'bash -c "chmod 755 '+path_ck_activate_all+'"'
        r = os.system(s)
        if r > 0:
            return {'return': 1, 'error': 'last command failed'}


# Grigori: I first thought to add local CK installation with --no-cache-dir
# to avoid rare strange effects with ck-python.cfg that is cached in a wheel
# and can point to a wrong python.

# However, it's very rare and in fact, we do not need to install CK inside
# virtual environment at all - we can reuse the one from the original installation!

# In such, case creating virtualenv is much faster!

#    ck.out(line)
#    ck.out('Installing CK ...')
#    ck.out('')
#
#    if win:
#        s = 'call "' + path_ck_activate_all + '" && pip install ck --no-cache-dir'
#    else:
#        s = 'bash -c "source '+path_ck_activate_all + ' ; pip install ck --no-cache-dir" '
#    ck.out('')
#    r = os.system(s)
#    if r > 0:
#        return {'return': 1, 'error': 'last command failed'}


# It's can't work at this moment because we don't have OS/platform components
    # Register python from virtual environment
#    ck.out(line)
#    ck.out('Register new python from the virtual environment ...')
#    ck.out('')
#
#    if win:
#        s = 'call "' + path_ck_activate_all + '" && ck detect soft:compiler.python --full_path="'+path_ck_new_python+'"'
#    else:
#        s = 'bash -c "source '+path_ck_activate_all + ' ; ck detect soft:compiler.python --full_path=\\"'+path_ck_new_python+'\\""'
#    ck.out(s)
#    ck.out('')
#    r = os.system(s)
#    if r > 0:
#        return {'return': 1, 'error': 'last command failed'}

    # If template, runs the script at the end:
    if template_path != '':
        ck.out(line)
        ck.out('Run script ('+template_path+') from template ('+template+') ...')
        ck.out('')

        if win:
            s = 'call "' + path_ck_activate_all + '" && call '+template_path
        else:
            s = 'bash -c "source '+path_ck_activate_all + ' ; source '+template_path+'"'
        ck.out(s)
        ck.out('')
        r = os.system(s)
        if r > 0:
            return {'return': 1, 'error': 'last command failed'}

    # Configure CK Register python from virtual environment
    ck.out(line)
    ck.out('Configure CK to install new packages to CK env entries with tags for easy search ...')
    ck.out('')

    if win:
        s = 'call "' + path_ck_activate_all + '" && ck setup kernel --var.install_to_env=yes'
    else:
        s = 'bash -c "source '+path_ck_activate_all + ' ; ck setup kernel --var.install_to_env=yes"'
    ck.out(s)
    ck.out('')
    r = os.system(s)
    if r > 0:
        return {'return': 1, 'error': 'last command failed'}

    ck.out(line)
    ck.out('Virtual environment is ready in '+p)
    ck.out('')
    ck.out('Start it with "ck activate venv:'+duoa+'"')

    return {'return': 0}

