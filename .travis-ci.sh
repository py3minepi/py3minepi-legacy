#!/bin/bash
# Based on a test script from avsm/ocaml repo https://github.com/avsm/ocaml

CHROOT_DIR=/tmp/arm-chroot

CHROOT_TARBALL_URL="https://s3.amazonaws.com/py3minepi-arm-chroot/py3minepi/arm-chroot/8/8.1/tmp/arm-chroot.tar.bz2"
CHROOT_TARBALL="/tmp/$(basename $CHROOT_TARBALL_URL)"

# Debian package dependencies for the host
HOST_DEPENDENCIES="debootstrap qemu-user-static binfmt-support sbuild"

# Debian package dependencies for the chrooted environment
GUEST_DEPENDENCIES="sudo python2.7 python3 python-pip python3-pip git"

# Command used to run the tests

function setup_arm_chroot {

	curl --silent --output ${CHROOT_TARBALL} ${CHROOT_TARBALL_URL}
	sudo tar -C / -jxf ${CHROOT_TARBALL}
	sudo mount -o bind /dev ${CHROOT_DIR}/dev
	sudo mount -t proc none ${CHROOT_DIR}/proc
	sudo mount -o bind /sys ${CHROOT_DIR}/sys
	sudo mount -o bind /tmp ${CHROOT_DIR}/tmp

    # Create file with environment variables which will be used inside chrooted
    # environment
    echo "export ARCH=${ARCH}" > envvars.sh
    echo "export TOXENV=${TOXENV}" > envvars.sh
    echo "export TRAVIS_BUILD_DIR=${TRAVIS_BUILD_DIR}" >> envvars.sh
    chmod a+x envvars.sh

    # Install dependencies inside chroot
    sudo chroot ${CHROOT_DIR} apt-get update
    sudo chroot ${CHROOT_DIR} apt-get --allow-unauthenticated install \
        -qq -y ${GUEST_DEPENDENCIES}

    # Create build dir and copy travis build files to our chroot environment
    sudo mkdir -p ${CHROOT_DIR}/${TRAVIS_BUILD_DIR}
    sudo rsync -av ${TRAVIS_BUILD_DIR}/ ${CHROOT_DIR}/${TRAVIS_BUILD_DIR}/

    # Indicate chroot environment has been set up
    sudo touch ${CHROOT_DIR}/.chroot_is_done

    # Call ourselves again which will cause tests to run
    sudo chroot ${CHROOT_DIR} bash -c "cd ${TRAVIS_BUILD_DIR} && ./.travis-ci.sh"
}

function run_tests {
    if [ -f "./envvars.sh" ]; then
        . ./envvars.sh
    fi

    echo "--- Running tests"
    echo "--- Environment: $(uname -a)"
    echo "--- Working directory: $(pwd)"
    ls -la

    sudo pip install tox
    tox
}

if [ "${ARCH}" = "arm" ]; then
  if [ -e "/.chroot_is_done" ]; then
    echo "--- Running inside chrooted environment"

    run_tests
  else
    echo "--- Setting up chrooted ARM environment"
    setup_arm_chroot
  fi
else
  sudo apt-get update
  sudo apt-get install -qq -y python-pip # Because we might not be running in a Pythonic environment

  run_tests
fi
