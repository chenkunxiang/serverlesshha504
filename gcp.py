import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'glucose' in request_json:
        glucose_value = request_json['glucose']
    elif request_args and 'glucose' in request_args:
        glucose_value = request_args['glucose']
    else:
        glucose_value = 80
    
    try:
        glucose_value = float(glucose_value)
    except (TypeError, ValueError):
        return "Not Valid"

    lower_bound = 70
    upper_bound = 90

    if glucose_value < lower_bound:
        glucose_value_label = "Your glucose level is low"
    elif glucose_value > upper_bound:
        glucose_value_label = "Your glucose level is high"
    else:
        glucose_value_label = "Your glucose level is normal"

    return glucose_value_label
