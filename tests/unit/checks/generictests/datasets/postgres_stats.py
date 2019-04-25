# yapf: disable


checkname = 'postgres_stats'


mock_item_state = {
    '': 1547250000.0,
}


freeze_time = '2019-01-12 00:00:00'


info = [[u'[databases_start]'],
        [u'postgres'],
        [u'adwebconnect'],
        [u'[databases_end]'],
        [u'datname', u'sname', u'tname', u'vtime', u'atime'],
        [u'postgres', u'pg_catalog', u'pg_statistic', u'-1', u'-1'],
        [u'adwebconnect', u'public', u'serveraktion', u'1488881726', u'1488881726'],
        [u'adwebconnect', u'pg_catalog', u'pg_statistic', u'1488882719', u'-1'],
        [u'adwebconnect', u'public', u'auftrag', u'1489001316', u'1489001316'],
        [u'adwebconnect', u'public', u'anrede', u'-1', u'-1'],
        [u'adwebconnect', u'public', u'auftrag_mediadaten', u'-1', u'']]


discovery = {'': [(u'ANALYZE adwebconnect', {}),
                  (u'ANALYZE postgres', {}),
                  (u'VACUUM adwebconnect', {}),
                  (u'VACUUM postgres', {})]}


checks = {
    '': [
        (u'ANALYZE adwebconnect', {'never_analyze_vacuum': (1000, 1100)}, [
            (0, u'Table: auftrag', []),
            (0, 'Time since last vacuum: 674 d', []),
            (2, u'2 tables were never analyzed: anrede/auftrag_mediadaten (warn/crit at 16 m/18 m)', []),
        ]),
        (u'ANALYZE adwebconnect', {}, [
            (0, u'Table: auftrag', []),
            (0, 'Time since last vacuum: 674 d', []),
            (1, u'2 tables were never analyzed: anrede/auftrag_mediadaten', []),
        ]),
        (u'ANALYZE postgres', {}, [
            (0, 'No never checked tables', []),
        ]),
        (u'VACUUM adwebconnect', {}, [
            (0, u'Table: auftrag', []),
            (0, 'Time since last vacuum: 674 d', []),
            (1, u'2 tables were never vacuumed: anrede/auftrag_mediadaten', []),
        ]),
        (u'VACUUM postgres', {}, [
            (0, 'No never checked tables', []),
        ]),
]}