import subprocess
from git_release import errors, git_helpers

def _parse_tag(tag):
    major, minor =  tag.split('.')
    return int(major), int(minor)

def _increment_tag(tag, release_type):
    major, minor = _parse_tag(tag)
    if release_type == 'major':
        new_major = major + 1
        new_minor = 0
    else:
        new_major = major
        new_minor = minor + 1

    return '{}.{}'.format(new_major, new_minor)

def release(release_type, signed):
    if not git_helpers.is_master():
        raise errors.NotMasterException("Current branch is not master.\nAborting.")

    tag = git_helpers.get_current_tag()
    if not tag:
        raise errors.NoTagException("Unable to get current tag.\nAborting.")

    new_tag = _increment_tag(tag, release_type)

    git_helpers.tag(signed, new_tag)
    print("Successfully tagged with version: {}".format(new_tag))
    print('Run "git push origin {}" to finish releasing your new tag.'.format(new_tag))
