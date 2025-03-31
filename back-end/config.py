from flask import Blueprint, request, jsonify
from services.weather import OpenWeatherService, NWSService
from services.notifications import SMSService, EmailService
from utils.auth import token_required
from database.models import Alert, User

bp = Blueprint('alerts', __name__)

@bp.route('/alerts', methods=['GET'])
@token_required
def get_alerts(current_user):
    alerts = Alert.query.filter_by(user_id=current_user.id).all()
    return jsonify([alert.serialize() for alert in alerts])

@bp.route('/alerts/subscribe', methods=['POST'])
@token_required
def subscribe(current_user):
    data = request.json
    service = OpenWeatherService() if data['service'] == 'ow' else NWSService()
    
    alerts = service.get_alerts(data['lat'], data['lon'])
    for alert in alerts:
        # Save to DB
        new_alert = Alert(
            user_id=current_user.id,
            location=f"{data['lat']},{data['lon']}",
            alert_type=alert['event']
        )
        db.session.add(new_alert)
        
        # Send notifications
        if current_user.phone:
            SMSService.send_alert(current_user.phone, f"Weather Alert: {alert['description']}")
        EmailService.send_alert(
            current_user.email,
            "Weather Alert",
            f"<h1>{alert['event']}</h1><p>{alert['description']}</p>"
        )
    
    db.session.commit()
    return jsonify({"message": "Subscribed to alerts"})
