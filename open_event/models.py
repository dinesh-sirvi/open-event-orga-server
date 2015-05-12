from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    logo = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    location_name = db.Column(db.String)

    def __init__(self, name=None, logo=None, start_time=None, end_time=None, latitude=None, longitude=None, location_name=None):
        self.name = name
        self.logo = logo
        self.start_time = start_time
        self.end_time = end_time
        self.latitude = latitude
        self.longitude = longitude
        self.location_name = location_name

    def __repr__(self):
        return '<Event %r>' % (self.name)

speakers = db.Table('speakers_sessions',
    db.Column('speaker_id', db.Integer, db.ForeignKey('speaker.id')),
    db.Column('session_id', db.Integer, db.ForeignKey('session.id'))
)

class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    subtitle = db.Column(db.String)
    abstract = db.Column(db.Text)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    type = db.Column(db.String)
    track = db.Column(db.Integer)
    speakers = db.relationship('Speaker', secondary=speakers,
                                backref=db.backref('sessions', lazy='dynamic'))
    level = db.Column(db.String)
    microlocation = db.Column(db.Integer)

    def __init__(self,
                 title=None,
                 subtitle=None,
                 abstract=None,
                 description=None,
                 start_time=None,
                 end_time=None,
                 type=None,
                 track=None,
                 speakers=None,
                 level=None,
                 microlocation=None):
        self.title = title
        self.subtitle = subtitle
        self.abstract = abstract
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.type = type
        self.track = track
        self.speakers = speakers
        self.level = level
        self.microlocation = microlocation

    def __repr__(self):
        return '<Session %r>' % (self.title)


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Track %r>' % (self.name)

class Speaker(db.Model):
    __tablename__ = 'speaker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    photo = db.Column(db.String)
    biography = db.Column(db.Text)
    email = db.Column(db.String)
    web = db.Column(db.String)
    twitter = db.Column(db.String)
    facebook = db.Column(db.String)
    github = db.Column(db.String)
    linkedin = db.Column(db.String)
    organisation = db.Column(db.String)
    position = db.Column(db.String)
    country = db.Column(db.String)

    def __init__(self,
                 name=None,
                 photo=None,
                 biography=None,
                 email=None,
                 web=None,
                 twitter=None,
                 facebook=None,
                 github=None,
                 linkedin=None,
                 organisation=None,
                 position=None,
                 country=None):
        self.name = name
        self.photo = photo
        self.biography = biography
        self.email = email
        self.web = web
        self.twitter = twitter
        self.facebook = facebook
        self.github = github
        self.linkedin = linkedin
        self.organisation = organisation
        self.position = position
        self.country = country

    def __repr__(self):
        return '<Speaker %r>' % (self.name)

class Sponsor(db.Model):
    __tablename__ = 'sponsors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    logo = db.Column(db.String)

    def __init__(self, name=None, url=None, logo=None, ):
        self.name = name
        self.url = url
        self.logo = logo

    def __repr__(self):
        return '<Sponsor %r>' % (self.name)

class Microlocation(db.Model):
    __tablename__ = 'microlocations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    floor = db.Column(db.Integer)

    def __init__(self, name=None, latitude=None, longitude=None, floor=None ):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.floor = floor

    def __repr__(self):
        return '<Sponsor %r>' % (self.name)
