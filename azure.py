import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    try:
        glucose_value = req.params.get('glucose')
        
        if not glucose_value:
            try:
                req_body = req.get_json()
            except ValueError:
                req_body = {}
            glucose_value = req_body.get('glucose', 80)

        try:
            glucose_value = float(glucose_value)
        except (TypeError, ValueError):
            return func.HttpResponse("Not Valid", status_code=400)

        lower_bound = 70
        upper_bound = 90

        if glucose_value < lower_bound:
            glucose_value_label = "Your glucose level is low"
        elif glucose_value > upper_bound:
            glucose_value_label = "Your glucose level is high"
        else:
            glucose_value_label = "Your glucose level is normal"

        return func.HttpResponse(glucose_value_label, status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
