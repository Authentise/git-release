import subprocess
from git_release import errors

def _get_output_or_none(args):
    try:
        return subprocess.check_output(args).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return None

def get_current_tag():
    return _get_output_or_none(['git', 'describe', '--abbrev=0'])

def is_master():
    branch = _get_output_or_none(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return branch == 'master'

def tag(signed, new_tag):
    signing_arg = '-a'
    if signed:
        signing_arg = '-s'
    exit_code = subprocess.call(['git', 'tag', signing_arg, new_tag])
    if exit_code != 0:
        raise errors.FailedToTag("git tag returned a failing exit_code")
