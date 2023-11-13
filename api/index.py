from flask import Flask, request, redirect, render_template

app = Flask(__name__)

resolve_url = "https://simplifier.net/resolve?canonical={}&scope={}"

@app.route('/')
def home():
    example_indirect_canonical = "/fhir/ca/StructureDefinition/MaintainedDevice"
    example_direct_canonical = "/fhir/StructureDefinition/ACME-base-patient"
    return render_template('home.html',
                           example_indirect_canonical=example_indirect_canonical,
                           example_direct_canonical=example_direct_canonical)

@app.route('/fhir/ca/')
@app.route('/fhir/ca/<path:rest>')
def canonicalRedirectDirect(rest=None):
    canonical = str(request.url)
    scope = "acme.canada@latest"
    redirect_url = resolve_url.format(canonical, scope)
    return redirect(redirect_url, code=301)

@app.route('/fhir/')
@app.route('/fhir/<path:rest>')
def canonicalRedirectIndirect(rest=None):
    canonical = str(request.url)
    scope = "acme.base.r4@latest"
    redirect_url = resolve_url.format(canonical, scope)
    return render_template('redirect.html', redirect_url=redirect_url)
    
@app.route('/<path:rest>')
def Fallback(rest=None):
    return render_template('other.html')


    