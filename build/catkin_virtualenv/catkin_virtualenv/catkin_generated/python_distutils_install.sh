#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/tndrd/workspaces/kondo/src/catkin_virtualenv/catkin_virtualenv"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/tndrd/workspaces/kondo/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/tndrd/workspaces/kondo/install/lib/python3/dist-packages:/home/tndrd/workspaces/kondo/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/tndrd/workspaces/kondo/build" \
    "/usr/bin/python3" \
    "/home/tndrd/workspaces/kondo/src/catkin_virtualenv/catkin_virtualenv/setup.py" \
     \
    build --build-base "/home/tndrd/workspaces/kondo/build/catkin_virtualenv/catkin_virtualenv" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/tndrd/workspaces/kondo/install" --install-scripts="/home/tndrd/workspaces/kondo/install/bin"
