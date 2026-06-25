import uuid
from AIRE import db
"""
- requirements
  - requirement_id PK (the token)
  - json_requirement complete structured requirement JSON
  - source 'chatbot' | 'audio'
  - submitted_at timestamp

  ba_outputs
  - output_id PK
  - requirement_id FK → requirements
  - user_stories JSON
  - functional_label 'Functional' | 'Non-Functional'
  - generated_at timestamp
"""


class requirements(db.Model):
    requirement_id = db.Column(db.String(length=100), primary_key=True, default=lambda: str(uuid.uuid4())[:8].upper())
    json_requirement = db.Column(db.Text, nullable=False)  # db.Text allows long strings like JSON
    source = db.Column(db.String(length=50), nullable=False)
    submitted_at = db.Column(db.String(length=50), nullable=False)
    ba_outputs = db.relationship('ba_outputs', backref='ba_req', lazy=True)


class ba_outputs(db.Model):
    output_id = db.Column(db.Integer(), primary_key=True)
    user_stories = db.Column(db.Text, nullable=False)
    functional_label = db.Column(db.String(length=200), nullable=False)
    generated_at = db.Column(db.String(length=100), nullable=False)
    requirement_id = db.Column(db.String(length=100), db.ForeignKey('requirements.requirement_id'))
