##
# Flamedisx colab setup
##
import sys
if 'google.colab' in sys.modules:
    %tensorflow_version 2.x
    try:
        import flamedisx
    except ImportError:
        branch = "master" if len(sys.argv) < 2 else sys.argv[1]
        print(f"Cloning Flamedisx and checking out branch {branch}")

        !git clone https://github.com/FlamTeam/flamedisx.git
        %cd flamedisx
        !git checkout $branch
        !git pull origin $branch
        !python setup.py develop
        %cd ..

import flamedisx as fd
if not hasattr(fd, 'ERSource'):
    print("\n\n>>Flamedisx is not yet installed. Restart the runtime<<!")
else:
    print("Flamedisx is installed :-)")
