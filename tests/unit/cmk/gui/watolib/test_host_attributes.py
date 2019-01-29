# Triggers plugin loading of plugins.wato which registers all the plugins
import cmk.gui.wato  # pylint: disable=unused-import
import cmk.gui.watolib.host_attributes as attrs

expected_attributes = {
    'additional_ipv4addresses': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': ['ip-v4'],
        'editable': True,
        'from_config': False,
        'show_in_folder': False,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': u'Address'
    },
    'additional_ipv6addresses': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': ['ip-v6'],
        'editable': True,
        'from_config': False,
        'show_in_folder': False,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': u'Address'
    },
    'alias': {
        'class_name': 'NagiosTextAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': False,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': True,
        'show_inherited_value': True,
        'topic': None
    },
    'contactgroups': {
        'class_name': 'ContactGroupsAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': None
    },
    'ipaddress': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': ['ip-v4'],
        'editable': True,
        'from_config': False,
        'show_in_folder': False,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': True,
        'show_inherited_value': True,
        'topic': u'Address'
    },
    'ipv6address': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': ['ip-v6'],
        'editable': True,
        'from_config': False,
        'show_in_folder': False,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': True,
        'show_inherited_value': True,
        'topic': u'Address'
    },
    'locked_attributes': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': False,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': False,
        'show_in_table': False,
        'show_inherited_value': False,
        'topic': None
    },
    'locked_by': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': False,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': False,
        'topic': None
    },
    'management_address': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': False,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': u'Management Board'
    },
    'management_ipmi_credentials': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': u'Management Board'
    },
    'management_protocol': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': u'Management Board'
    },
    'management_snmp_community': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': u'Management Board'
    },
    'network_scan': {
        'class_name': 'NetworkScanAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': False,
        'show_in_host_search': False,
        'show_in_table': False,
        'show_inherited_value': False,
        'topic': u'Network Scan'
    },
    'network_scan_result': {
        'class_name': 'NetworkScanResultAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': False,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': False,
        'show_in_host_search': False,
        'show_in_table': False,
        'show_inherited_value': False,
        'topic': u'Network Scan'
    },
    'parents': {
        'class_name': 'ParentsAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': True,
        'show_inherited_value': True,
        'topic': None
    },
    'site': {
        'class_name': 'SiteAttribute',
        'depends_on_roles': [],
        'depends_on_tags': [],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': True,
        'show_inherited_value': True,
        'topic': None
    },
    'snmp_community': {
        'class_name': 'ValueSpecAttribute',
        'depends_on_roles': [],
        'depends_on_tags': ['snmp'],
        'editable': True,
        'from_config': False,
        'show_in_folder': True,
        'show_in_form': True,
        'show_in_host_search': True,
        'show_in_table': False,
        'show_inherited_value': True,
        'topic': None
    },
}


def test_registered_host_attributes():
    #xx = {}
    #for ident, cls in attrs._host_attribute.items():
    #    topic = [e[1] for e in attrs._host_attributes if e[0] == cls]
    #    topic = topic[0] if topic else None

    #    xx[ident] = {
    #        "class_name": cls.__class__.__name__,
    #        "topic": topic,
    #        "show_in_table": cls._show_in_table,
    #        "show_in_folder": cls._show_in_folder,
    #        "show_in_host_search": cls._show_in_host_search,
    #        "show_in_form": cls._show_in_form,
    #        "show_inherited_value": cls._show_inherited_value,
    #        "depends_on_tags": cls._depends_on_tags,
    #        "depends_on_roles": cls._depends_on_roles,
    #        "editable": cls._editable,
    #        "from_config": cls._from_config,
    #    }

    #import pprint
    #x = pprint.pformat(xx)
    #open("/tmp/x", "w").write(x)

    names = attrs._host_attribute.keys()
    assert sorted(expected_attributes.keys()) == sorted(names)

    for ident, attr in attrs._host_attribute.items():
        #rulespec = rulespec_class()
        spec = expected_attributes[ident]

        assert attr.__class__.__name__ == spec["class_name"]

        topic = [e[1] for e in attrs._host_attributes if e[0] == attr]
        topic = topic[0] if topic else None
        assert topic == spec["topic"]

        assert spec["show_in_table"] == attr._show_in_table
        assert spec["show_in_folder"] == attr._show_in_folder
        assert spec["show_in_host_search"] == attr._show_in_host_search
        assert spec["show_in_form"] == attr._show_in_form
        assert spec["show_inherited_value"] == attr._show_inherited_value
        assert spec["depends_on_tags"] == attr._depends_on_tags
        assert spec["depends_on_roles"] == attr._depends_on_roles
        assert spec["editable"] == attr._editable
        assert spec["from_config"] == attr._from_config


