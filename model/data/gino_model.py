from db_config.gino_connect import db

class Signup(db.Model):
    __tablename__ = 'signup'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.Text, unique=True)
    first_name = db.Column(db.Text, unique=True)
    last_name = db.Column(db.Text, unique=True)
    role = db.Column(db.Text)

class Signin(db.Model):
    __tablename__ = 'signin'
    id = db.Column(db.Integer, primary_key=True, default=lambda: db.Sequence('signin_id_seq').next_value())
    username = db.Column(db.String(45))
    password = db.Column(db.String(100))

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    role = db.Column(db.Text)

class Campaign(db.Model):
    __tablename__ = 'campaign'
    campaign_id = db.Column(db.Integer, primary_key=True, default=lambda: db.Sequence('campaign_id_seq').next_value())
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    goal_amount = db.Column(db.Numeric)
    raised_amount = db.Column(db.Numeric)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    category = db.Column(db.Text)
    media = db.Column(db.LargeBinary)
    status = db.Column(db.String(45))

class Donation(db.Model):
    __tablename__ = 'donation'
    donation_id = db.Column(db.Integer, primary_key=True, default=lambda: db.Sequence('donation_id_seq').next_value())
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.campaign_id'))
    donator_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    donation_amount = db.Column(db.Numeric)
    donation_date = db.Column(db.Date)
    message_leaving = db.Column(db.Text)

class Newsfeed(db.Model):
    __tablename__ = 'newsfeed'
    newsfeed_id = db.Column(db.Integer, primary_key=True, default=lambda: db.Sequence('newsfeed_id_seq').next_value())
    author = db.Column(db.String(45))
    headline = db.Column(db.Text)
    summary = db.Column(db.Text)
    media = db.Column(db.LargeBinary)
    publish_date = db.Column(db.Date)
    category = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
