import re

from osgtest.library import core, osgunittest

class TestMisc(osgunittest.OSGTestCase):

    def test_01_web100clt(self):
        core.skip_ok_unless_installed('ndt-client')

        command = ('web100clt', '-v')
        stdout = core.check_system(command, 'NDT client')[0]
        self.assert_(re.search('ndt.+version', stdout, re.IGNORECASE)
                     is not None)

    def test_02_osg_version(self):
        core.skip_ok_unless_installed('osg-version')

        command = ('osg-version',)

        # First we verify that osg-version runs
        stdout = core.check_system(command, 'osg-version')[0]

        # Then we pull out the version number from the output
        version_pattern = re.compile(r'(\d+\.\d+\.\d+)')
        matches = version_pattern.search(stdout)

        # Is there a version number?
        self.assert_(matches is not None)
        osg_version = matches.group(1)

        # Get the version number from the RPM
        command = ('rpm', '-q', 'osg-version')
        stdout = core.check_system(command, "osg-version RPM version")[0]
        matches = version_pattern.search(stdout)
        self.assert_(matches is not None)

        # Verify that the versions match
        osg_version_rpm_version = matches.group(1)
        self.assert_(osg_version == osg_version_rpm_version)

