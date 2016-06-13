"""
    test_default_fixtures_dir
    ~~~~~~~~~~~~~

    A set of tests that check the default fixtures directory of Flask-Fixtures.

    :copyright: (c) 2016 Feng Yao <yaoelvon@gmail.com>.
    :license: MIT, see LICENSE for more details.
"""


from __future__ import absolute_import

import unittest

from myapp import app
from myapp.models import db, Author

from flask.ext.fixtures import FixturesMixin


class TestDefaultFixturesDir(unittest.TestCase, FixturesMixin):
    '''Test fixtures directory set problem.
    When coder set app.config['FIXTURES_DIRS'] and FIXTURES_DIRS path
    and "current_app.root_path + '/fixtures'" together have
    a same file like 'author.json', flask-fixtures will get
    "current_app.root_path + '/fixtures/author.json'" file.
    I think that default can use "current_app.root_path + '/fixtures'",
    but we shoud use app.config['FIXTURES_DIRS']
    when coder had set "app.config['FIXTURES_DIRS']".
    '''
    app = app
    db = db
    app.config['FIXTURES_DIRS'] = [app.root_path + '/../fixtures']
    fixtures = ['authors.json']

    def setUp(self):
        self.SUT_app = app
        if hasattr(app, 'app_context'):
            self.app_context = self.SUT_app.app_context()
        else:
            self.app_context = self.SUT_app.test_reqeust_context()
        self.app_context.push()
        app.logger.debug('app.root_path={0}'.format(app.config['FIXTURES_DIRS']))

    def tearDown(self):
        app.config.pop('FIXTURES_DIRS')
        self.app_context.pop()

    def test_get_authors_json_from_dir_set(self):
        author = Author.query.first()

        self.assertEqual(author.first_name, 'Feng')
        self.assertEqual(author.last_name, 'Yao')
