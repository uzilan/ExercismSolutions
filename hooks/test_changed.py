#!/usr/bin/env python

import os
import sys
import hook_utils as hut


def main(commit=-1, *args, **kwargs):
    if commit == 'HEAD':
        commit = 0
    else:
        commit = int(commit)
    changed_exercises = hut.get_changed_exercises(commit)
    changed_tracks = set(track for track, _ in changed_exercises)
    for track in changed_tracks:
        hut.log('Running linter...', track)
        results, ret = hut.linter(track)
        if results.startswith('No available'):
            hut.log(results, track)
        elif ret == 0:
            hut.log('Style checks passed', track)
        else:
            hut.abort(results, track)
    simple_tracks = {'cpp', 'csharp', 'go', 'haskell', 'java', 'ruby'}
    for track, exercise in sorted(changed_exercises):
        dir = os.path.join(track, exercise)
        if not os.path.isdir(dir):
            continue
        label = '{}/{}'.format(track, exercise)
        hut.log('Running tests...', label)
        os.chdir(dir)
        if track == 'python':
            results, ret = hut.runner(track, exercise)
            if ret == 0:
                hut.log(('All tests were collected and passed '
                         'successfully'), label)
            elif ret == 5:
                hut.log('No tests were collected', label)
            elif ret == 1:
                print(results)
                hut.abort(('Tests were collected and run but some of '
                           'the tests failed'), label)
            elif ret == 2:
                hut.abort('Test execution was interrupted by the user', label)
            elif ret == 3:
                hut.abort(('Internal error happened while executing '
                           'tests'), label)
            elif ret == 4:
                hut.abort('pytest command line usage error', label)
        elif track in simple_tracks:
            results, ret = hut.runner(track, exercise)
            if results is None:
                hut.log('Test runner not yet implemented; skipping', label)
            else:
                if ret == 0:
                    hut.log(('All tests passed successfully'), label)
                else:
                    print(results)
                    hut.abort('Some of the tests failed', label)
        else:
            hut.abort('Unknown track "{}"'.format(track))
        os.chdir(os.path.join('..', '..'))
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