def test_legacy_register_rulegroup_with_defaults(monkeypatch):
    monkeypatch.setattr(attrs, "_host_attributes", [])
    monkeypatch.setattr(attrs, "_host_attribute", {})
    #monkeypatch.setattr(cmk.gui.watolib.rulespecs, "rulespec_group_registry",
    #                    RulespecGroupRegistry())

    assert "lat" not in attrs._host_attribute

    cmk.gui.wato.declare_host_attribute(
        cmk.gui.wato.NagiosTextAttribute(
            "lat",
            "_LAT",
            "Latitude",
            "Latitude",
        ),)

    attr = attrs._host_attribute["lat"]
    assert isinstance(attr, cmk.gui.wato.NagiosTextAttribute)
    assert attr.show_in_table() is True
    assert attr.show_in_folder() is True
    assert attr.show_in_host_search() is True
    assert attr.show_in_form() is True

    topic = [e[1] for e in attrs._host_attributes if e[0] == attr]
    topic = topic[0] if topic else None
    assert topic is None

    assert attr.depends_on_tags() == []
    assert attr.depends_on_roles() == []
    assert attr.editable() is True
    assert attr.show_inherited_value() is True
    assert attr.may_edit() is True
    assert attr.from_config() is False


def test_legacy_register_rulegroup_without_defaults(monkeypatch):
    monkeypatch.setattr(attrs, "_host_attributes", [])
    monkeypatch.setattr(attrs, "_host_attribute", {})
    #monkeypatch.setattr(cmk.gui.watolib.rulespecs, "rulespec_group_registry",
    #                    RulespecGroupRegistry())

    assert "lat" not in attrs._host_attribute

    cmk.gui.wato.declare_host_attribute(
        cmk.gui.wato.NagiosTextAttribute(
            "lat",
            "_LAT",
            "Latitude",
            "Latitude",
        ),
        show_in_table=False,
        show_in_folder=False,
        show_in_host_search=False,
        topic="xyz",
        show_in_form=False,
        depends_on_tags=["xxx"],
        depends_on_roles=["guest"],
        editable=False,
        show_inherited_value=False,
        may_edit=lambda: False,
        from_config=True,
    )

    attr = attrs._host_attribute["lat"]
    assert isinstance(attr, cmk.gui.wato.NagiosTextAttribute)
    assert attr.show_in_table() is False
    assert attr.show_in_folder() is False
    assert attr.show_in_host_search() is False
    assert attr.show_in_form() is False

    topic = [e[1] for e in attrs._host_attributes if e[0] == attr]
    topic = topic[0] if topic else None
    assert topic == "xyz"

    assert attr.depends_on_tags() == ["xxx"]
    assert attr.depends_on_roles() == ["guest"]
    assert attr.editable() is False
    assert attr.show_inherited_value() is False
    assert attr.may_edit() is False
    assert attr.from_config() is True


def test_get_sorted_host_attribute_topics():
    assert attrs.get_sorted_host_attribute_topics("host") == [
        (None, u'Basic settings'),
        (u'Address', u'Address'),
        (u'Data sources', u'Data sources'),
        (u'Host tags', u'Host tags'),
        (u'Management Board', u'Management Board'),
    ]


def test_get_sorted_host_attributes_by_topic():
    assert [a.name() for a in attrs.get_sorted_host_attributes_by_topic(None)] == [
        'contactgroups',
        'alias',
        'snmp_community',
        'parents',
        'site',
        'locked_by',
        'locked_attributes',
    ]