from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return f'Welcome to our URL redirector!<br>'\
            +f'Try: <a href=\"\Base\StructureDefinition\Patient">\Base\StructureDefinition\Patient</a>'

@app.route('/')
@app.route('/<first>')
@app.route('/<first>/<path:rest>')
def fallback(first=None, rest=None):
    # return f'The current URL is: {request.url}'
    return redirect("https://simplifier.net/resolve?"\
                    +"canonical="+str(request.url)
                    +"&scope=hl7.fhir.r4.core@latest",
                    code=302)

    