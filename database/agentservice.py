from database import get_db
from database.models import TourAgent


def get_all_agent_db():
    db = next(get_db())
    agent = db.query(TourAgent).all()
    return agent


def add_agent_db(country_id, agent_name, agent_tellNo, agent_email, tour_cost):
    db = next(get_db())
    agent = TourAgent(country_id=country_id, agent_name=agent_name, agent_tellNo=agent_tellNo, agent_email=agent_email,
                      tour_cost=tour_cost)
    db.add(agent)
    db.commit()
    return 'Agent registered'


def get_agents_db(agent_id):
    db = next(get_db())
    agent = db.query(TourAgent).filter_by(agent_id=agent_id).first()
    if agent:
        return agent
    else:
        return f'Tour agent by {agent_id} ID not found'


def get_agents_by_country_db(country_id):
    db = next(get_db())
    agent = db.query(TourAgent).filter_by(country_id=country_id).all()
    if agent:
        return agent
    else:
        return f'Tour agents by {country_id} ID not found'


def edit_agent_db(agent_id, edit, new):
    db = next(get_db())
    agent = db.query(TourAgent).filter_by(agent_id=agent_id).first()
    if agent:
        if edit == 'agent_name':
            agent.agent_name = new
        elif edit == 'agent_tellNo':
            agent.agent_tellNo = new
        elif edit == 'agent_email':
            agent.agent_email = new
        elif edit == 'tour_cost':
            agent.tour_cost = new
        elif edit == 'country_id':
            agent.country_id = new
        else:
            return 'Argument not found!'
        db.commit()
        return agent
    else:
        return f'Tour agent by {agent_id} ID not found'


def delete_agent_db(agent_id):
    db = next(get_db())
    agent = db.query(TourAgent).filter_by(agent_id=agent_id).first()
    if agent:
        db.delete(agent)
        db.commit()
        return 'Agent deleted'
    else:
        return f'Tour agent by {agent_id} ID not found'

































