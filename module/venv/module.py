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
# run CK virtual env


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

    # Get environment info
    r = ck.access({'action': 'load',
                   'module_uoa': work['self_module_uoa'],
                  'data_uoa': duoa})
    if r['return'] > 0:
        return r

    d=r['dict']

    path_to_activate_all = os.path.join(r['path'], d['ck_activate_all'])

    # Run shell
    s = 'bash --init-file "' + path_to_activate_all + '"'

    ck.out(line)
    ck.out(s)
    ck.out('')

    os.system(s)

    return {'return': 0}

##############################################################################
# prepare CK virtual env


def prepare(i):
    """
    Input:  {
              data_uoa - virtual environment name
              (force_detect) - if 'yes' force to detect installed python again
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o = i.get('out', '')

    duoa = i.get('data_uoa', '')

    if duoa == '':
        return {'return': 1, 'error': 'virtual alias is not defined'}

    fd = i.get('force_detect', '') == 'yes'

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
    path_to_orig_python_env = os.path.join(r['path'], 'env.sh')

    python_bin = d.get('env', {}).get('CK_ENV_COMPILER_PYTHON_FILE', '')
    if python_bin == '':
        return {'return': 1, 'error': 'python binary file is not found - please contact developers'}

    ck_repos = 'ck-repos'
    ck_tools = 'ck-tools'
    ck_activate = os.path.join('bin', 'activate')

    ck_activate_all = 'env.sh'

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
    path_ck_activate_all = os.path.join(p, ck_activate_all)

    # Create virtual env (load python env to set up env)
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
    script = """#! /bin/bash
# CK generated script

export CK_REPOS=$<ck_repos>$
export CK_TOOLS=$<ck_tools>$

# May need some shared libs from the original python
source $<path_to_orig_python_env>$

source $<venv>$
"""

    script = script.replace('$<ck_repos>$', path_ck_repos)
    script = script.replace('$<ck_tools>$', path_ck_tools)
    script = script.replace('$<path_to_orig_python_env>$', path_to_orig_python_env)
    script = script.replace('$<venv>$', path_ck_activate)

    r = ck.save_text_file({'text_file': path_ck_activate_all,
                           'string': script})
    if r['return'] > 0:
        return r

    s = 'bash -c "chmod 755 '+path_ck_activate_all+'"'
    r = os.system(s)
    if r > 0:
        return {'return': 1, 'error': 'last command failed'}

    ck.out(line)
    ck.out('Virtual environment is ready in '+p)
    ck.out('')
    ck.out('Start it with "ck run venv:'+duoa+'"')

    return {'return': 0}
