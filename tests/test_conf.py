__copyright__ = "Copyright (c) 2024 Alex Laird"
__license__ = "MIT"

import os
import shutil
from unittest import TestCase

from amazonorders import conf
from amazonorders.conf import AmazonOrdersConfig


class TestConf(TestCase):
    def setUp(self):
        conf.DEFAULT_CONFIG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".config")
        self.test_output_dir = os.path.join(conf.DEFAULT_CONFIG_DIR, "output")
        self.test_cookie_jar_path = os.path.join(conf.DEFAULT_CONFIG_DIR, "cookies.json")

    def tearDown(self):
        if os.path.exists(conf.DEFAULT_CONFIG_DIR):
            shutil.rmtree(conf.DEFAULT_CONFIG_DIR)

    def test_provision_config(self):
        # WHEN
        config_path = os.path.join(conf.DEFAULT_CONFIG_DIR, "config.yml")
        self.assertFalse(os.path.exists(conf.DEFAULT_CONFIG_DIR))
        self.assertFalse(os.path.exists(config_path))
        self.assertFalse(os.path.exists(self.test_output_dir))
        self.assertFalse(os.path.exists(self.test_cookie_jar_path))

        # GIVEN
        config = AmazonOrdersConfig(data={
            "output_dir": self.test_output_dir,
            "cookie_jar_path": self.test_cookie_jar_path
        })

        # THEN
        self.assertEqual(config_path, config.config_path)
        self.assertTrue(os.path.exists(conf.DEFAULT_CONFIG_DIR))
        self.assertFalse(os.path.exists(config_path))
        self.assertTrue(os.path.exists(self.test_output_dir))
        self.assertEqual("en-US", config.locale)
        self.assertEqual(10, config.max_auth_attempts)
        self.assertEqual(self.test_output_dir, config.output_dir)
        self.assertEqual(self.test_cookie_jar_path, config.cookie_jar_path)

        # GIVEN
        config.save()

        # THEN
        self.assertTrue(os.path.exists(config_path))
        with open(config.config_path, "r") as f:
            self.assertEqual("""cookie_jar_path: {}
locale: en-US
max_auth_attempts: 10
output_dir: {}
""".format(self.test_cookie_jar_path, self.test_output_dir), f.read())

    def test_override_default(self):
        # GIVEN
        config = AmazonOrdersConfig(data={
            "max_auth_attempts": 11
        })

        self.assertEqual(11, config.max_auth_attempts)

    def test_load_from_file(self):
        # GIVEN
        config_path = os.path.join(conf.DEFAULT_CONFIG_DIR, "load-from-config.yml")
        test_output_dir = os.path.join(conf.DEFAULT_CONFIG_DIR, "load-from-config-output")
        test_cookie_jar_path = os.path.join(conf.DEFAULT_CONFIG_DIR, "load-from-config-cookies.json")
        os.makedirs(conf.DEFAULT_CONFIG_DIR)
        with open(config_path, "w") as f:
            f.write("""cookie_jar_path: {}
locale: some-locale
max_auth_attempts: 11
output_dir: {}
""".format(test_cookie_jar_path, test_output_dir))

        # WHEN
        config = AmazonOrdersConfig(config_path=config_path)

        self.assertEqual(config_path, config.config_path)
        self.assertEqual("some-locale", config.locale)
        self.assertEqual(11, config.max_auth_attempts)
        self.assertEqual(test_output_dir, config.output_dir)
        self.assertEqual(test_cookie_jar_path, config.cookie_jar_path)

    def test_update_config(self):
        # GIVEN
        config = AmazonOrdersConfig(data={
            "max_auth_attempts": 11
        })

        self.assertEqual(11, config.max_auth_attempts)

        # WHEN
        config.update_config("max_auth_attempts", 7)

        # THEN
        self.assertEqual(7, config.max_auth_attempts)
