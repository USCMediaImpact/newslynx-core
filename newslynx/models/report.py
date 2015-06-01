from sqlalchemy.dialects.postgresql import JSON

from jinja2 import Template

from newslynx.core import db
from newslynx.lib import dates


class Report(db.Model):

    __tablename__ = 'reports'

    id = db.Column(db.Integer, unique=True, index=True, primary_key=True)
    org_id = db.Column(
        db.Integer, db.ForeignKey('orgs.id'), index=True)
    name = db.Column(db.Text, index=True)
    created = db.Column(db.DateTime(timezone=True), index=True)
    template = db.Column(db.Text)
    data = db.Column(JSON)

    def __init__(self, **kw):
        self.org_id = kw.get('org_id')
        self.name = kw.get('name')
        self.created = kw.get('created', dates.now())
        self.template = kw.get('template', None)
        self.data = kw.get('data')

    def to_dict(self):
        return {
            'id': self.id,
            'org_id': self.org_id,
            'name': self.name,
            'created': self.created,
            'has_template': self.template is not None,
            'data': self.data
        }

    def render(self):
        """
        Render the data as html.
        """
        t = Template(self.template)
        return t.render(data=self.data)

    def __repr__(self):
        return "<Report %r / %r >" % (self.org_id, self.name)
